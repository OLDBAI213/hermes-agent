import re

with open('ui-tui/src/lib/text.ts', 'r', encoding='utf-8') as f:
    lines = f.readlines()

result = []
in_conflict = False
keep_theirs = False

for line in lines:
    if line.startswith('<<<<<<< ours'):
        in_conflict = True
        keep_theirs = False
        continue
    elif line.startswith('=======') and in_conflict:
        keep_theirs = True
        continue
    elif line.startswith('>>>>>>> theirs') and in_conflict:
        in_conflict = False
        continue
    
    if in_conflict:
        if keep_theirs:
            result.append(line)
    else:
        result.append(line)

with open('ui-tui/src/lib/text.ts', 'w', encoding='utf-8') as f:
    f.writelines(result)

print(f'Done. Lines: {len(result)}')
