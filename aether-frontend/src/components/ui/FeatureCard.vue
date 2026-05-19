<template>
  <div
    class="glass gradient-border rounded-2xl p-6 flex flex-col gap-4 glass-hover cursor-default group"
    @mousemove="onMouseMove"
    @mouseleave="onMouseLeave"
    :style="tiltStyle"
  >
    <!-- Icon -->
    <div :class="['w-12 h-12 rounded-xl flex items-center justify-center transition-all duration-300 group-hover:scale-110', iconBg]">
      <component :is="icon" :size="22" :class="iconColor" />
    </div>

    <!-- Content -->
    <div>
      <h3 class="font-semibold text-white text-base mb-1.5">{{ title }}</h3>
      <p class="text-sm text-white/55 leading-relaxed">{{ description }}</p>
    </div>

    <!-- Bottom glow line -->
    <div :class="['h-px bg-gradient-to-r opacity-0 group-hover:opacity-100 transition-opacity duration-300', glowLine]"></div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  icon: Object,
  title: String,
  description: String,
  color: { type: String, default: 'purple' } // purple | cyan | emerald | red
})

const colorMap = {
  purple: { iconBg: 'bg-purple-500/15', iconColor: 'text-purple-400', glowLine: 'from-transparent via-purple-500/60 to-transparent' },
  cyan:   { iconBg: 'bg-cyan-500/15',   iconColor: 'text-cyan-400',   glowLine: 'from-transparent via-cyan-500/60 to-transparent' },
  emerald:{ iconBg: 'bg-emerald-500/15',iconColor: 'text-emerald-400',glowLine: 'from-transparent via-emerald-500/60 to-transparent' },
  red:    { iconBg: 'bg-red-500/15',    iconColor: 'text-red-400',    glowLine: 'from-transparent via-red-500/60 to-transparent' },
}
const { iconBg, iconColor, glowLine } = computed(() => colorMap[props.color] || colorMap.purple).value

// Subtle tilt effect
const tiltStyle = ref({})
function onMouseMove(e) {
  const rect = e.currentTarget.getBoundingClientRect()
  const x = (e.clientX - rect.left) / rect.width - 0.5
  const y = (e.clientY - rect.top) / rect.height - 0.5
  tiltStyle.value = { transform: `perspective(600px) rotateY(${x * 6}deg) rotateX(${-y * 6}deg) translateY(-4px)` }
}
function onMouseLeave() { tiltStyle.value = { transform: 'perspective(600px) rotateY(0deg) rotateX(0deg) translateY(0)' } }
</script>
