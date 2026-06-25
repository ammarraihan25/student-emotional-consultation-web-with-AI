<template>
  <div :class="['flex gap-3.5 animate-message-in', isUser ? 'flex-row-reverse' : 'flex-row']">
    <!-- Avatar -->
    <div class="shrink-0 mt-0.5 relative group">
      <div v-if="isUser"
        class="w-9 h-9 rounded-xl bg-gradient-to-br from-purple-500 to-cyan-400 flex items-center justify-center text-xs font-bold text-white shadow-[0_3px_10px_rgba(168,85,247,0.25)]"
      >
        {{ userInitial }}
      </div>
      <div v-else 
        :class="[
          'w-9 h-9 rounded-xl flex items-center justify-center text-sm font-black text-white transition-all duration-500 select-none',
          avatarGlow
        ]"
      >
        Æ
        <!-- Pulsing avatar halo for AI status -->
        <span class="absolute -bottom-0.5 -right-0.5 w-2.5 h-2.5 rounded-full border border-slate-50 dark:border-[#050b18] bg-emerald-400"></span>
      </div>
    </div>

    <!-- Bubble + Meta -->
    <div :class="['flex flex-col max-w-[80%] sm:max-w-[72%]', isUser ? 'items-end' : 'items-start']">
      <!-- Bubble -->
      <div
        :class="[
          'px-4 py-3 rounded-2xl text-sm leading-relaxed whitespace-pre-wrap transition-all duration-500 shadow-sm',
          isUser
            ? 'bg-gradient-to-br from-purple-600 to-indigo-600 text-white rounded-tr-sm'
            : ['glass bg-white dark:bg-transparent border border-slate-200 dark:border-white/10 text-slate-800 dark:text-white/95 rounded-tl-sm shadow-sm dark:shadow-none', emotionBorderClass]
        ]"
      >
        <div v-html="formattedContent" class="markdown-body"></div>
      </div>

      <!-- Meta row -->
      <div :class="['flex items-center gap-2.5 mt-2', isUser ? 'flex-row-reverse' : 'flex-row']">
        <span class="text-[10px] text-slate-400 dark:text-white/25 font-medium">{{ timeStr }}</span>
        <EmotionBadge v-if="!isUser && message.emotion" :emotion="message.emotion" :score="message.score" :animated="true" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import EmotionBadge from '@/components/ui/EmotionBadge.vue'
import { useAuthStore } from '@/stores/auth'

const props = defineProps({
  message: { type: Object, required: true }
})

const auth = useAuthStore()
const isUser = computed(() => props.message.role === 'user')
const userInitial = computed(() => auth.user?.name?.charAt(0).toUpperCase() || 'U')

const timeStr = computed(() => {
  const d = new Date(props.message.timestamp)
  return d.toLocaleTimeString('id-ID', { hour: '2-digit', minute: '2-digit' })
})

const emotionBorderClass = computed(() => {
  if (isUser.value || !props.message.emotion) return ''
  const map = {
    Hijau: 'emotion-border-hijau border-l-4',
    Kuning: 'emotion-border-kuning border-l-4',
    Merah: 'emotion-border-merah border-l-4'
  }
  return map[props.message.emotion] || ''
})

const avatarGlow = computed(() => {
  if (isUser.value) return ''
  const map = {
    Hijau: 'bg-gradient-to-br from-emerald-500/80 to-teal-600/80 shadow-[0_0_12px_rgba(16,185,129,0.35)]',
    Kuning: 'bg-gradient-to-br from-yellow-500/80 to-amber-600/80 shadow-[0_0_12px_rgba(234,179,8,0.35)]',
    Merah: 'bg-gradient-to-br from-red-500/80 to-rose-600/80 shadow-[0_0_12px_rgba(239,68,68,0.45)]'
  }
  return map[props.message.emotion] || 'bg-gradient-to-br from-purple-600 to-indigo-700 shadow-[0_0_10px_rgba(124,58,237,0.3)]'
})

// Safe basic markdown bold/italic parser to improve AI layout formatting
const formattedContent = computed(() => {
  let text = props.message.content
  if (!text) return ''
  // Escape HTML tags to prevent XSS
  text = text
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
  // Parse bold (**text**)
  text = text.replace(/\*\*(.*?)\*\*/g, '<strong class="font-bold text-slate-900 dark:text-white">$1</strong>')
  // Parse italic (*text*)
  text = text.replace(/\*(.*?)\*/g, '<em class="italic text-slate-800 dark:text-white/90">$1</em>')
  return text
})
</script>

<style>
.markdown-body strong {
  font-weight: 700;
}
.markdown-body em {
  font-style: italic;
}
</style>

