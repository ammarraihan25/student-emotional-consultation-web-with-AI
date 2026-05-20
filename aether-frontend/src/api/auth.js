import http from './axios'

export async function login(email, password) {
  const response = await http.post('/login', { email, password })
  return response.data // { user, token }
}

export async function demoLogin() {
  const response = await http.post('/demo-login')
  return response.data // { user, token }
}

export async function register(name, email, password, password_confirmation) {
  const response = await http.post('/register', { name, email, password, password_confirmation })
  return response.data // { user, token }
}

export async function getUser() {
  const response = await http.get('/user')
  return response.data
}

export async function logout() {
  await http.post('/logout')
  return true
}
