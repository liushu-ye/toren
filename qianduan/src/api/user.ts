// 示例用户接口
import request from './index'

export interface User {
  id: number
  email: string
  name: string
}
// 获取用户信息
export function getUserInfo() {
  return request.get<User>('/user/me')
}

// 登录接口
export function login(data: { email: string; password: string }) {
  return request.post<User>('/user/login', data)
}
