const FORTUNES = [
  '一次清爽重构就能让问题变清楚',
  '今天的小命名，挡住明天的大问题',
  '下一条提交信息会很干净',
  '你怀疑的边界条件值得复查',
  '改动越小，判断越稳',
  '今天适合大胆删除，不急着加抽象',
  '合适的 helper 已经在代码库里',
  '先发可验证结果，再继续打磨',
  '测试马上会替未来的你省时间',
  '你对那条分支的怀疑是有价值的'
]

const LEGENDARY = [
  '传说掉落：一行修好，一次通过',
  '传说掉落：所有不稳定测试都干净通过',
  '传说掉落：你的 diff 自己会说明问题'
]

const hash = (s: string) => [...s].reduce((h, c) => Math.imul(h ^ c.charCodeAt(0), 16777619), 2166136261) >>> 0

const fromScore = (n: number) => {
  const rare = n % 20 === 0
  const bag = rare ? LEGENDARY : FORTUNES

  return `${rare ? '🌟' : '🔮'} ${bag[n % bag.length]}`
}

export const randomFortune = () => fromScore(Math.floor(Math.random() * 0x7fffffff))
export const dailyFortune = (seed: null | string) => fromScore(hash(`${seed || 'anon'}|${new Date().toDateString()}`))
