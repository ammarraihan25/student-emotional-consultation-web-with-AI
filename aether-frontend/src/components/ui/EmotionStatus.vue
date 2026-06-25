<template>
  <div class="glass rounded-2xl p-4.5 border border-white/8 space-y-4 shadow-lg transition-all duration-300">
    <div class="flex items-center gap-2">
      <Activity :size="15" class="text-purple-400" />
      <span class="text-xs text-white/50 font-semibold uppercase tracking-wider">Status Emosi Sesi</span>
    </div>

    <!-- Main Emotion Indicator -->
    <div class="flex flex-col items-center py-2.5">
      <!-- Animated Ring -->
      <div class="relative">
        <div :class="['w-24 h-24 rounded-full flex items-center justify-center transition-all duration-500', ringBg]">
          <div :class="['w-16 h-16 rounded-full flex items-center justify-center transition-all duration-500', innerBg, glow]">
            <span class="text-3.5xl transition-transform duration-500 hover:scale-110 select-none">{{ emoji }}</span>
          </div>
        </div>
        <svg class="absolute inset-0 w-24 h-24 -rotate-90" viewBox="0 0 96 96">
          <circle cx="48" cy="48" r="44" fill="none" stroke="rgba(255,255,255,0.03)" stroke-width="4.5" />
          <circle
            cx="48" cy="48" r="44" fill="none"
            :stroke="strokeColor" stroke-width="4.5"
            stroke-linecap="round"
            :stroke-dasharray="`${scorePercent * 2.76} 276.5`"
            class="transition-all duration-1000 ease-out"
          />
        </svg>
      </div>

      <div class="mt-4 text-center">
        <p :class="['text-lg font-black tracking-tight', labelColor]">{{ label }}</p>
        <p class="text-xs text-white/40 mt-0.5">Maks. Skor Sesi: <span class="text-white/70 font-semibold">{{ score }}</span> / 100</p>
      </div>
    </div>

    <!-- Short descriptive status helper -->
    <div class="bg-white/3 border border-white/5 rounded-xl p-3 text-[11px] leading-relaxed text-white/60 text-center">
      {{ statusDescription }}
    </div>

    <!-- Score Bar -->
    <div class="space-y-1">
      <div class="flex justify-between text-[10px] text-white/30 font-medium uppercase tracking-wider">
        <span>Aman</span>
        <span>Distress</span>
        <span>Krisis</span>
      </div>
      <div class="h-2 bg-white/5 rounded-full overflow-hidden p-0.5 border border-white/5">
        <div
          :class="['h-full rounded-full transition-all duration-1000 ease-out', barColor]"
          :style="`width: ${Math.min(scorePercent, 100)}%`"
        ></div>
      </div>
      <div class="flex justify-between text-[10px] text-white/20 font-semibold">
        <span>0</span>
        <span class="text-yellow-500/40">35</span>
        <span class="text-red-500/40">70</span>
        <span>100</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { Activity } from '@lucide/vue'

const props = defineProps({
  emotion: { type: String, default: null },
  score: { type: Number, default: 0 }
})

const scorePercent = computed(() => props.score)

const emoji = computed(() => ({ Hijau: '😌', Kuning: '😟', Merah: '🆘' }[props.emotion] || '🍃'))
const label = computed(() => ({ Hijau: 'Stabil / Normal', Kuning: 'Distress Emosional', Merah: 'Krisis' }[props.emotion] || 'Belum Terdeteksi'))
const labelColor = computed(() => ({ Hijau: 'text-emerald-400', Kuning: 'text-yellow-400', Merah: 'text-red-400' }[props.emotion] || 'text-white/40'))
const ringBg = computed(() => ({ Hijau: 'bg-emerald-500/5', Kuning: 'bg-yellow-500/5', Merah: 'bg-red-500/5' }[props.emotion] || 'bg-white/3'))
const innerBg = computed(() => ({ Hijau: 'bg-emerald-500/15', Kuning: 'bg-yellow-500/15', Merah: 'bg-red-500/15' }[props.emotion] || 'bg-white/5'))
const glow = computed(() => ({ Hijau: 'animate-pulse-glow-green', Kuning: 'animate-pulse-glow-yellow', Merah: 'animate-pulse-glow-red' }[props.emotion] || ''))
const strokeColor = computed(() => ({ Hijau: '#10b981', Kuning: '#eab308', Merah: '#ef4444' }[props.emotion] || 'rgba(255,255,255,0.08)'))
const barColor = computed(() => ({ Hijau: 'bg-gradient-to-r from-emerald-500 to-emerald-400', Kuning: 'bg-gradient-to-r from-yellow-500 to-amber-500', Merah: 'bg-gradient-to-r from-red-500 to-rose-500' }[props.emotion] || 'bg-white/10'))

const statusDescription = computed(() => {
  const map = {
    Hijau: 'Pikiranmu tenang dan berada dalam kondisi stabil. Pertahankan rutinitas positifmu! 💚',
    Kuning: 'Ada tekanan emosional sedang terdeteksi. Silakan luangkan waktu sejenak untuk rileks. 💛',
    Merah: 'Terdeteksi kondisi krisis/stres tinggi. Kami sangat menyarankan untuk menghubungi konselor terdekat. 🆘'
  }
  return map[props.emotion] || 'Tulis pesan pertamamu untuk mulai melacak indikator kesehatan emosional.'
})
</script>

