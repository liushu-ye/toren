<script setup lang="ts">
import { useUserStore } from '@/stores/user'

const { setToken, setUserInfo, clearToken } = useUserStore()

const login = () => {
  setToken('123456')
  setUserInfo({ id: 1, name: '张三' })
}

const logout = () => {
  clearToken()
}
</script>

<template>
  <button @click="login">登录吧</button>
  <button @click="logout">退出登录</button>
</template>

<style scoped></style>
