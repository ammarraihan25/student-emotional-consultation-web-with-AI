<template>
  <div class="glass rounded-2xl p-4 border border-white/8">
    <div class="flex items-center gap-2 mb-3">
      <Activity :size="15" class="text-purple-400" />
      <span class="text-xs text-white/50 font-medium uppercase tracking-wider">Status Emosi</span>
    </div>

    <!-- Main Emotion Indicator -->
    <div class="flex flex-col items-center py-4">
      <!-- Animated Ring -->
      <div class="relative">
        <div :class="['w-24 h-24 rounded-full flex items-center justify-center', ringBg]">
          <div :class="['w-16 h-16 rounded-full flex items-center justify-center', innerBg, glow]">
            <span class="text-3xl">{{ emoji }}</span>
          </div>
        </div>
        <svg class="absolute inset-0 w-24 h-24 -rotate-90" viewBox="0 0 96 96">
          <circle cx="48" cy="48" r="44" fill="none" stroke="rgba(255,255,255,0.05)" stroke-width="4" />
          <circle
            cx="48" cy="48" r="44" fill="none"
            :stroke="strokeColor" stroke-width="4"
            stroke-linecap="round"
            :stroke-dasharray="`${scorePercent * 2.76} 276.5`"
            class="transition-all duration-1000"
          />
        </svg>
      </div>

      <div class="mt-3 text-center">
        <p :class="['text-xl font-bold', labelColor]">{{ label }}</p>
        <p class="text-xs text-white/40 mt-0.5">Skor: <span class="text-white/70 font-semibold">{{ score }}</span> / 100</p>
      </div>
    </div>

    <!-- Score Bar -->
    <div class="mt-2">
      <div class="flex justify-between text-xs text-white/30 mb-1.5">
        <span>Aman</span>
        <span>Distress</span>
        <span>Krisis</span>
      </div>
      <div class="h-2 bg-white/10 rounded-full overflow-hidden">
        <div
          :class="['h-full rounded-full transition-all duration-1000', barColor]"
          :style="`width: ${Math.min(scorePercent, 100)}%`"
        ></div>
      </div>
      <div class="flex justify-between text-xs text-white/20 mt-1">
        <span>0</span>
        <span class="text-yellow-500/50">35</span>
        <span class="text-red-500/50">70</span>
        <span>100</span>
      </div>
    </div>

    <EmotionBadge :emotion="emotion" :score="score" class="mt-3 justify-center" />
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { Activity } from '@lucide/vue'
import EmotionBadge from './EmotionBadge.vue'

const props = defineProps({
  emotion: { type: String, default: null },
  score: { type: Number, default: 0 }
})

const scorePercent = computed(() => props.score)

const emoji = computed(() => ({ Hijau: '😌', Kuning: '😟', Merah: '🆘' }[props.emotion] || '🤖'))
const label = computed(() => ({ Hijau: 'Stabil', Kuning: 'Distress Emosional', Merah: 'Krisis' }[props.emotion] || 'Mendeteksi...'))
const labelColor = computed(() => ({ Hijau: 'text-emerald-400', Kuning: 'text-yellow-400', Merah: 'text-red-400' }[props.emotion] || 'text-white/50'))
const ringBg = computed(() => ({ Hijau: 'bg-emerald-500/10', Kuning: 'bg-yellow-500/10', Merah: 'bg-red-500/10' }[props.emotion] || 'bg-white/5'))
const innerBg = computed(() => ({ Hijau: 'bg-emerald-500/20', Kuning: 'bg-yellow-500/20', Merah: 'bg-red-500/20' }[props.emotion] || 'bg-white/10'))
const glow = computed(() => ({ Hijau: 'animate-pulse-glow-green', Kuning: 'animate-pulse-glow-yellow', Merah: 'animate-pulse-glow-red' }[props.emotion] || ''))
const strokeColor = computed(() => ({ Hijau: '#10b981', Kuning: '#eab308', Merah: '#ef4444' }[props.emotion] || 'rgba(255,255,255,0.1)'))
const barColor = computed(() => ({ Hijau: 'bg-gradient-to-r from-emerald-500 to-emerald-400', Kuning: 'bg-gradient-to-r from-yellow-500 to-orange-400', Merah: 'bg-gradient-to-r from-red-500 to-red-400' }[props.emotion] || 'bg-white/20'))
</script>
