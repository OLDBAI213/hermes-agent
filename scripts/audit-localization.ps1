[CmdletBinding()]
param(
    [ValidateSet("all", "tui", "feishu", "lark-cli")]
    [string] $Scope = "all",

    [string] $Output = "",

    [switch] $IncludeTests,

    [switch] $FailOnMustReview
)

$ErrorActionPreference = "Stop"

$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$HermesHome = $env:HERMES_HOME
if (-not $HermesHome) {
    $parent = Split-Path $RepoRoot -Parent
    if (Test-Path (Join-Path $parent "config.yaml")) {
        $HermesHome = $parent
    }
}

$skipPathPattern = "(\\|/)(node_modules|dist|build|coverage|venv|\.venv|__pycache__|\.pytest_cache)(\\|/)"
$sourceExts = @(".ts", ".tsx", ".js", ".jsx", ".py", ".yaml", ".yml")
$quotedEnglishPattern = '["''`][^"''`]*[A-Za-z]{3,}[^"''`]*["''`]'
$compactKeyPattern = '^\w+:\s*["''`][a-z0-9_.-]+["''`],?$'
$displayFieldLiteralPattern = '["''`](label|title|description|message|placeholder|hint|help|status|summary|empty|error|warning|footer|tooltip|caption|content|text)["''`]\s*:\s*f?["''`]'
$feishuLiteralDisplayPattern = '["''`](content|title|text)["''`]\s*:\s*f?["''`]'

function Add-ScanPath {
    param(
        [System.Collections.Generic.List[object]] $Specs,
        [string] $Path,
        [string] $Kind
    )

    if (-not $Path) {
        return
    }
    if (Test-Path $Path) {
        $Specs.Add([pscustomobject]@{
            Path = (Resolve-Path $Path).Path
            Kind = $Kind
        }) | Out-Null
    }
}

function Get-RelativePath {
    param([string] $Path)

    if ($Path.StartsWith($RepoRoot, [System.StringComparison]::OrdinalIgnoreCase)) {
        return $Path.Substring($RepoRoot.Length).TrimStart("\", "/")
    }
    if ($HermesHome -and $Path.StartsWith($HermesHome, [System.StringComparison]::OrdinalIgnoreCase)) {
        return ('$HERMES_HOME\' + $Path.Substring($HermesHome.Length).TrimStart("\", "/"))
    }
    return $Path
}

function ConvertTo-MarkdownCell {
    param([string] $Text, [int] $Max = 180)

    if ($null -eq $Text) {
        return ""
    }
    $oneLine = $Text -replace "\s+", " "
    if ($oneLine.Length -gt $Max) {
        $oneLine = $oneLine.Substring(0, $Max - 1) + "…"
    }
    return ($oneLine -replace "\|", "\|")
}

function Get-UserFacingReason {
    param([string] $Line, [string] $Path)

    $trimmed = $Line.Trim()
    if ($trimmed -match "^(import|from|export\s+type|type\s+|interface\s+|enum\s+)" ) {
        return $null
    }
    if ($trimmed -match "^(//|#|\*)") {
        return $null
    }
    if ($trimmed -match "^logger\.") {
        return $null
    }
    if ($trimmed -match "^(label|title|description|message|placeholder|hint|help|status|summary|empty|error|warning|footer|tooltip|caption|reason|verb|fortune|charm|name)\s*[:=]") {
        return "user-facing field"
    }
    if ($trimmed -match $script:displayFieldLiteralPattern) {
        return "literal display field"
    }
    if ($trimmed -match ">[^<{}]*[A-Za-z]{3,}[^<{}]*<") {
        return "TUI JSX literal"
    }
    if ($trimmed -match "(print|console\.(log|error|warn)|raise\s+\w*Error|click\.echo|Prompt\.ask)\(") {
        return "user-facing output"
    }
    if ($trimmed -match "\b(sys|page|setStatus|pushActivity|pushTrail|newSession|guardBusySessionSwitch|OverlayHint)\s*\(" -or $trimmed -match "\btranscript\.(sys|page)\s*\(" -or $trimmed -match "\bturnController\.(pushActivity|pushTrail)\s*\(") {
        return "TUI status/output"
    }
    if ($Path -match "gateway\\platforms\\feishu|gateway/platforms/feishu|runtime_footer|display_config") {
        if ($trimmed -match "(_web_response|_web_json_response|_set_fatal_error|SendResult\(.*error=|raise\s+\w*Error)\(") {
            return "Feishu error/response"
        }
        if ($trimmed -match $script:feishuLiteralDisplayPattern) {
            return "Feishu literal display"
        }
    }
    if ($Path -match "lark-cli-toolbox") {
        if ($trimmed -match $script:displayFieldLiteralPattern) {
            return "lark-cli literal display"
        }
    }
    return $null
}

function Test-TechOnlyLine {
    param([string] $Line)

    $trimmed = $Line.Trim()
    if ($trimmed -match "https?://|www\.|localhost|127\.0\.0\.1") { return $true }
    if ($trimmed -cmatch "\b[A-Z][A-Z0-9_]{2,}\b") { return $true }
    if ($trimmed -match "\b(application/json|text/plain|multipart/form-data|Authorization|Content-Type)\b") { return $true }
    if ($trimmed -match "\b(true|false|null|None|async|await|return|const|let|var|class|function|def|if|else|for|while|switch|case|try|except|catch)\b") {
        if ($trimmed -notmatch $script:quotedEnglishPattern) {
            return $true
        }
    }
    if ($trimmed -match "\b(feishu|lark|telegram|slack|discord|openai|anthropic|provider|model|session_id|message_id|chat_id|user_id|tool_call|event_type)\b") {
        if ($trimmed -notmatch "(label|title|description|message|placeholder|hint|help|status|summary|empty|error|warning|footer|tooltip|caption|content|text)\s*[:=]") {
            return $true
        }
    }
    if ($trimmed -match $script:compactKeyPattern) { return $true }
    return $false
}

$scanSpecs = [System.Collections.Generic.List[object]]::new()
if ($Scope -in @("all", "tui")) {
    Add-ScanPath $scanSpecs (Join-Path $RepoRoot "ui-tui\src") "tui"
}
if ($Scope -in @("all", "feishu")) {
    Add-ScanPath $scanSpecs (Join-Path $RepoRoot "gateway\platforms\feishu.py") "feishu"
    Add-ScanPath $scanSpecs (Join-Path $RepoRoot "gateway\platforms\feishu_comment.py") "feishu"
    Add-ScanPath $scanSpecs (Join-Path $RepoRoot "gateway\platforms\feishu_comment_rules.py") "feishu"
    Add-ScanPath $scanSpecs (Join-Path $RepoRoot "gateway\runtime_footer.py") "feishu"
    Add-ScanPath $scanSpecs (Join-Path $RepoRoot "gateway\display_config.py") "feishu"
}
if ($Scope -in @("all", "lark-cli")) {
    Add-ScanPath $scanSpecs (Join-Path $RepoRoot "plugins\lark-cli-toolbox") "lark-cli"
    if ($HermesHome) {
        Add-ScanPath $scanSpecs (Join-Path $HermesHome "plugins\lark-cli-toolbox") "lark-cli"
    }
}

$files = [System.Collections.Generic.List[object]]::new()
foreach ($spec in $scanSpecs) {
    if ((Get-Item $spec.Path).PSIsContainer) {
        Get-ChildItem $spec.Path -Recurse -File | Where-Object {
            $sourceExts -contains $_.Extension `
                -and $_.FullName -notmatch $skipPathPattern `
                -and ($IncludeTests -or ($_.FullName -notmatch "(\\|/)__tests__(\\|/)" -and $_.Name -notmatch "\.test\.(ts|tsx|js|jsx|py)$"))
        } | ForEach-Object {
            $files.Add([pscustomobject]@{ File = $_.FullName; Kind = $spec.Kind }) | Out-Null
        }
    }
    else {
        $item = Get-Item $spec.Path
        if ($sourceExts -contains $item.Extension) {
            $files.Add([pscustomobject]@{ File = $item.FullName; Kind = $spec.Kind }) | Out-Null
        }
    }
}

$results = [System.Collections.Generic.List[object]]::new()
foreach ($entry in $files) {
    $lineNo = 0
    foreach ($line in Get-Content -LiteralPath $entry.File -Encoding UTF8) {
        $lineNo += 1
        $hasChinese = $line -match "[一-龯]"
        $hasEnglishText = $line -match $quotedEnglishPattern -or $line -match ">[A-Za-z][^<>{}]{2,}<"
        if (-not $hasChinese -and -not $hasEnglishText) {
            continue
        }

        $reason = Get-UserFacingReason $line $entry.File
        $isTechOnly = Test-TechOnlyLine $line
        $category = "could_review"
        if ($hasChinese -and -not $hasEnglishText) {
            $category = "already_zh"
            $reason = "contains Chinese"
        }
        elseif ($hasChinese -and $hasEnglishText) {
            if ($isTechOnly) {
                $category = "skip_tech"
                if (-not $reason) { $reason = "mixed technical/protocol line" }
            }
            elseif ($reason) {
                $category = "mixed_review"
            }
            else {
                $category = "could_review"
                $reason = "mixed Chinese and English, visibility unknown"
            }
        }
        elseif ($reason -and -not $isTechOnly) {
            $category = "must_review"
        }
        elseif ($isTechOnly) {
            $category = "skip_tech"
            if (-not $reason) { $reason = "technical/protocol line" }
        }
        elseif (-not $reason) {
            $reason = "English string, visibility unknown"
        }

        if ($category -eq "already_zh") {
            continue
        }

        $results.Add([pscustomobject]@{
            Category = $category
            Scope = $entry.Kind
            Path = Get-RelativePath $entry.File
            Line = $lineNo
            Reason = $reason
            Text = $line.Trim()
        }) | Out-Null
    }
}

$ordered = $results | Sort-Object @{ Expression = {
        switch ($_.Category) {
            "must_review" { 0 }
            "mixed_review" { 1 }
            "could_review" { 2 }
            "skip_tech" { 3 }
            default { 9 }
        }
    } }, Scope, Path, Line

$summary = $ordered | Group-Object Category | Sort-Object Name | ForEach-Object {
    [pscustomobject]@{ Category = $_.Name; Count = $_.Count }
}

Write-Host "Localization audit scope: $Scope"
Write-Host "Repo: $RepoRoot"
if ($HermesHome) { Write-Host "HERMES_HOME: $HermesHome" }
$summary | Format-Table -AutoSize

$must = @($ordered | Where-Object { $_.Category -eq "must_review" })
if ($must.Count -gt 0) {
    Write-Host ""
    Write-Host "Top must_review items:"
    $must | Select-Object -First 40 Scope, Path, Line, Reason, Text | Format-Table -Wrap
}

if ($Output) {
    $outPath = if ([System.IO.Path]::IsPathRooted($Output)) { $Output } else { Join-Path $RepoRoot $Output }
    $outDir = Split-Path $outPath -Parent
    if ($outDir -and -not (Test-Path $outDir)) {
        New-Item -ItemType Directory -Path $outDir | Out-Null
    }

    $lines = [System.Collections.Generic.List[string]]::new()
    $lines.Add("# Localization Audit Current") | Out-Null
    $lines.Add("") | Out-Null
    $lines.Add("- Generated: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz')") | Out-Null
    $lines.Add("- Scope: $Scope") | Out-Null
    $lines.Add("- Repo: $RepoRoot") | Out-Null
    if ($HermesHome) { $lines.Add("- HERMES_HOME: $HermesHome") | Out-Null }
    $lines.Add("") | Out-Null
    $lines.Add("## Summary") | Out-Null
    $lines.Add("") | Out-Null
    $lines.Add("| Category | Count |") | Out-Null
    $lines.Add("| --- | ---: |") | Out-Null
    foreach ($item in $summary) {
        $lines.Add("| $($item.Category) | $($item.Count) |") | Out-Null
    }

    foreach ($category in @("must_review", "mixed_review", "could_review", "skip_tech")) {
        $items = @($ordered | Where-Object { $_.Category -eq $category })
        $lines.Add("") | Out-Null
        $lines.Add("## $category") | Out-Null
        $lines.Add("") | Out-Null
        if ($items.Count -eq 0) {
            $lines.Add("_No items._") | Out-Null
            continue
        }
        $lines.Add("| Scope | File | Line | Reason | Text |") | Out-Null
        $lines.Add("| --- | --- | ---: | --- | --- |") | Out-Null
        foreach ($item in $items) {
            $lines.Add("| $($item.Scope) | $(ConvertTo-MarkdownCell $item.Path 110) | $($item.Line) | $(ConvertTo-MarkdownCell $item.Reason 80) | $(ConvertTo-MarkdownCell $item.Text 220) |") | Out-Null
        }
    }

    Set-Content -LiteralPath $outPath -Value $lines -Encoding UTF8
    Write-Host ""
    Write-Host "Report written: $outPath"
}

if ($FailOnMustReview -and $must.Count -gt 0) {
    throw "Localization audit found $($must.Count) must_review item(s)."
}
