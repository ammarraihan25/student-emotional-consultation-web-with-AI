<template>
  <div class="glass rounded-2xl p-4 border border-white/8 space-y-4">
    <div class="flex items-center gap-2">
      <Brain :size="15" class="text-cyan-400" />
      <span class="text-xs text-white/50 font-medium uppercase tracking-wider">Panel Analisis</span>
    </div>

    <!-- NLP Indicators -->
    <div class="space-y-2">
      <div v-for="ind in indicators" :key="ind.label" class="flex items-center gap-2">
        <div :class="['w-2 h-2 rounded-full shrink-0', ind.color]"></div>
        <span class="text-xs text-white/60 flex-1">{{ ind.label }}</span>
        <span :class="['text-xs font-semibold', ind.valueColor]">{{ ind.value }}</span>
      </div>
    </div>

    <div class="h-px bg-white/8"></div>

    <!-- Rincian Rule Kalkulasi -->
    <div v-if="details && details.length > 0">
      <p class="text-[10px] text-white/40 mb-2 font-medium uppercase tracking-wider">Kalkulasi Rule</p>
      <div class="space-y-1.5 max-h-32 overflow-y-auto pr-1">
        <div v-for="(d, idx) in details" :key="idx" class="flex items-center justify-between bg-white/5 px-2.5 py-1.5 rounded-lg border border-white/5">
          <div class="flex-1 min-w-0 pr-2">
            <p class="text-[10px] text-white/80 font-medium truncate">{{ d.category }}</p>
            <p class="text-[9px] text-white/40 truncate">Kunci: "{{ d.keyword }}"</p>
          </div>
          <span :class="['text-[11px] font-bold shrink-0', d.points > 0 ? 'text-purple-400' : 'text-emerald-400']">
            {{ d.points > 0 ? '+' : '' }}{{ d.points }}
          </span>
        </div>
      </div>
    </div>

    <div v-if="details && details.length > 0" class="h-px bg-white/8"></div>

    <!-- Recommendation -->
    <div v-if="emotion">
      <p class="text-xs text-white/40 mb-2 font-medium">Rekomendasi</p>
      <div :class="['rounded-xl p-3 text-xs leading-relaxed', recStyle]">
        {{ recommendation }}
      </div>
    </div>

    <div v-else class="text-center py-3">
      <Cpu :size="28" class="text-white/15 mx-auto mb-2" />
      <p class="text-xs text-white/30">Kirim pesan untuk memulai analisis emosi</p>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { Brain, Cpu } from '@lucide/vue'

const props = defineProps({
  emotion: { type: String, default: null },
  score: { type: Number, default: 0 },
  details: { type: Array, default: () => [] }
})

const indicators = computed(() => {
  const s = props.score
  const e = props.emotion
  return [
    {
      label: 'Kategori Masalah',
      value: s > 0 ? `+${Math.min(s, 30)} poin` : '--',
      color: 'bg-purple-400',
      valueColor: 'text-purple-300'
    },
    {
      label: 'Kedalaman Emosi',
      value: e ? (e === 'Hijau' ? 'Rendah' : e === 'Kuning' ? 'Sedang' : 'Tinggi') : '--',
      color: 'bg-cyan-400',
      valueColor: 'text-cyan-300'
    },
    {
      label: 'Indikator Risiko',
      value: e === 'Merah' ? '⚠️ Terdeteksi' : 'Tidak ada',
      color: e === 'Merah' ? 'bg-red-400 animate-pulse' : 'bg-emerald-400',
      valueColor: e === 'Merah' ? 'text-red-400' : 'text-emerald-400'
    },
    {
      label: 'Total Skor',
      value: props.score > 0 ? String(props.score) : '--',
      color: 'bg-white/30',
      valueColor: 'text-white/70'
    }
  ]
})

const recommendation = computed(() => {
  const map = {
    Hijau: 'Kondisimu terlihat stabil. Pertahankan kebiasaan positifmu dan tetap jaga kesehatan mentalmu. 💚',
    Kuning: 'Coba teknik relaksasi napas dalam 4-7-8. Istirahat sejenak dan hubungi teman terdekatmu. 💛',
    Merah: 'Segera hubungi konselor atau seseorang yang kamu percaya. Kamu tidak perlu menanggung ini sendirian. 🆘'
  }
  return map[props.emotion] || ''
})

const recStyle = computed(() => {
  const map = {
    Hijau: 'bg-emerald-500/10 border border-emerald-500/20 text-emerald-300/80',
    Kuning: 'bg-yellow-500/10 border border-yellow-500/20 text-yellow-300/80',
    Merah: 'bg-red-500/10 border border-red-500/20 text-red-300/80'
  }
  return map[props.emotion] || ''
})
</script>
