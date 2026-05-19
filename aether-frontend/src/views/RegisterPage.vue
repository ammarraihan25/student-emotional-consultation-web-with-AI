<template>
  <div class="min-h-screen bg-[#050b18] flex items-center justify-center px-4 relative overflow-hidden py-16">
    <div class="fixed inset-0 pointer-events-none">
      <div class="absolute top-[-20%] right-[-10%] w-96 h-96 rounded-full bg-cyan-700/20 blur-[120px] animate-float2"></div>
      <div class="absolute bottom-[-10%] left-[-10%] w-80 h-80 rounded-full bg-purple-700/25 blur-[100px] animate-float"></div>
    </div>

    <div class="relative w-full max-w-md z-10">
      <div class="text-center mb-8">
        <router-link to="/" class="inline-flex items-center gap-3 mb-6">
          <div class="relative">
            <div class="w-11 h-11 rounded-2xl bg-gradient-to-br from-purple-600 to-cyan-500 flex items-center justify-center">
              <span class="text-white font-black text-xl">Æ</span>
            </div>
            <div class="absolute inset-0 rounded-2xl bg-gradient-to-br from-purple-600 to-cyan-500 blur-md opacity-50"></div>
          </div>
          <span class="font-bold text-2xl gradient-text">Aether</span>
        </router-link>
        <h1 class="text-2xl font-bold text-white mb-2">Buat akun baru</h1>
        <p class="text-sm text-white/50">Mulai perjalanan emosionalmu bersama AI</p>
      </div>

      <div class="glass gradient-border rounded-3xl p-8">
        <form @submit.prevent="handleRegister" class="space-y-5">
          <div v-if="error" class="bg-red-500/10 border border-red-500/30 rounded-xl px-4 py-3 text-sm text-red-400 flex items-center gap-2">
            <AlertCircle :size="16" /> {{ error }}
          </div>

          <div>
            <label class="block text-xs text-white/50 font-medium mb-2">Nama Lengkap</label>
            <div class="relative">
              <User :size="16" class="absolute left-3.5 top-1/2 -translate-y-1/2 text-white/30" />
              <input v-model="form.name" type="text" required
                class="w-full bg-white/5 border border-white/10 rounded-xl px-4 py-3 pl-10 text-sm text-white placeholder-white/25 outline-none focus:border-purple-500/60 focus:bg-white/8 transition-all"
                placeholder="Nama kamu" />
            </div>
          </div>

          <div>
            <label class="block text-xs text-white/50 font-medium mb-2">Email</label>
            <div class="relative">
              <Mail :size="16" class="absolute left-3.5 top-1/2 -translate-y-1/2 text-white/30" />
              <input v-model="form.email" type="email" required
                class="w-full bg-white/5 border border-white/10 rounded-xl px-4 py-3 pl-10 text-sm text-white placeholder-white/25 outline-none focus:border-purple-500/60 focus:bg-white/8 transition-all"
                placeholder="nama@email.com" />
            </div>
          </div>

          <div>
            <label class="block text-xs text-white/50 font-medium mb-2">Password</label>
            <div class="relative">
              <Lock :size="16" class="absolute left-3.5 top-1/2 -translate-y-1/2 text-white/30" />
              <input v-model="form.password" :type="showPw ? 'text' : 'password'" required minlength="8"
                class="w-full bg-white/5 border border-white/10 rounded-xl px-4 py-3 pl-10 pr-10 text-sm text-white placeholder-white/25 outline-none focus:border-purple-500/60 focus:bg-white/8 transition-all"
                placeholder="Minimal 8 karakter" />
              <button type="button" @click="showPw = !showPw" class="absolute right-3.5 top-1/2 -translate-y-1/2 text-white/30 hover:text-white/60">
                <component :is="showPw ? EyeOff : Eye" :size="16" />
              </button>
            </div>
            <!-- Strength indicator -->
            <div class="flex gap-1 mt-2">
              <div v-for="i in 4" :key="i" :class="['h-1 flex-1 rounded-full transition-all', i <= pwStrength ? strengthColor : 'bg-white/10']"></div>
            </div>
          </div>

          <div class="flex items-start gap-3">
            <button type="button" @click="form.agree = !form.agree"
              :class="['w-5 h-5 rounded border transition-all flex items-center justify-center mt-0.5 shrink-0',
                form.agree ? 'bg-purple-500 border-purple-500' : 'border-white/20 bg-white/5']">
              <Check v-if="form.agree" :size="12" class="text-white" />
            </button>
            <span class="text-xs text-white/50 leading-relaxed">Saya menyetujui <a href="#" class="text-purple-400">Syarat & Ketentuan</a> dan <a href="#" class="text-purple-400">Kebijakan Privasi</a> Aether.</span>
          </div>

          <button type="submit" :disabled="loading || !form.agree"
            class="btn-glow w-full text-white font-bold py-3.5 rounded-xl text-sm flex items-center justify-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed">
            <Loader2 v-if="loading" :size="16" class="animate-spin" />
            <UserPlus v-else :size="16" />
            {{ loading ? 'Mendaftar...' : 'Buat Akun' }}
          </button>
        </form>

        <p class="text-center text-xs text-white/40 mt-6">
          Sudah punya akun?
          <router-link to="/login" class="text-purple-400 hover:text-purple-300 font-medium transition-colors"> Masuk</router-link>
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { User, Mail, Lock, Eye, EyeOff, UserPlus, Loader2, AlertCircle, Check } from '@lucide/vue'
import { useAuthStore } from '@/stores/auth'
import { register } from '@/api/auth'

const router = useRouter()
const auth = useAuthStore()

const form = ref({ name: '', email: '', password: '', agree: false })
const loading = ref(false)
const error = ref('')
const showPw = ref(false)

const pwStrength = computed(() => {
  const p = form.value.password
  if (!p) return 0
  let s = 0
  if (p.length >= 8) s++
  if (/[A-Z]/.test(p)) s++
  if (/[0-9]/.test(p)) s++
  if (/[^A-Za-z0-9]/.test(p)) s++
  return s
})
const strengthColor = computed(() => {
  const map = { 1: 'bg-red-500', 2: 'bg-orange-500', 3: 'bg-yellow-500', 4: 'bg-emerald-500' }
  return map[pwStrength.value] || 'bg-white/10'
})

async function handleRegister() {
  if (!form.value.agree) return
  loading.value = true
  error.value = ''
  try {
    const { user, token } = await register(form.value.name, form.value.email, form.value.password)
    auth.setAuth(user, token)
    router.push('/chat')
  } catch (e) {
    error.value = e.message || 'Gagal mendaftar. Coba lagi.'
  } finally {
    loading.value = false
  }
}
</script>
