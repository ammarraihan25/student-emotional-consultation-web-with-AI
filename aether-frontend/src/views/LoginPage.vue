<template>
  <div class="min-h-screen bg-[#050b18] flex items-center justify-center px-4 relative overflow-hidden">
    <!-- Blobs -->
    <div class="fixed inset-0 pointer-events-none">
      <div class="absolute top-[-20%] left-[-10%] w-96 h-96 rounded-full bg-purple-700/25 blur-[120px] animate-float"></div>
      <div class="absolute bottom-[-10%] right-[-10%] w-80 h-80 rounded-full bg-cyan-600/20 blur-[100px] animate-float2"></div>
    </div>

    <div class="relative w-full max-w-md z-10">
      <!-- Logo -->
      <div class="text-center mb-8">
        <router-link to="/" class="inline-flex items-center gap-3 mb-6">
          <div class="relative">
            <div class="w-11 h-11 rounded-2xl bg-gradient-to-br from-purple-600 to-cyan-500 flex items-center justify-center shadow-lg">
              <span class="text-white font-black text-xl">Æ</span>
            </div>
            <div class="absolute inset-0 rounded-2xl bg-gradient-to-br from-purple-600 to-cyan-500 blur-md opacity-50"></div>
          </div>
          <span class="font-bold text-2xl gradient-text">Aether</span>
        </router-link>
        <h1 class="text-2xl font-bold text-white mb-2">Selamat datang kembali</h1>
        <p class="text-sm text-white/50">Masuk untuk melanjutkan perjalanan emosionalmu</p>
      </div>

      <!-- Card -->
      <div class="glass gradient-border rounded-3xl p-8">
        <form @submit.prevent="handleLogin" class="space-y-5">
          <!-- Error -->
          <div v-if="error" class="bg-red-500/10 border border-red-500/30 rounded-xl px-4 py-3 text-sm text-red-400 flex items-center gap-2">
            <AlertCircle :size="16" /> {{ error }}
          </div>

          <!-- Email -->
          <div>
            <label class="block text-xs text-white/50 font-medium mb-2">Email</label>
            <div class="relative">
              <Mail :size="16" class="absolute left-3.5 top-1/2 -translate-y-1/2 text-white/30" />
              <input v-model="form.email" type="email" required
                class="w-full bg-white/5 border border-white/10 rounded-xl px-4 py-3 pl-10 text-sm text-white placeholder-white/25 outline-none focus:border-purple-500/60 focus:bg-white/8 transition-all"
                placeholder="nama@email.com" />
            </div>
          </div>

          <!-- Password -->
          <div>
            <div class="flex justify-between mb-2">
              <label class="text-xs text-white/50 font-medium">Password</label>
              <a href="#" class="text-xs text-purple-400 hover:text-purple-300 transition-colors">Lupa password?</a>
            </div>
            <div class="relative">
              <Lock :size="16" class="absolute left-3.5 top-1/2 -translate-y-1/2 text-white/30" />
              <input v-model="form.password" :type="showPw ? 'text' : 'password'" required
                class="w-full bg-white/5 border border-white/10 rounded-xl px-4 py-3 pl-10 pr-10 text-sm text-white placeholder-white/25 outline-none focus:border-purple-500/60 focus:bg-white/8 transition-all"
                placeholder="••••••••" />
              <button type="button" @click="showPw = !showPw" class="absolute right-3.5 top-1/2 -translate-y-1/2 text-white/30 hover:text-white/60">
                <component :is="showPw ? EyeOff : Eye" :size="16" />
              </button>
            </div>
          </div>

          <!-- Remember me -->
          <div class="flex items-center gap-3">
            <button type="button" @click="form.remember = !form.remember"
              :class="['w-5 h-5 rounded border transition-all flex items-center justify-center',
                form.remember ? 'bg-purple-500 border-purple-500' : 'border-white/20 bg-white/5']">
              <Check v-if="form.remember" :size="12" class="text-white" />
            </button>
            <span class="text-xs text-white/50">Ingat saya</span>
          </div>

          <!-- Submit -->
          <button type="submit" :disabled="loading"
            class="btn-glow w-full text-white font-bold py-3.5 rounded-xl text-sm flex items-center justify-center gap-2">
            <Loader2 v-if="loading" :size="16" class="animate-spin" />
            <LogIn v-else :size="16" />
            {{ loading ? 'Memproses...' : 'Masuk' }}
          </button>
        </form>

        <!-- Demo login -->
        <button @click="demoLogin"
          class="mt-3 w-full py-3 rounded-xl text-xs text-white/50 border border-white/10 hover:bg-white/5 hover:text-white/70 transition-all flex items-center justify-center gap-2">
          <Zap :size="13" class="text-cyan-400" /> Coba Demo (tanpa daftar)
        </button>

        <p class="text-center text-xs text-white/40 mt-6">
          Belum punya akun?
          <router-link to="/register" class="text-purple-400 hover:text-purple-300 font-medium transition-colors"> Daftar sekarang</router-link>
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { Mail, Lock, Eye, EyeOff, LogIn, Loader2, AlertCircle, Check, Zap } from '@lucide/vue'
import { useAuthStore } from '@/stores/auth'
import { login } from '@/api/auth'

const router = useRouter()
const auth = useAuthStore()

const form = ref({ email: '', password: '', remember: false })
const loading = ref(false)
const error = ref('')
const showPw = ref(false)

async function handleLogin() {
  loading.value = true
  error.value = ''
  try {
    const { user, token } = await login(form.value.email, form.value.password)
    auth.setAuth(user, token)
    router.push('/chat')
  } catch (e) {
    error.value = e.message || 'Terjadi kesalahan. Coba lagi.'
  } finally {
    loading.value = false
  }
}

function demoLogin() {
  auth.demoLogin()
  router.push('/chat')
}
</script>
