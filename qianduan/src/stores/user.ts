import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

interface UserInfo {
  id: number
  name: string
  email?: string
}

export const useUserStore = defineStore('user', () => {
  // state
  const getTokenFromStorage = () => {
    try {
      return localStorage.getItem('token') || ''
    } catch {
      return ''
    }
  }

  const token = ref<string>(getTokenFromStorage())
  const userInfo = ref<UserInfo | null>(null)

  // actions
  const setToken = (newToken: string) => {
    token.value = newToken
    localStorage.setItem('token', newToken)
  }

  const clearToken = () => {
    token.value = ''
    localStorage.removeItem('token')
    userInfo.value = null
  }

  const setUserInfo = (info: UserInfo) => {
    userInfo.value = info
  }

  // getters
  const isLoggedIn = computed(() => !!token.value)

  return {
    token,
    userInfo,
    setToken,
    clearToken,
    setUserInfo,
    isLoggedIn,
  }
})
