<template>
  <div class="flex flex-col h-full">
    <!-- Messages area -->
    <div ref="messagesEl" class="flex-1 overflow-y-auto px-4 py-4 space-y-4 scroll-smooth">
      <MessageBubble v-for="msg in messages" :key="msg.id" :message="msg" />
      <div v-if="isTyping" class="flex flex-row gap-3">
        <div class="w-8 h-8 rounded-xl bg-gradient-to-br from-purple-700 to-indigo-800 flex items-center justify-center text-sm shrink-0 mt-1">Æ</div>
        <div class="glass border border-white/10 rounded-2xl rounded-tl-sm">
          <TypingIndicator />
        </div>
      </div>
      <div ref="bottomEl"></div>
    </div>

    <!-- NLP Processing state -->
    <div v-if="isAnalyzing" class="px-4 py-2 border-t border-white/8">
      <div class="flex items-center gap-2 text-xs text-white/40">
        <div class="flex gap-1">
          <div class="w-1 h-3 bg-purple-500 rounded-full animate-[pulse_0.8s_ease-in-out_infinite]"></div>
          <div class="w-1 h-3 bg-cyan-500 rounded-full animate-[pulse_0.8s_ease-in-out_0.2s_infinite]"></div>
          <div class="w-1 h-3 bg-emerald-500 rounded-full animate-[pulse_0.8s_ease-in-out_0.4s_infinite]"></div>
        </div>
        <span>Memproses NLP · Mendeteksi emosi · Scoring...</span>
      </div>
    </div>

    <!-- Input area -->
    <div class="p-4 border-t border-white/8">
      <div class="glass rounded-2xl border border-white/10 focus-within:border-purple-500/50 transition-all duration-300 focus-within:shadow-[0_0_20px_rgba(168,85,247,0.15)]">
        <textarea
          ref="inputEl"
          v-model="inputText"
          @keydown.enter.exact.prevent="sendMessage"
          rows="1"
          placeholder="Ceritakan apa yang kamu rasakan..."
          class="w-full bg-transparent px-4 pt-3 pb-1 text-sm text-white placeholder-white/25 resize-none outline-none max-h-32"
          style="field-sizing: content;"
        ></textarea>
        <div class="flex items-center justify-between px-4 pb-3 pt-1">
          <span class="text-xs text-white/25">{{ inputText.length }}/500 · Enter untuk kirim</span>
          <button
            @click="sendMessage"
            :disabled="!inputText.trim() || isTyping"
            :class="[
              'w-9 h-9 rounded-xl flex items-center justify-center transition-all duration-200',
              inputText.trim() && !isTyping
                ? 'btn-glow text-white hover:scale-110'
                : 'bg-white/5 text-white/25 cursor-not-allowed'
            ]"
          >
            <Send :size="16" />
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, nextTick } from 'vue'
import { Send } from '@lucide/vue'
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

function sendMessage() {
  if (!inputText.value.trim() || props.isTyping) return
  emit('send', inputText.value.trim())
  inputText.value = ''
}

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
