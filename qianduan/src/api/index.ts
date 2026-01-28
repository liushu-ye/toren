import axios from 'axios'

// 创建 axios 实例
const service = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
  timeout: 10000,
})

// 请求拦截器 - 统一添加 /api/ 前缀
service.interceptors.request.use(
  (config) => {
    // 如果不是绝对路径且不以 /api/ 开头，添加 /api/ 前缀
    if (config.url && !config.url.startsWith('http') && !config.url.startsWith('/api/')) {
      config.url = `/api/${config.url}`
    }
    return config
  },
  (error) => Promise.reject(error),
)

// 请求拦截器
service.interceptors.request.use(
  (config) => {
    // 这里可以统一添加 token
    const token = localStorage.getItem('token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => Promise.reject(error),
)

// 响应拦截器
service.interceptors.response.use(
  (response) => {
    const res = response.data
    if (res.code === 0) {
      return res.data
    } else {
      // 使用更优雅的错误处理方式，避免频繁 alert
      console.error('API错误:', res.message || '请求失败')
      return Promise.reject(res)
    }
  },
  (error) => {
    // 使用 console.error 替代 alert，避免浏览器保持活跃状态
    console.error('网络错误:', error.message || '网络错误或服务器异常')
    return Promise.reject(error)
  },
)

export default service
