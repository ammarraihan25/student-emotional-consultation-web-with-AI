<template>
  <div class="flex flex-col h-full bg-slate-50 dark:bg-[#050b18]/60 relative transition-colors">
    
    <!-- Messages area -->
    <div ref="messagesEl" class="flex-1 overflow-y-auto px-4 md:px-6 py-6 space-y-6 scroll-smooth">
      
      <!-- Welcome Dashboard (Only shown if messages contain only the welcome message) -->
      <div v-if="messages.length <= 1" class="max-w-2xl mx-auto py-4 space-y-8 animate-fade-in">
        <!-- Calming greeting -->
        <div class="text-center space-y-3">
          <div class="w-16 h-16 rounded-3xl bg-gradient-to-br from-purple-500/10 to-cyan-500/10 dark:from-purple-500/20 dark:to-cyan-500/20 border border-purple-500/20 dark:border-purple-500/30 flex items-center justify-center mx-auto shadow-sm dark:shadow-[0_0_20px_rgba(168,85,247,0.15)]">
            <Brain class="text-purple-500 dark:text-purple-400 w-8 h-8 animate-float" />
          </div>
          <h2 class="text-2xl font-bold text-slate-900 dark:text-white tracking-tight">Halo, Selamat Datang 🍃</h2>
          <p class="text-sm text-slate-600 dark:text-white/60 max-w-md mx-auto leading-relaxed">
            Aku Aether, konselor sebaya AI-mu. Ceritakan apa saja yang mengganjal di pikiranmu hari ini secara santai dan aman.
          </p>
        </div>

        <!-- Guided Breathing Widget -->
        <div class="glass rounded-2xl p-5 border border-slate-200 dark:border-white/8 bg-white/80 dark:bg-transparent shadow-sm dark:shadow-none relative overflow-hidden transition-all duration-500">
          <div class="flex items-center justify-between mb-4">
            <div class="flex items-center gap-2">
              <Wind class="text-cyan-500 dark:text-cyan-400 w-5 h-5 animate-pulse" />
              <span class="text-xs font-semibold text-slate-600 dark:text-white/80 uppercase tracking-wider">Latihan Pernapasan Calming</span>
            </div>
            <button 
              @click="toggleBreathing" 
              class="text-xs font-medium px-3 py-1.5 rounded-xl border border-cyan-500/30 text-cyan-400 hover:bg-cyan-500/10 transition-all flex items-center gap-1.5"
            >
              <component :is="isBreathing ? Square : Play" :size="12" />
              {{ isBreathing ? 'Hentikan' : 'Mulai Latihan' }}
            </button>
          </div>

          <div class="flex flex-col items-center justify-center py-6 min-h-[140px] relative">
            <div v-if="!isBreathing" class="text-center space-y-2">
              <p class="text-xs text-slate-500 dark:text-white/50 max-w-sm">
                Merasa stres atau tegang? Lakukan latihan pernapasan dalam 12 detik (4s Tarik, 4s Tahan, 4s Hembuskan) untuk menenangkan sarafmu.
              </p>
            </div>
            <div v-else class="flex flex-col items-center justify-center space-y-4">
              <!-- Calming circles -->
              <div class="relative w-24 h-24 flex items-center justify-center">
                <!-- Glowing breathing circle -->
                <div class="absolute w-20 h-20 rounded-full border-2 border-cyan-500/40 bg-cyan-500/5 animate-breathe flex items-center justify-center">
                  <div class="w-10 h-10 rounded-full bg-cyan-500/20 blur-sm"></div>
                </div>
                <span class="text-sm font-black text-slate-900 dark:text-white z-10 select-none">{{ 12 - breathingSeconds }}s</span>
              </div>
              <div class="text-center">
                <p class="text-sm font-bold text-cyan-500 dark:text-cyan-400 tracking-wide transition-all uppercase">{{ breathingPhase }}</p>
                <p class="text-[10px] text-slate-500 dark:text-white/40 mt-0.5">Ikuti ritme kembang kempis lingkaran di atas</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Quick Mood Selection -->
        <div class="space-y-3">
          <p class="text-xs font-semibold text-slate-500 dark:text-white/50 uppercase tracking-wider">Bagaimana perasaanmu saat ini?</p>
          <div class="grid grid-cols-2 sm:grid-cols-5 gap-2.5">
            <button 
              v-for="mood in moods" 
              :key="mood.label"
              @click="selectMood(mood)"
              class="glass bg-white dark:bg-transparent hover:bg-slate-50 dark:hover:bg-white/10 border border-slate-200 dark:border-white/5 hover:border-slate-300 dark:hover:border-white/20 rounded-xl p-3 text-center transition-all duration-300 flex flex-col items-center gap-1.5 group hover:-translate-y-0.5 cursor-pointer shadow-sm dark:shadow-none"
            >
              <span class="text-2xl group-hover:scale-110 transition-transform">{{ mood.emojiChar || mood.emoji }}</span>
              <span class="text-[11px] font-medium text-slate-700 dark:text-white/70">{{ mood.label }}</span>
            </button>
          </div>
        </div>

        <!-- Suggestion prompts -->
        <div class="space-y-3">
          <p class="text-xs font-semibold text-slate-500 dark:text-white/50 uppercase tracking-wider">Pertanyaan atau keluhan populer:</p>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
            <button 
              v-for="s in suggestions" 
              :key="s"
              @click="$emit('send', s)"
              class="glass bg-white dark:bg-transparent text-left border border-slate-200 dark:border-white/5 hover:border-purple-500/40 hover:bg-purple-50 dark:hover:bg-purple-500/5 rounded-xl p-3.5 text-xs text-slate-700 dark:text-white/70 hover:text-slate-900 dark:hover:text-white transition-all duration-300 flex items-center justify-between group cursor-pointer shadow-sm dark:shadow-none"
            >
              <span class="leading-relaxed pr-2">{{ s }}</span>
              <ArrowRight :size="14" class="text-slate-400 dark:text-white/20 group-hover:text-purple-500 dark:group-hover:text-purple-400 shrink-0 group-hover:translate-x-1 transition-all" />
            </button>
          </div>
        </div>
      </div>

      <!-- Real message list -->
      <template v-else>
        <MessageBubble v-for="msg in messages" :key="msg.id" :message="msg" />
      </template>

      <!-- Typing state -->
      <div v-if="isTyping" class="flex flex-row gap-3 animate-message-in">
        <div class="w-8 h-8 rounded-xl bg-gradient-to-br from-purple-600 to-indigo-700 dark:from-purple-700 dark:to-indigo-800 flex items-center justify-center text-sm shrink-0 mt-1 shadow-sm dark:shadow-[0_0_10px_rgba(124,58,237,0.3)] text-white">Æ</div>
        <div class="glass bg-white dark:bg-transparent border border-slate-200 dark:border-white/10 rounded-2xl rounded-tl-sm px-4 py-3 shadow-sm dark:shadow-none">
          <TypingIndicator />
        </div>
      </div>
      <div ref="bottomEl"></div>
    </div>

    <!-- NLP Processing state -->
    <div v-if="isAnalyzing" class="px-6 py-2.5 border-t border-slate-200 dark:border-white/5 bg-slate-100 dark:bg-[#050b18]/40 transition-colors">
      <div class="flex items-center gap-2.5 text-xs text-slate-500 dark:text-white/40">
        <div class="flex gap-1.5 items-center">
          <span class="w-1.5 h-1.5 bg-purple-500 rounded-full animate-ping"></span>
          <span class="w-1.5 h-1.5 bg-cyan-500 rounded-full animate-ping [animation-delay:0.2s]"></span>
          <span class="w-1.5 h-1.5 bg-emerald-500 rounded-full animate-ping [animation-delay:0.4s]"></span>
        </div>
        <span class="font-medium">Memproses input NLP & Deteksi Emosi...</span>
      </div>
    </div>

    <!-- Input area -->
    <div class="p-4 md:p-6 border-t border-slate-200 dark:border-white/5 bg-white/90 dark:bg-[#050b18]/80 backdrop-blur-md transition-colors">
      <div class="max-w-3xl mx-auto glass bg-slate-50 dark:bg-transparent rounded-3xl border border-slate-200 dark:border-white/8 focus-within:border-purple-500/50 transition-all duration-300 focus-within:shadow-[0_0_20px_rgba(168,85,247,0.1)] dark:focus-within:shadow-[0_0_30px_rgba(168,85,247,0.15)] flex flex-col p-1.5">
        <div class="flex items-start px-2">
          <!-- Small decorative AI icon inside input -->
          <Sparkles class="text-slate-400 dark:text-white/20 w-4 h-4 mt-3 ml-2 shrink-0" />
          <textarea
            ref="inputEl"
            v-model="inputText"
            @keydown.enter.exact.prevent="sendMessage"
            rows="1"
            placeholder="Tulis apa yang kamu rasakan, Aether siap dengerin..."
            class="w-full bg-transparent px-3 py-2.5 text-sm text-slate-900 dark:text-white placeholder-slate-400 dark:placeholder-white/30 resize-none outline-none max-h-32 leading-relaxed"
            style="field-sizing: content;"
          ></textarea>
        </div>
        <div class="flex items-center justify-between px-3 pb-2 pt-1 border-t border-slate-200 dark:border-white/5">
          <span class="text-[10px] text-slate-400 dark:text-white/30 font-medium ml-2">{{ inputText.length }}/500 · Enter untuk kirim</span>
          <button
            @click="sendMessage"
            :disabled="!inputText.trim() || isTyping"
            :class="[
              'w-8 h-8 rounded-xl flex items-center justify-center transition-all duration-300',
              inputText.trim() && !isTyping
                ? 'btn-glow bg-purple-500 text-white hover:scale-105 hover:shadow-[0_0_15px_rgba(124,58,237,0.6)] cursor-pointer'
                : 'bg-slate-200 dark:bg-white/5 text-slate-400 dark:text-white/20 cursor-not-allowed'
            ]"
          >
            <Send :size="14" />
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, nextTick, onUnmounted } from 'vue'
import { Send, Brain, Sparkles, Wind, Play, Square, ArrowRight } from '@lucide/vue'
import MessageBubble from './MessageBubble.vue'
import TypingIndicator from './TypingIndicator.vue'

const props = defineProps({
  messages: { type: Array, default: () => [] },
  isTyping: { type: Boolean, default: false },
  isAnalyzing: { type: Boolean, default: false }
})
const emit = defineEmits(['send'])

const inputText = ref('')
const messagesEl = ref(null)
const bottomEl = ref(null)
const inputEl = ref(null)

// Breathing Widget state
const isBreathing = ref(false)
const breathingSeconds = ref(0)
const breathingPhase = ref('Tarik Napas')
let breathingInterval = null

const moods = [
  { emojiChar: '😰', label: 'Cemas', prompt: 'Aku sedang merasa cemas akhir-akhir ini karena ' },
  { emojiChar: '😴', label: 'Burnout', prompt: 'Aku merasa lelah dan burnout dengan ' },
  { emojiChar: '😢', label: 'Sedih', prompt: 'Aku merasa agak sedih dan butuh teman bicara mengenai ' },
  { emojiChar: '😡', label: 'Marah', prompt: 'Aku merasa kesal dan emosi tentang ' },
  { emojiChar: '😊', label: 'Baik', prompt: 'Hari ini suasana hatiku sedang baik, tapi aku ingin cerita tentang ' }
]

const suggestions = [
  'Tugas kuliah menumpuk dan aku mulai merasa kewalahan.',
  'Aku susah berkonsentrasi karena terlalu banyak pikiran negatif.',
  'Bagaimana cara mengatasi kecemasan saat presentasi di depan kelas?',
  'Ingin bercerita tentang perasaanku hari ini secara acak.'
]

function sendMessage() {
  if (!inputText.value.trim() || props.isTyping) return
  emit('send', inputText.value.trim())
  inputText.value = ''
}

function selectMood(mood) {
  inputText.value = mood.prompt
  nextTick(() => {
    inputEl.value?.focus()
  })
}

function toggleBreathing() {
  if (isBreathing.value) {
    stopBreathing()
  } else {
    startBreathing()
  }
}

function startBreathing() {
  isBreathing.value = true
  breathingSeconds.value = 0
  breathingPhase.value = 'Tarik Napas'
  
  breathingInterval = setInterval(() => {
    breathingSeconds.value = (breathingSeconds.value + 1) % 12
    if (breathingSeconds.value < 4) {
      breathingPhase.value = 'Tarik Napas'
    } else if (breathingSeconds.value < 8) {
      breathingPhase.value = 'Tahan Napas'
    } else {
      breathingPhase.value = 'Hembuskan'
    }
  }, 1000)
}

function stopBreathing() {
  isBreathing.value = false
  if (breathingInterval) {
    clearInterval(breathingInterval)
    breathingInterval = null
  }
}

onUnmounted(() => {
  stopBreathing()
})

watch(() => props.messages.length, async () => {
  await nextTick()
  bottomEl.value?.scrollIntoView({ behavior: 'smooth' })
})

watch(() => props.isTyping, async (val) => {
  if (val) {
    await nextTick()
    bottomEl.value?.scrollIntoView({ behavior: 'smooth' })
  }
})
</script>

