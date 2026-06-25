<template>
  <div class="min-h-screen bg-slate-50 dark:bg-[#020817] flex font-sans overflow-hidden text-slate-900 dark:text-slate-100 transition-colors duration-300">
    
    <!-- LEFT SIDE: Mascot & Quote (Hidden on mobile) -->
    <div class="hidden lg:flex lg:w-1/2 relative flex-col items-center justify-center p-12 border-r border-slate-200 dark:border-white/5 bg-slate-100 dark:bg-gradient-to-b dark:from-[#020817] dark:to-[#0A172B]">
      <!-- Background animations & Variations -->
      <div class="absolute inset-0 overflow-hidden pointer-events-none">
        <div class="absolute top-[10%] left-[10%] w-[500px] h-[500px] bg-gradient-to-tr from-[#16D5D2]/10 to-transparent blur-[120px] rounded-full animate-float-slow"></div>
        <div class="absolute bottom-[10%] right-[10%] w-[400px] h-[400px] bg-gradient-to-bl from-[#8B5CF6]/10 to-transparent blur-[100px] rounded-full animate-float"></div>
        
        <!-- Decorative Rings -->
        <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] border border-white/5 rounded-full z-0"></div>
        <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[450px] h-[450px] border border-dashed border-[#16D5D2]/20 rounded-full animate-spin-slow z-0" style="animation-duration: 25s;"></div>

        <!-- Tiny stars/particles -->
        <div class="absolute top-[30%] left-[20%] w-1.5 h-1.5 bg-white rounded-full animate-pulse shadow-[0_0_10px_white]"></div>
        <div class="absolute top-[60%] left-[80%] w-2 h-2 bg-[#36CFFF] rounded-full animate-pulse shadow-[0_0_15px_#36CFFF]" style="animation-delay: 1s"></div>
        <div class="absolute top-[80%] left-[30%] w-1.5 h-1.5 bg-[#16D5D2] rounded-full animate-pulse shadow-[0_0_10px_#16D5D2]" style="animation-delay: 2s"></div>
      </div>

      <!-- Content -->
      <div class="relative z-10 flex flex-col items-center max-w-lg mx-auto mt-[-5%]">
        <img src="/images/aether6.png" alt="Aether Mascot" class="w-[350px] h-auto mb-12 animate-float drop-shadow-[0_30px_60px_rgba(22,213,210,0.25)]" />
        
        <div class="glass-panel px-8 py-6 text-center border-t border-[#16D5D2]/20 bg-white/50 dark:bg-transparent shadow-lg dark:shadow-[0_20px_50px_rgba(0,0,0,0.5)]">
          <h2 class="text-3xl font-serif italic leading-snug mb-3 text-slate-900 dark:text-white">
            "Kamu tidak harus menghadapi <br/> semuanya sendirian."
          </h2>
          <div class="flex items-center justify-center gap-3">
            <span class="w-8 h-[1px] bg-[#16D5D2]/50"></span>
            <p class="text-[#16D5D2] font-semibold tracking-widest text-xs uppercase">Aether Mental Health AI</p>
            <span class="w-8 h-[1px] bg-[#16D5D2]/50"></span>
          </div>
        </div>
      </div>
    </div>

    <!-- RIGHT SIDE: Login Form -->
    <div class="w-full lg:w-1/2 flex items-center justify-center p-6 sm:p-12 relative">
      <!-- Mobile Background -->
      <div class="absolute inset-0 lg:hidden overflow-hidden pointer-events-none">
        <div class="absolute top-[-10%] right-[-10%] w-64 h-64 bg-[#16D5D2]/10 blur-[100px] rounded-full"></div>
      </div>

      <div class="w-full max-w-md animate-fade-in-up">
        
        <!-- Header area with Logo and ThemeToggle -->
        <div class="flex items-center justify-between mb-12">
          <router-link to="/" class="inline-flex items-center gap-2 group">
            <span class="font-sans font-bold tracking-wide text-2xl text-slate-900 dark:text-white transition-colors">Aether</span>
          </router-link>
          <ThemeToggle />
        </div>

        <h1 class="text-4xl font-serif font-bold text-slate-900 dark:text-white mb-3 tracking-tight">Selamat Datang Kembali</h1>
        <p class="text-slate-600 dark:text-slate-400 mb-10 text-base">Masuk untuk melanjutkan perjalanan emosionalmu.</p>

        <!-- Login Card -->
        <div class="glass-panel p-8 bg-white/80 dark:bg-white/5 border border-slate-200 dark:border-white/10 shadow-xl dark:shadow-none">
          <form @submit.prevent="handleLogin" class="space-y-6">
            
            <!-- Error Alert -->
            <div v-if="error" class="bg-red-500/10 border border-red-500/30 rounded-2xl px-4 py-3 text-sm text-red-400 flex items-center gap-2">
              <AlertCircle :size="16" /> {{ error }}
            </div>

            <!-- Email -->
            <div>
              <label class="block text-xs text-slate-500 dark:text-slate-400 font-medium mb-2 uppercase tracking-wide">Email</label>
              <div class="relative">
                <Mail :size="18" class="absolute left-4 top-1/2 -translate-y-1/2 text-slate-400 dark:text-slate-500" />
                <input v-model="form.email" type="email" required
                  class="w-full bg-slate-50 dark:bg-white/5 border border-slate-200 dark:border-white/10 rounded-2xl px-4 py-3.5 pl-11 text-sm text-slate-900 dark:text-white placeholder-slate-400 dark:placeholder-slate-500 outline-none focus:border-[#16D5D2]/60 focus:bg-white focus:dark:bg-white/10 transition-all glow-cyan-border focus:glow-cyan-border shadow-inner dark:shadow-none"
                  placeholder="nama@email.com" />
              </div>
            </div>

            <!-- Password -->
            <div>
              <div class="flex justify-between items-center mb-2">
                <label class="block text-xs text-slate-500 dark:text-slate-400 font-medium uppercase tracking-wide">Password</label>
                <a href="#" class="text-xs text-[#16D5D2] hover:text-[#36CFFF] transition-colors">Lupa password?</a>
              </div>
              <div class="relative">
                <Lock :size="18" class="absolute left-4 top-1/2 -translate-y-1/2 text-slate-400 dark:text-slate-500" />
                <input v-model="form.password" :type="showPw ? 'text' : 'password'" required
                  class="w-full bg-slate-50 dark:bg-white/5 border border-slate-200 dark:border-white/10 rounded-2xl px-4 py-3.5 pl-11 pr-11 text-sm text-slate-900 dark:text-white placeholder-slate-400 dark:placeholder-slate-500 outline-none focus:border-[#16D5D2]/60 focus:bg-white focus:dark:bg-white/10 transition-all focus:glow-cyan-border shadow-inner dark:shadow-none"
                  placeholder="••••••••" />
                <button type="button" @click="showPw = !showPw" class="absolute right-4 top-1/2 -translate-y-1/2 text-slate-400 hover:text-slate-600 dark:text-slate-500 dark:hover:text-slate-300">
                  <component :is="showPw ? EyeOff : Eye" :size="18" />
                </button>
              </div>
            </div>

            <!-- Primary Action -->
            <button type="submit" :disabled="loading"
              class="w-full bg-gradient-to-r from-[#16D5D2] to-[#36CFFF] text-[#060B14] font-bold py-4 text-sm flex items-center justify-center gap-2 mt-6 rounded-full hover:shadow-[0_0_20px_rgba(22,213,210,0.5)] transition-all">
              <Loader2 v-if="loading" :size="18" class="animate-spin" />
              <LogIn v-else :size="18" />
              {{ loading ? 'Memproses...' : 'Masuk' }}
            </button>
            
          </form>

          <!-- Secondary Action -->
          <div class="mt-4">
            <button @click="demoLogin" :disabled="loading"
              class="w-full border border-slate-300 dark:border-white/20 text-slate-700 dark:text-white font-medium py-4 text-sm flex items-center justify-center gap-2 rounded-full hover:bg-slate-100 dark:hover:bg-white/10 transition-all">
              <Zap :size="16" class="text-[#16D5D2] dark:text-[#36CFFF]" /> Coba Demo
            </button>
          </div>
        </div>

        <p class="text-center text-sm text-slate-500 dark:text-slate-400 mt-8">
          Belum punya akun? 
          <router-link to="/register" class="text-[#16D5D2] hover:text-[#36CFFF] font-medium transition-colors">Daftar sekarang</router-link>
        </p>

      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { useRouter } from 'vue-router'
import { AlertCircle, Mail, Lock, Eye, EyeOff, Loader2, LogIn, Zap } from '@lucide/vue'
import { useAuthStore } from '@/stores/auth'
import ThemeToggle from '../components/ThemeToggle.vue'

const router = useRouter()
const authStore = useAuthStore()

const form = reactive({ email: '', password: '' })
const error = ref('')
const loading = ref(false)
const showPw = ref(false)

const handleLogin = async () => {
  error.value = ''
  loading.value = true
  try {
    const res = await auth.login(form.email, form.password)
    if (res.success) {
      router.push('/chat')
    } else {
      error.value = res.error || 'Login gagal. Periksa kembali kredensial Anda.'
    }
  } catch (err) {
    error.value = 'Terjadi kesalahan pada server. Silakan coba lagi.'
  } finally {
    loading.value = false
  }
}

const demoLogin = async () => {
  error.value = ''
  loading.value = true
  try {
    const res = await authStore.demoLogin()
    if (res.success) {
      router.push('/chat')
    } else {
      error.value = 'Gagal menggunakan akun demo.'
    }
  } catch (err) {
    error.value = 'Terjadi kesalahan jaringan.'
  } finally {
    loading.value = false
  }
}
</script>
