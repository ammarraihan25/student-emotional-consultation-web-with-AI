import http from './axios'

export async function login(email, password) {
  // TODO: POST /api/login → returns { user, token }
  // Mock for demo
  if (email && password) {
    return {
      user: { id: 1, name: 'Mahasiswa Demo', email },
      token: 'demo-token-aether-2024'
    }
  }
  throw new Error('Email atau password salah')
}

export async function register(name, email, password) {
  // TODO: POST /api/register
  return {
    user: { id: 1, name, email },
    token: 'demo-token-aether-2024'
  }
}

export async function getUser() {
  // TODO: GET /api/user
  return { id: 1, name: 'Mahasiswa Demo', email: 'demo@aether.ai' }
}

export async function logout() {
  // TODO: POST /api/logout
  return true
}
