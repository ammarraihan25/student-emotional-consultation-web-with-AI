<template>
  <span
    :class="[
      'inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-semibold',
      'border transition-all duration-300',
      config.bg, config.border, config.text,
      animated ? config.glow : ''
    ]"
  >
    <span :class="['w-2 h-2 rounded-full', config.dot, animated ? 'animate-pulse' : '']"></span>
    {{ config.label }}
    <span v-if="score !== null" class="opacity-70 font-normal">({{ score }})</span>
  </span>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  emotion: { type: String, default: null }, // 'Hijau' | 'Kuning' | 'Merah' | null
  score: { type: Number, default: null },
  animated: { type: Boolean, default: true }
})

const config = computed(() => {
  const map = {
    Hijau: {
      label: 'Stabil',
      bg: 'bg-emerald-500/15',
      border: 'border-emerald-500/40',
      text: 'text-emerald-400',
      dot: 'bg-emerald-400',
      glow: 'animate-pulse-glow-green'
    },
    Kuning: {
      label: 'Distress Emosional',
      bg: 'bg-yellow-500/15',
      border: 'border-yellow-500/40',
      text: 'text-yellow-400',
      dot: 'bg-yellow-400',
      glow: 'animate-pulse-glow-yellow'
    },
    Merah: {
      label: 'Krisis',
      bg: 'bg-red-500/15',
      border: 'border-red-500/40',
      text: 'text-red-400',
      dot: 'bg-red-400',
      glow: 'animate-pulse-glow-red'
    }
  }
  return map[props.emotion] || {
    label: 'Belum terdeteksi',
    bg: 'bg-white/5',
    border: 'border-white/15',
    text: 'text-white/50',
    dot: 'bg-white/30',
    glow: ''
  }
})
</script>
