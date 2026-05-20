import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { demoLogin as apiDemoLogin, getUser } from '@/api/auth'

export const useAuthStore = defineStore('auth', () => {
  const user = ref(null)
  const token = ref(localStorage.getItem('aether_token') || null)

  const isAuthenticated = computed(() => !!token.value)

  function setAuth(userData, tokenValue) {
    user.value = userData
    token.value = tokenValue
    localStorage.setItem('aether_token', tokenValue)
  }

  function logout() {
    user.value = null
    token.value = null
    localStorage.removeItem('aether_token')
  }

  // Fetch logged in user profile to restore state on reload
  async function fetchUser() {
    if (!token.value) return null
    try {
      const userData = await getUser()
      user.value = userData
      return userData
    } catch (err) {
      console.error('Failed to fetch user profile', err)
      logout()
      throw err
    }
  }

  // Demo: auto-login by calling the backend
  async function demoLogin() {
    try {
      const { user: userData, token: tokenValue } = await apiDemoLogin()
      setAuth(userData, tokenValue)
      return true
    } catch (err) {
      console.error('Demo login failed', err)
      throw err
    }
  }

  return { user, token, isAuthenticated, setAuth, logout, fetchUser, demoLogin }
})

