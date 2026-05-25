const FORTUNES = [
  '一次干净重构，就能把问题看清楚',
  '今天的小改名，能挡住明天的大 bug',
  '下一条提交信息会非常清楚',
  '你担心的边界条件，答案已经在代码里',
  '小 diff，大安稳',
  '今天适合大胆删除，不适合新增抽象',
  '真正该用的 helper 已经在项目里',
  '先交付，再让过度思考追上来',
  '测试马上会救未来的你一次',
  '你对那条分支的怀疑是对的'
]

const LEGENDARY = [
  '传说掉落：一行修复，一次通过',
  '传说掉落：所有 flaky test 都干净通过',
  '传说掉落：这个 diff 自带说明书'
]

const hash = (s: string) => [...s].reduce((h, c) => Math.imul(h ^ c.charCodeAt(0), 16777619), 2166136261) >>> 0

const fromScore = (n: number) => {
  const rare = n % 20 === 0
  const bag = rare ? LEGENDARY : FORTUNES

  return `${rare ? '🌟' : '🔮'} ${bag[n % bag.length]}`
}

export const randomFortune = () => fromScore(Math.floor(Math.random() * 0x7fffffff))
export const dailyFortune = (seed: null | string) => fromScore(hash(`${seed || 'anon'}|${new Date().toDateString()}`))
