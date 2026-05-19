<template>
  <div class="min-h-screen bg-[#050b18] flex">
    <!-- Sidebar -->
    <Sidebar
      :sessions="chatStore.sessions"
      :mobile-open="mobileSidebarOpen"
      :show-history="true"
      @new-chat="chatStore.newSession()"
      @select-session="chatStore.selectSession($event)"
      @logout="handleLogout"
      @close-mobile="mobileSidebarOpen = false"
    />

    <!-- Main area -->
    <div class="flex-1 flex flex-col md:ml-64 transition-all duration-300 min-h-screen">
      <!-- Top bar (mobile) -->
      <div class="md:hidden flex items-center gap-3 px-4 py-3 border-b border-white/8 glass">
        <button @click="mobileSidebarOpen = true" class="p-2 rounded-lg text-white/60 hover:text-white hover:bg-white/10 transition-all">
          <Menu :size="20" />
        </button>
        <span class="font-semibold text-white/90 text-sm">Aether Chat</span>
        <EmotionBadge :emotion="chatStore.sessionEmotion" :score="chatStore.sessionScore" class="ml-auto" />
      </div>

      <!-- Chat + panels layout -->
      <div class="flex flex-1 overflow-hidden">
        <!-- Chat area -->
        <div class="flex-1 flex flex-col min-h-0">
          <!-- Header -->
          <div class="hidden md:flex items-center justify-between px-6 py-4 border-b border-white/8">
            <div>
              <h1 class="font-bold text-white text-lg">Chat dengan Aether</h1>
              <p class="text-xs text-white/40">AI Mental Health Companion · Sesi aktif</p>
            </div>
            <div class="flex items-center gap-3">
              <div class="flex items-center gap-2 glass rounded-xl px-3 py-1.5 border border-white/10">
                <div class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></div>
                <span class="text-xs text-white/60">AI Online</span>
              </div>
              <EmotionBadge :emotion="chatStore.sessionEmotion" :score="chatStore.sessionScore" />
            </div>
          </div>

          <!-- ChatWindow -->
          <div class="flex-1 min-h-0">
            <ChatWindow
              :messages="chatStore.messages"
              :is-typing="chatStore.isTyping"
              :is-analyzing="chatStore.isAnalyzing"
              @send="chatStore.sendMessage($event)"
            />
          </div>
        </div>

        <!-- Right Panel (desktop) -->
        <div class="hidden lg:flex flex-col w-72 border-l border-white/8 p-4 gap-4 overflow-y-auto">
          <EmotionStatus :emotion="chatStore.sessionEmotion" :score="chatStore.sessionScore" />
          <AnalyticsPanel :emotion="chatStore.currentEmotion" :score="chatStore.currentScore" :details="chatStore.currentDetails" />

          <!-- Quick tips -->
          <div class="glass rounded-2xl p-4 border border-white/8">
            <p class="text-xs text-white/40 mb-3 font-medium uppercase tracking-wider">Tips Hari Ini</p>
            <div class="text-xs text-white/60 leading-relaxed italic">
              "{{ dailyTip }}"
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Emergency Modal -->
    <EmergencyModal :show="chatStore.showEmergencyModal" @close="chatStore.showEmergencyModal = false" />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { Menu } from '@lucide/vue'
import { useChatStore } from '@/stores/chat'
import { useAuthStore } from '@/stores/auth'
import Sidebar from '@/components/layout/Sidebar.vue'
import ChatWindow from '@/components/chat/ChatWindow.vue'
import EmotionStatus from '@/components/ui/EmotionStatus.vue'
import EmotionBadge from '@/components/ui/EmotionBadge.vue'
import AnalyticsPanel from '@/components/chat/AnalyticsPanel.vue'
import EmergencyModal from '@/components/modals/EmergencyModal.vue'

const chatStore = useChatStore()
const authStore = useAuthStore()
const router = useRouter()
const mobileSidebarOpen = ref(false)

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
