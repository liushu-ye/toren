// 示例用户接口

import request from './index'

// 获取用户信息
export function getUserInfo() {
  return request.get('/user/me')
}

// 登录接口
export function login(data: { email: string; password: string }) {
  return request.post('/user/login', data)
}
