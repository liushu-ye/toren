import axios from 'axios'

// 创建 axios 实例
const service = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL, // 读取 .env 配置
  timeout: 10000,
})

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
  (error) => Promise.reject(error)
)

// 响应拦截器
service.interceptors.response.use(
  (response) => {
    const res = response.data
    if (res.code === 0) {
      return res.data
    } else {
      // 这里可以做统一错误提示处理
      window.alert(res.message || '请求失败')
      return Promise.reject(res)
    }
  },
  (error) => {
    window.alert('网络错误或服务器异常')
    return Promise.reject(error)
  }
)

export default service
