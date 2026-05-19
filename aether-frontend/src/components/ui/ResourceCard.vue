<template>
  <div class="glass rounded-2xl overflow-hidden glass-hover group cursor-pointer" @click="$emit('click')">
    <!-- Thumbnail -->
    <div class="relative h-44 overflow-hidden">
      <div :class="['absolute inset-0 bg-gradient-to-br', thumbnail]"></div>
      <div class="absolute inset-0 flex items-center justify-center text-5xl">{{ emoji }}</div>
      <!-- Category badge -->
      <div class="absolute top-3 left-3">
        <span :class="['text-xs font-semibold px-2.5 py-1 rounded-full', categoryStyle]">{{ category }}</span>
      </div>
      <!-- Duration -->
      <div class="absolute bottom-3 right-3 glass rounded-lg px-2 py-1 text-xs text-white/70 flex items-center gap-1">
        <Clock :size="11" />
        {{ duration }}
      </div>
    </div>

    <!-- Content -->
    <div class="p-4">
      <h3 class="font-semibold text-white text-sm mb-1.5 group-hover:text-purple-300 transition-colors line-clamp-2">{{ title }}</h3>
      <p class="text-xs text-white/50 leading-relaxed line-clamp-2">{{ description }}</p>
      <div class="flex items-center gap-2 mt-3">
        <component :is="typeIcon" :size="13" class="text-white/30" />
        <span class="text-xs text-white/30">{{ type }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { Clock, BookOpen, Video, Wind, Heart } from '@lucide/vue'

const props = defineProps({
  title: String,
  description: String,
  category: { type: String, default: 'Artikel' },
  duration: { type: String, default: '5 menit' },
  type: { type: String, default: 'Artikel' },
  emoji: { type: String, default: '📖' },
  thumbnail: { type: String, default: 'from-purple-900/60 to-navy-900' }
})

defineEmits(['click'])

const categoryColors = {
  Artikel: 'bg-purple-500/20 text-purple-300 border border-purple-500/30',
  Video: 'bg-cyan-500/20 text-cyan-300 border border-cyan-500/30',
  Meditasi: 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/30',
  Breathing: 'bg-blue-500/20 text-blue-300 border border-blue-500/30',
  Tips: 'bg-yellow-500/20 text-yellow-300 border border-yellow-500/30',
}
const categoryStyle = computed(() => categoryColors[props.category] || categoryColors.Artikel)

const typeIconMap = { Artikel: BookOpen, Video, Meditasi: Heart, Breathing: Wind, Tips: Heart }
const typeIcon = computed(() => typeIconMap[props.type] || BookOpen)
</script>
