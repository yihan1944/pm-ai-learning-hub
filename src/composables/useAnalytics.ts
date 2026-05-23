const PV_KEY = 'pm_ai_pv'
const UV_KEY = 'pm_ai_uv'
const UV_SESSION_KEY = 'pm_ai_uv_session'

export function useAnalytics() {
  // PV: 每次访问 +1
  const getPv = (): number => {
    const stored = localStorage.getItem(PV_KEY)
    const count = stored ? parseInt(stored, 10) : 0
    const newCount = count + 1
    localStorage.setItem(PV_KEY, String(newCount))
    return newCount
  }

  // UV: 每个浏览器会话只计一次
  const getUv = (): number => {
    const stored = localStorage.getItem(UV_KEY)
    const count = stored ? parseInt(stored, 10) : 0
    const sessionMark = sessionStorage.getItem(UV_SESSION_KEY)
    if (!sessionMark) {
      const newCount = count + 1
      localStorage.setItem(UV_KEY, String(newCount))
      sessionStorage.setItem(UV_SESSION_KEY, '1')
      return newCount
    }
    return count
  }

  const pv = getPv()
  const uv = getUv()

  return { pv, uv }
}
