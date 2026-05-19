import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

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

  // Demo: auto-login with mock user for development
  function demoLogin() {
    setAuth(
      { id: 1, name: 'Mahasiswa Demo', email: 'demo@aether.ai', avatar: null },
      'demo-token-aether-2024'
    )
  }

  return { user, token, isAuthenticated, setAuth, logout, demoLogin }
})
