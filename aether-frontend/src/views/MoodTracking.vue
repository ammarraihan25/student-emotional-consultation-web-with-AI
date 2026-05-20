<template>
  <div class="min-h-screen bg-[#050b18] flex">
    <Sidebar :sessions="[]" :show-history="false" @logout="handleLogout" />

    <div class="flex-1 md:ml-64 overflow-y-auto">
      <div class="max-w-5xl mx-auto px-4 sm:px-6 py-8">
        <!-- Header -->
        <div class="mb-8">
          <h1 class="text-2xl font-bold text-white mb-1">Mood <span class="gradient-text">Tracking</span></h1>
          <p class="text-sm text-white/50">Pantau tren emosionalmu selama 7 hari terakhir</p>
        </div>

        <!-- Stats cards -->
        <div class="grid grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
          <div v-for="stat in stats" :key="stat.label"
            class="glass rounded-2xl p-5 border border-white/8 flex flex-col gap-2">
            <div :class="['w-10 h-10 rounded-xl flex items-center justify-center', stat.bg]">
              <component :is="stat.icon" :size="18" :class="stat.color" />
            </div>
            <p :class="['text-2xl font-black', stat.color]">{{ stat.value }}</p>
            <p class="text-xs text-white/50">{{ stat.label }}</p>
          </div>
        </div>

        <!-- Charts row -->
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-8">
          <!-- Line chart -->
          <div class="lg:col-span-2 glass rounded-2xl p-6 border border-white/8">
            <h2 class="text-sm font-semibold text-white mb-4 flex items-center gap-2">
              <TrendingUp :size="16" class="text-purple-400" /> Tren Emosi 7 Hari
            </h2>
            <MoodChart :data="moodStore.weeklyData" />
          </div>

          <!-- Distribution -->
          <div class="glass rounded-2xl p-6 border border-white/8">
            <h2 class="text-sm font-semibold text-white mb-4 flex items-center gap-2">
              <PieChart :size="16" class="text-cyan-400" /> Distribusi Emosi
            </h2>
            <div class="space-y-4 mt-2">
              <div v-for="item in distribution" :key="item.label" class="flex flex-col gap-1.5">
                <div class="flex justify-between text-xs">
                  <span class="text-white/70 flex items-center gap-1.5">{{ item.emoji }} {{ item.label }}</span>
                  <span :class="item.color">{{ item.pct }}%</span>
                </div>
                <div class="h-2 bg-white/10 rounded-full overflow-hidden">
                  <div :class="['h-full rounded-full transition-all duration-1000', item.bar]" :style="`width:${item.pct}%`"></div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Weekly calendar -->
        <div class="glass rounded-2xl p-6 border border-white/8">
          <h2 class="text-sm font-semibold text-white mb-5 flex items-center gap-2">
            <Calendar :size="16" class="text-emerald-400" /> Kalender Mingguan
          </h2>
          <div class="grid grid-cols-7 gap-3">
            <div v-for="day in moodStore.weeklyData" :key="day.day" class="flex flex-col items-center gap-2">
              <span class="text-xs text-white/40">{{ day.day }}</span>
              <div :class="['w-10 h-10 rounded-xl flex items-center justify-center text-lg border transition-all', dayStyle(day.emotion)]">
                {{ dayEmoji(day.emotion) }}
              </div>
              <span class="text-xs text-white/50">{{ day.score }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { TrendingUp, Flame, Activity, ShieldCheck, PieChart, Calendar } from '@lucide/vue'
import { useMoodStore } from '@/stores/mood'
import { useAuthStore } from '@/stores/auth'
import Sidebar from '@/components/layout/Sidebar.vue'
import MoodChart from '@/components/mood/MoodChart.vue'

const moodStore = useMoodStore()
const auth = useAuthStore()
const router = useRouter()

onMounted(() => {
  moodStore.fetchMoodData()
})

const total = computed(() => {
  const d = moodStore.emotionDistribution
  return (d.Hijau || 0) + (d.Kuning || 0) + (d.Merah || 0)
})

const distribution = computed(() => [
  { label: 'Stabil', emoji: '🟢', pct: total.value > 0 ? Math.round((moodStore.emotionDistribution.Hijau / total.value) * 100) : 0, color: 'text-emerald-400', bar: 'bg-emerald-500' },
  { label: 'Distress', emoji: '🟡', pct: total.value > 0 ? Math.round((moodStore.emotionDistribution.Kuning / total.value) * 100) : 0, color: 'text-yellow-400', bar: 'bg-yellow-500' },
  { label: 'Krisis', emoji: '🔴', pct: total.value > 0 ? Math.round((moodStore.emotionDistribution.Merah / total.value) * 100) : 0, color: 'text-red-400', bar: 'bg-red-500' },
])

const stats = computed(() => [
  { label: 'Total Sesi', value: moodStore.stats.totalSessions, icon: Activity, color: 'text-purple-400', bg: 'bg-purple-500/15' },
  { label: 'Hari Berturut-turut', value: `${moodStore.stats.streak} 🔥`, icon: Flame, color: 'text-orange-400', bg: 'bg-orange-500/15' },
  { label: 'Rata-rata Skor', value: moodStore.stats.avgScore, icon: TrendingUp, color: 'text-cyan-400', bg: 'bg-cyan-500/15' },
  { label: 'Stabilitas', value: `${moodStore.stats.stabilityPercent}%`, icon: ShieldCheck, color: 'text-emerald-400', bg: 'bg-emerald-500/15' },
])

function dayEmoji(e) { return { Hijau: '😌', Kuning: '😟', Merah: '😰' }[e] || '❓' }
function dayStyle(e) {
  return { Hijau: 'border-emerald-500/40 bg-emerald-500/10', Kuning: 'border-yellow-500/40 bg-yellow-500/10', Merah: 'border-red-500/40 bg-red-500/10' }[e] || 'border-white/10 bg-white/5'
}

function handleLogout() { auth.logout(); router.push('/') }
</script>
