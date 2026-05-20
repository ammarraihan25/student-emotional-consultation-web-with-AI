<template>
  <div class="glass rounded-2xl p-4 border border-white/8">
    <div class="flex items-center gap-2 mb-4">
      <TrendingUp :size="15" class="text-purple-400" />
      <span class="text-xs text-white/50 font-medium uppercase tracking-wider">Tren Emosi 7 Hari</span>
    </div>
    <Line :data="chartData" :options="chartOptions" class="max-h-40" />

    <!-- Legend -->
    <div class="flex items-center gap-4 mt-3 justify-center">
      <div class="flex items-center gap-1.5 text-xs text-white/40">
        <div class="w-3 h-0.5 bg-emerald-400 rounded"></div>
        <span>Stabil (0–35)</span>
      </div>
      <div class="flex items-center gap-1.5 text-xs text-white/40">
        <div class="w-3 h-0.5 bg-yellow-400 rounded"></div>
        <span>Distress (36–70)</span>
      </div>
      <div class="flex items-center gap-1.5 text-xs text-white/40">
        <div class="w-3 h-0.5 bg-red-400 rounded"></div>
        <span>Krisis (>70)</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { Line } from 'vue-chartjs'
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Tooltip, Filler } from 'chart.js'
import { TrendingUp } from '@lucide/vue'

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Tooltip, Filler)

const props = defineProps({
  data: { type: Array, default: () => [] }
})

const chartData = computed(() => ({
  labels: props.data.map(d => d.day),
  datasets: [{
    label: 'Skor Emosi',
    data: props.data.map(d => d.score),
    borderColor: 'rgba(168, 85, 247, 0.8)',
    backgroundColor: 'rgba(168, 85, 247, 0.08)',
    pointBackgroundColor: props.data.map(d =>
      d.score > 70 ? '#ef4444' : d.score >= 36 ? '#eab308' : '#10b981'
    ),
    pointBorderColor: 'transparent',
    pointRadius: 5,
    pointHoverRadius: 7,
    borderWidth: 2,
    tension: 0.4,
    fill: true
  }]
}))

const chartOptions = {
  responsive: true,
  maintainAspectRatio: true,
  plugins: { legend: { display: false }, tooltip: {
    backgroundColor: 'rgba(10, 22, 40, 0.95)',
    borderColor: 'rgba(168, 85, 247, 0.3)',
    borderWidth: 1,
    titleColor: '#f0f4ff',
    bodyColor: 'rgba(240, 244, 255, 0.6)',
    padding: 10,
    callbacks: {
      label: ctx => `Skor: ${ctx.raw} — ${ctx.raw > 70 ? '🔴 Krisis' : ctx.raw >= 36 ? '🟡 Distress' : '🟢 Stabil'}`
    }
  }},
  scales: {
    x: { grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: 'rgba(255,255,255,0.4)', font: { size: 11 } } },
    y: {
      min: 0, max: 100,
      grid: { color: 'rgba(255,255,255,0.05)' },
      ticks: { color: 'rgba(255,255,255,0.4)', font: { size: 11 }, stepSize: 35 }
    }
  }
}
</script>
