<template>
  <div :class="['flex gap-3 animate-message-in', isUser ? 'flex-row-reverse' : 'flex-row']">
    <!-- Avatar -->
    <div class="shrink-0 mt-1">
      <div v-if="isUser"
        class="w-8 h-8 rounded-xl bg-gradient-to-br from-purple-600 to-cyan-500 flex items-center justify-center text-xs font-bold text-white"
      >{{ userInitial }}</div>
      <div v-else class="w-8 h-8 rounded-xl bg-gradient-to-br from-purple-700 to-indigo-800 flex items-center justify-center text-sm">
        Æ
      </div>
    </div>

    <!-- Bubble + Meta -->
    <div :class="['flex flex-col max-w-[75%]', isUser ? 'items-end' : 'items-start']">
      <!-- Bubble -->
      <div
        :class="[
          'px-4 py-3 rounded-2xl text-sm leading-relaxed whitespace-pre-wrap',
          isUser
            ? 'bg-gradient-to-br from-purple-600 to-purple-700 text-white rounded-tr-sm'
            : 'glass border border-white/10 text-white/90 rounded-tl-sm'
        ]"
      >
        {{ message.content }}
      </div>

      <!-- Meta row -->
      <div :class="['flex items-center gap-2 mt-1.5', isUser ? 'flex-row-reverse' : 'flex-row']">
        <span class="text-xs text-white/25">{{ timeStr }}</span>
        <EmotionBadge v-if="!isUser && message.emotion" :emotion="message.emotion" :score="message.score" :animated="false" />
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
</script>
