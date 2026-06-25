<template>
  <div class="glass rounded-2xl p-4.5 border border-white/8 space-y-4.5 shadow-lg">
    <div class="flex items-center gap-2">
      <Brain :size="15" class="text-cyan-400 animate-pulse" />
      <span class="text-xs text-white/50 font-semibold uppercase tracking-wider">Panel Analisis AI</span>
    </div>

    <!-- NLP Indicators -->
    <div class="space-y-2.5">
      <div v-for="ind in indicators" :key="ind.label" class="flex items-center justify-between text-xs">
        <div class="flex items-center gap-2">
          <div :class="['w-2 h-2 rounded-full shrink-0', ind.color]"></div>
          <span class="text-white/60 font-medium">{{ ind.label }}</span>
        </div>
        <span :class="['font-semibold', ind.valueColor]">{{ ind.value }}</span>
      </div>
    </div>

    <div class="h-px bg-white/5"></div>

    <!-- Rincian Rule Kalkulasi -->
    <div v-if="details && details.length > 0" class="space-y-2">
      <p class="text-[10px] text-white/35 font-bold uppercase tracking-widest">Kalkulasi Rule NLP</p>
      <div class="space-y-1.5 max-h-36 overflow-y-auto pr-1">
        <div 
          v-for="(d, idx) in details" 
          :key="idx" 
          class="flex items-center justify-between bg-white/3 px-3 py-2 rounded-xl border border-white/5 hover:border-white/10 transition-colors"
        >
          <div class="flex-1 min-w-0 pr-2">
            <span class="inline-block px-1.5 py-0.5 rounded text-[8px] font-bold bg-purple-500/10 text-purple-300 border border-purple-500/20 mb-0.5">{{ d.category }}</span>
            <p class="text-[10px] text-white/70 font-medium truncate">Kata kunci: <span class="italic text-white">"{{ d.keyword }}"</span></p>
          </div>
          <span :class="['text-[11px] font-black shrink-0', d.points > 0 ? 'text-purple-400' : 'text-emerald-400']">
            {{ d.points > 0 ? '+' : '' }}{{ d.points }}
          </span>
        </div>
      </div>
    </div>

    <div v-if="details && details.length > 0" class="h-px bg-white/5"></div>

    <!-- Recommendation -->
    <div v-if="emotion" class="space-y-2">
      <p class="text-[10px] text-white/35 font-bold uppercase tracking-widest">Rekomendasi Tindakan</p>
      <div :class="['rounded-xl p-3.5 text-xs leading-relaxed border shadow-sm transition-all duration-500', recStyle]">
        <div class="font-bold mb-1 flex items-center gap-1.5">
          <span class="text-sm select-none">{{ recEmoji }}</span>
          Rekomendasi Aether:
        </div>
        <p class="text-white/80 leading-relaxed font-medium">{{ recommendation }}</p>
      </div>
    </div>

    <div v-else class="text-center py-5 space-y-2">
      <Cpu :size="24" class="text-white/10 mx-auto mb-1 animate-spin-slow" />
      <p class="text-xs text-white/30 max-w-[180px] mx-auto">Kirim cerita keluhanmu untuk melihat visualisasi analisis emosi.</p>
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
      value: s > 0 ? `+${Math.min(s, 30)} Poin` : '--',
      color: 'bg-purple-400 shadow-[0_0_8px_rgba(168,85,247,0.4)]',
      valueColor: 'text-purple-300 font-semibold'
    },
    {
      label: 'Kedalaman Emosi',
      value: e ? (e === 'Hijau' ? 'Normal' : e === 'Kuning' ? 'Sedang' : 'Tinggi') : '--',
      color: 'bg-cyan-400 shadow-[0_0_8px_rgba(34,211,238,0.4)]',
      valueColor: 'text-cyan-300 font-semibold'
    },
    {
      label: 'Indikator Risiko',
      value: e === 'Merah' ? '⚠️ Tinggi (Krisis)' : 'Aman',
      color: e === 'Merah' ? 'bg-red-400 animate-pulse shadow-[0_0_8px_rgba(239,68,68,0.5)]' : 'bg-emerald-400 shadow-[0_0_8px_rgba(16,185,129,0.4)]',
      valueColor: e === 'Merah' ? 'text-red-400 font-bold' : 'text-emerald-400 font-semibold'
    },
    {
      label: 'Total Skor',
      value: props.score > 0 ? `${props.score} / 100` : '--',
      color: 'bg-white/20',
      valueColor: 'text-white/80 font-bold'
    }
  ]
})

const recommendation = computed(() => {
  const map = {
    Hijau: 'Kondisimu terlihat stabil dan sehat. Teruskan pola hidup yang seimbang, lakukan meditasi berkala, dan tetap berpikir positif.',
    Kuning: 'Lakukan relaksasi pernapasan 4-7-8 yang ada di dasbor chat. Istirahatkan diri sejenak dari tugas kuliah, dan luapkan perasaanmu ke teman terdekat.',
    Merah: 'Sistem mendeteksi tingkat stres yang tinggi. Tolong jangan simpan beban ini sendirian. Hubungi layanan konseling kampus atau kontak darurat kami segera.'
  }
  return map[props.emotion] || ''
})

const recEmoji = computed(() => {
  const map = { Hijau: '🟢', Kuning: '🟡', Merah: '🔴' }
  return map[props.emotion] || '🍃'
})

const recStyle = computed(() => {
  const map = {
    Hijau: 'bg-emerald-500/5 border-emerald-500/20 text-emerald-300 shadow-[0_4px_15px_rgba(16,185,129,0.05)]',
    Kuning: 'bg-yellow-500/5 border-yellow-500/20 text-yellow-300 shadow-[0_4px_15px_rgba(234,179,8,0.05)]',
    Merah: 'bg-red-500/5 border-red-500/20 text-red-300 shadow-[0_4px_15px_rgba(239,68,68,0.08)] animate-pulse'
  }
  return map[props.emotion] || ''
})
</script>

