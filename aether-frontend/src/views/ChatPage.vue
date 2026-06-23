<template>
  <div class="min-h-screen bg-slate-50 dark:bg-[#020817] flex font-sans overflow-hidden text-slate-900 dark:text-slate-100 relative transition-colors duration-300">
    
    <!-- Background Elements -->
    <div class="fixed inset-0 pointer-events-none z-0">
      <div class="absolute top-[-20%] left-[20%] w-[500px] h-[500px] bg-[#16D5D2]/5 blur-[120px] rounded-full animate-float-slow"></div>
      <div class="absolute bottom-[-10%] right-[10%] w-[400px] h-[400px] bg-[#8B5CF6]/5 blur-[100px] rounded-full animate-float"></div>
      <!-- Tiny stars -->
      <div class="absolute top-[20%] left-[10%] w-1 h-1 bg-white rounded-full animate-pulse"></div>
      <div class="absolute top-[80%] left-[80%] w-1.5 h-1.5 bg-[#36CFFF] rounded-full animate-pulse" style="animation-delay: 1.5s"></div>
    </div>

    <!-- LEFT SIDEBAR -->
    <aside class="hidden lg:flex flex-col w-72 h-screen p-6 relative z-10 border-r border-slate-200 dark:border-white/5 bg-slate-100/90 dark:bg-[#0A172B]/50 backdrop-blur-3xl transition-colors">
      <!-- Logo and Theme Toggle -->
      <div class="flex items-center justify-between mb-12 px-2">
        <router-link to="/" class="flex items-center group">
          <span class="font-sans font-bold tracking-wide text-2xl text-slate-900 dark:text-white transition-colors">Aether</span>
        </router-link>
        <ThemeToggle />
      </div>

      <!-- Nav Items -->
      <nav class="flex-1 space-y-2">
        <button @click="chatStore.newSession()" class="w-full flex items-center justify-center gap-3 px-4 py-3.5 rounded-full bg-gradient-to-r from-[#16D5D2] to-[#36CFFF] text-[#060B14] font-bold shadow-[0_0_15px_rgba(22,213,210,0.3)] hover:shadow-[0_0_25px_rgba(22,213,210,0.5)] transition-all mb-6">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 5v14M5 12h14"/></svg>
          New Session
        </button>

        <div class="px-4 py-3 rounded-2xl text-slate-900 dark:text-white bg-slate-200 dark:bg-white/5 font-medium flex items-center gap-3 cursor-pointer">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="text-[#16D5D2] dark:text-[#36CFFF]"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg> Chat
        </div>
        <div class="px-4 py-3 rounded-2xl text-slate-600 dark:text-slate-400 hover:text-slate-900 hover:dark:text-white hover:bg-slate-200 dark:hover:bg-white/5 transition-colors font-medium flex items-center gap-3 cursor-pointer">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="text-[#8B5CF6]"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg> Mood Journal
        </div>
        <div class="px-4 py-3 rounded-2xl text-slate-600 dark:text-slate-400 hover:text-slate-900 hover:dark:text-white hover:bg-slate-200 dark:hover:bg-white/5 transition-colors font-medium flex items-center gap-3 cursor-pointer">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="text-[#4ADE80]"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/></svg> Resource Center
        </div>
        
        <div class="pt-6 mt-6 border-t border-slate-200 dark:border-white/5">
          <p class="px-4 text-xs font-semibold text-slate-500 uppercase tracking-wider mb-2">History</p>
          <div class="space-y-1">
            <div v-for="session in chatStore.sessions.slice(0,4)" :key="session.id" @click="chatStore.selectSession(session.id)" class="px-4 py-2 rounded-xl text-sm text-slate-600 dark:text-slate-400 hover:text-slate-900 hover:dark:text-white hover:bg-slate-200 dark:hover:bg-white/5 cursor-pointer truncate">
              {{ session.title || 'Sesi Konseling' }}
            </div>
          </div>
        </div>
      </nav>

      <!-- Profile / Logout -->
      <div class="mt-auto pt-4 border-t border-slate-200 dark:border-white/5">
        <button @click="handleLogout" class="w-full px-4 py-3 rounded-2xl text-slate-600 dark:text-slate-400 hover:text-red-600 dark:hover:text-red-400 hover:bg-red-100 dark:hover:bg-red-500/10 transition-colors flex items-center gap-3 font-medium">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 21H5a2 2 0 01-2-2V5a2 2 0 012-2h4M16 17l5-5-5-5M21 12H9"/></svg>
          Keluar
        </button>
      </div>
    </aside>

    <!-- CENTER CONVERSATION AREA -->
    <main class="flex-1 flex flex-col h-screen relative z-10">
      
      <div class="lg:hidden flex items-center justify-between p-4 glass-panel rounded-none border-t-0 border-x-0 border-b border-slate-200 dark:border-white/5 bg-white dark:bg-[#0A172B]/50">
        <button @click="mobileSidebarOpen = true" class="p-2 text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white">
          <Menu :size="24" />
        </button>
        <div class="font-sans font-bold text-xl text-slate-900 dark:text-white">Aether</div>
        <ThemeToggle />
      </div>

      <!-- Top Greeting -->
      <div class="py-4 px-6 md:px-10 flex items-center justify-center gap-4 border-b border-slate-200 dark:border-white/5 bg-white/80 dark:bg-[#060B14]/80 z-20 shadow-sm backdrop-blur-md">
        <img src="/images/aether4.png" alt="Aether Mascot" class="w-12 h-12 animate-float drop-shadow-[0_0_15px_rgba(22,213,210,0.3)]" />
        <div class="text-left">
          <h2 class="text-lg font-serif font-bold text-slate-900 dark:text-white leading-tight">Halo, aku Aether</h2>
          <p class="text-slate-500 dark:text-slate-400 text-xs mt-0.5">Tempat aman untuk berbicara dan memahami perasaanmu.</p>
        </div>
      </div>

      <!-- Messages Area -->
      <div class="flex-1 overflow-y-auto p-6 md:p-10 space-y-6 scrollbar-hide">
        <!-- Reusing existing ChatWindow logic but applying global CSS classes -->
        <ChatWindow
          :messages="chatStore.displayedMessages"
          :is-typing="chatStore.isTyping"
          :is-analyzing="chatStore.isAnalyzing"
          @send="chatStore.sendMessage($event)"
        />
      </div>

    </main>

    <!-- RIGHT PANEL (Dashboard) -->
    <aside class="hidden xl:flex flex-col w-80 h-screen p-6 relative z-10 border-l border-slate-200 dark:border-white/5 bg-slate-100/90 dark:bg-[#0A172B]/50 backdrop-blur-3xl overflow-y-auto scrollbar-hide transition-colors">
      <h3 class="text-xs font-bold tracking-widest text-slate-500 dark:text-slate-400 uppercase mb-6 text-center">Emotional State</h3>
      
      <!-- Dominant Emotion -->
      <div class="glass-panel p-6 mb-8 text-center relative overflow-hidden border-slate-200 dark:border-[#16D5D2]/20 bg-white/80 dark:bg-transparent shadow-sm dark:shadow-none">
        <div class="absolute inset-0 bg-gradient-to-b from-[#16D5D2]/5 dark:from-[#16D5D2]/10 to-transparent"></div>
        <div class="relative z-10">
          <p class="text-[10px] text-slate-500 dark:text-slate-400 uppercase tracking-widest mb-2 font-bold">Emosi Dominan</p>
          <h4 class="text-4xl font-serif italic text-slate-900 dark:text-white mb-2">Tenang</h4>
          <p class="text-xs text-[#16D5D2] font-medium">Kondisi mental optimal.</p>
        </div>
      </div>

      <!-- Emotional Spectrum (Bar) -->
      <div class="mb-10 px-2">
        <div class="flex justify-between text-xs font-semibold text-slate-500 dark:text-slate-400 mb-3 uppercase tracking-wider">
          <span>Stres</span>
          <span>Rileks</span>
        </div>
        <div class="h-2 w-full bg-slate-200 dark:bg-white/5 rounded-full overflow-hidden">
          <div class="h-full w-[80%] bg-gradient-to-r from-[#8B5CF6] to-[#16D5D2] rounded-full shadow-[0_0_10px_#16D5D2]"></div>
        </div>
      </div>

      <!-- Coping Mechanisms -->
      <h3 class="text-xs font-bold tracking-widest text-slate-500 dark:text-slate-400 uppercase mb-4 text-center">Rekomendasi Coping</h3>
      <div class="space-y-3 mb-8">
        <div class="p-4 rounded-2xl bg-white dark:bg-white/5 border border-slate-200 dark:border-white/5 flex items-start gap-4 hover:bg-slate-50 dark:hover:bg-white/10 transition-colors cursor-pointer shadow-sm dark:shadow-none">
          <div class="w-10 h-10 rounded-full bg-[#16D5D2]/10 border border-[#16D5D2]/30 flex items-center justify-center flex-shrink-0 text-[#16D5D2]">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10z"/><path d="M12 8v4"/><path d="M12 16h.01"/></svg>
          </div>
          <div>
            <h5 class="text-sm font-bold text-slate-900 dark:text-white">Latihan Napas 4-7-8</h5>
            <p class="text-xs text-slate-500 dark:text-slate-400 mt-1 leading-relaxed">Bantu menjaga ritme ketenangan pikiran.</p>
          </div>
        </div>
        <div class="p-4 rounded-2xl bg-white dark:bg-white/5 border border-slate-200 dark:border-white/5 flex items-start gap-4 hover:bg-slate-50 dark:hover:bg-white/10 transition-colors cursor-pointer shadow-sm dark:shadow-none">
          <div class="w-10 h-10 rounded-full bg-[#8B5CF6]/10 border border-[#8B5CF6]/30 flex items-center justify-center flex-shrink-0 text-[#8B5CF6]">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.59 13.41l-7.17 7.17a2 2 0 01-2.83 0L2 12V2h10l8.59 8.59a2 2 0 010 2.82z"/><line x1="7" y1="7" x2="7.01" y2="7"/></svg>
          </div>
          <div>
            <h5 class="text-sm font-bold text-slate-900 dark:text-white">Jurnal Afirmasi</h5>
            <p class="text-xs text-slate-500 dark:text-slate-400 mt-1 leading-relaxed">Pertahankan energi positif hari ini.</p>
          </div>
        </div>
      </div>

      <!-- Quick Tips -->
      <div class="glass-panel p-5 mt-auto bg-white/80 dark:bg-transparent border-slate-200 dark:border-white/5 shadow-sm dark:shadow-none">
        <p class="text-xs text-[#16D5D2] font-semibold uppercase tracking-wider mb-3">Insight Harian</p>
        <p class="text-sm text-slate-600 dark:text-slate-300 leading-relaxed italic">
          "{{ dailyTip }}"
        </p>
      </div>
    </aside>

    <!-- Mobile Sidebar overlay (hidden normally) -->
    <div v-if="mobileSidebarOpen" class="fixed inset-0 bg-[#020817]/80 backdrop-blur-sm z-40 lg:hidden" @click="mobileSidebarOpen = false"></div>
    <aside v-if="mobileSidebarOpen" class="fixed top-0 left-0 bottom-0 w-72 bg-[#0A172B] border-r border-white/5 z-50 p-6 flex flex-col lg:hidden">
      <!-- Similar content to Desktop sidebar -->
      <div class="flex justify-between items-center mb-10">
        <span class="font-bold text-2xl text-white font-sans">Aether</span>
        <button @click="mobileSidebarOpen = false" class="text-slate-400"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6L6 18M6 6l12 12"/></svg></button>
      </div>
      <button @click="chatStore.newSession(); mobileSidebarOpen = false" class="w-full flex items-center gap-3 px-4 py-3 rounded-2xl bg-[#16D5D2]/10 text-[#16D5D2] font-medium border border-[#16D5D2]/20 mb-4">
        New Session
      </button>
      <div class="flex-1 space-y-2 text-slate-400 font-medium">
        <div class="px-4 py-3 rounded-2xl hover:text-white hover:bg-white/5 cursor-pointer">💬 Chat</div>
        <div class="px-4 py-3 rounded-2xl hover:text-white hover:bg-white/5 cursor-pointer">📖 Mood Journal</div>
      </div>
      <button @click="handleLogout" class="mt-auto w-full px-4 py-3 rounded-2xl text-slate-400 hover:text-red-400 hover:bg-red-500/10 flex items-center gap-3 font-medium">
        Keluar
      </button>
    </aside>

    <!-- Emergency Modal -->
    <EmergencyModal :show="chatStore.showEmergencyModal" @close="chatStore.showEmergencyModal = false" />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { Menu } from '@lucide/vue'
import { useChatStore } from '@/stores/chat'
import { useAuthStore } from '@/stores/auth'
import ChatWindow from '@/components/chat/ChatWindow.vue'
import EmergencyModal from '@/components/modals/EmergencyModal.vue'
import ThemeToggle from '../components/ThemeToggle.vue'

const chatStore = useChatStore()
const authStore = useAuthStore()
const router = useRouter()
const mobileSidebarOpen = ref(false)

onMounted(() => {
  chatStore.loadHistory()
})

const tips = [
  'Istirahat 5 menit setiap jam bisa mencegah burnout akademik.',
  'Menulis jurnal harian membantu mengenali pola emosi negatif.',
  'Berbicara dengan orang terpercaya lebih efektif dari memendam sendiri.',
  'Tidur 7-8 jam sangat berpengaruh pada regulasi emosi.',
]
const dailyTip = tips[new Date().getDay() % tips.length]

function handleLogout() {
  authStore.logout()
  router.push('/')
}
</script>
