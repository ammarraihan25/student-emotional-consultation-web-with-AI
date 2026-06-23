<template>
  <div class="min-h-screen bg-[#050b18] flex">
    <Sidebar :sessions="[]" :show-history="false" @logout="handleLogout" />

    <div class="flex-1 md:ml-64 overflow-y-auto">

      <!-- ── Hero Header Banner ── -->
      <div class="relative overflow-hidden border-b border-white/5">
        <div class="absolute inset-0 bg-gradient-to-r from-purple-900/50 via-indigo-900/30 to-[#050b18]"></div>
        <div class="absolute top-0 right-0 w-64 h-full bg-gradient-to-l from-cyan-900/20 to-transparent"></div>
        <div class="absolute -top-10 left-48 w-48 h-48 rounded-full bg-purple-600/10 blur-[60px]"></div>
        <div class="relative z-10 max-w-5xl mx-auto px-4 sm:px-6 py-8 flex items-start justify-between gap-4">
          <div class="space-y-2">
            <div class="flex items-center gap-2.5">
              <div class="w-9 h-9 rounded-xl bg-gradient-to-br from-purple-500 to-cyan-600 flex items-center justify-center shadow-[0_0_15px_rgba(168,85,247,0.3)]">
                <TrendingUp :size="16" class="text-white" />
              </div>
              <div>
                <h1 class="text-xl font-black text-white leading-tight">Mood <span class="gradient-text">Tracking</span></h1>
                <p class="text-xs text-white/45">Pantau perjalanan emosionalmu — 7 hari terakhir</p>
              </div>
            </div>
            <p class="text-xs text-white/35 max-w-sm leading-relaxed">
              Melacak mood adalah langkah pertama menuju pemahaman diri yang lebih dalam. Pola ini akan membantu Aether memberikan saran yang lebih personal.
            </p>
          </div>
          <!-- Decorative emotion ring -->
          <div class="hidden sm:flex items-center gap-3 shrink-0">
            <div v-for="(e, i) in ['😌','😟','😊','😴','😰']" :key="i"
              :class="['w-9 h-9 rounded-full glass border border-white/10 flex items-center justify-center text-lg transition-all hover:scale-110 cursor-default', `animation-delay-${i}`]"
              :style="`animation-delay: ${i * 0.15}s`"
            >{{ e }}</div>
          </div>
        </div>
      </div>

      <div class="max-w-5xl mx-auto px-4 sm:px-6 py-8 space-y-6">

        <!-- ── Stats cards ── -->
        <div class="grid grid-cols-2 lg:grid-cols-4 gap-4">
          <div v-for="stat in stats" :key="stat.label"
            :class="['relative rounded-2xl p-5 border overflow-hidden flex flex-col gap-3 group hover:-translate-y-0.5 transition-all duration-300', stat.cardBg, stat.cardBorder]"
          >
            <div class="absolute -top-4 -right-4 w-20 h-20 rounded-full opacity-10 blur-xl" :class="stat.glowBg"></div>
            <div class="flex items-center justify-between">
              <div :class="['w-9 h-9 rounded-xl flex items-center justify-center', stat.bg]">
                <component :is="stat.icon" :size="16" :class="stat.color" />
              </div>
              <span :class="['text-xs font-bold px-2 py-0.5 rounded-full', stat.badgeBg, stat.color]">↑</span>
            </div>
            <div>
              <p :class="['text-2xl font-black', stat.color]">{{ stat.value }}</p>
              <p class="text-xs text-white/45 mt-0.5">{{ stat.label }}</p>
            </div>
          </div>
        </div>

        <!-- ── Charts row ── -->
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-5">
          <!-- Line chart -->
          <div class="lg:col-span-2 glass rounded-2xl p-5 border border-white/8">
            <div class="flex items-center justify-between mb-4">
              <h2 class="text-sm font-bold text-white flex items-center gap-2">
                <TrendingUp :size="15" class="text-purple-400" /> Tren Emosi 7 Hari
              </h2>
              <span class="text-[10px] text-white/35 px-2 py-1 rounded-lg bg-white/5 border border-white/8">📅 Minggu Ini</span>
            </div>
            <MoodChart :data="moodStore.weeklyData" />
          </div>

          <!-- Distribution -->
          <div class="glass rounded-2xl p-5 border border-white/8">
            <h2 class="text-sm font-bold text-white mb-4 flex items-center gap-2">
              <PieChart :size="15" class="text-cyan-400" /> Distribusi
            </h2>
            <div class="space-y-5">
              <div v-for="item in distribution" :key="item.label">
                <div class="flex justify-between text-xs mb-1.5">
                  <span class="text-white/70 flex items-center gap-1.5 font-medium">{{ item.emoji }} {{ item.label }}</span>
                  <span :class="['font-bold', item.color]">{{ item.pct }}%</span>
                </div>
                <div class="h-2 bg-white/8 rounded-full overflow-hidden">
                  <div :class="['h-full rounded-full transition-all duration-1000 ease-out', item.bar]" :style="`width:${item.pct}%`"></div>
                </div>
                <p class="text-[10px] text-white/30 mt-1">{{ item.count }} sesi</p>
              </div>
            </div>

            <!-- Summary hint -->
            <div class="mt-5 pt-4 border-t border-white/5 text-[11px] text-white/45 leading-relaxed bg-white/3 rounded-xl p-3">
              💡 <span class="text-white/60 font-medium">Insight:</span> {{ moodInsight }}
            </div>
          </div>
        </div>

        <!-- ── Weekly calendar ── -->
        <div class="glass rounded-2xl p-5 border border-white/8">
          <div class="flex items-center justify-between mb-5">
            <h2 class="text-sm font-bold text-white flex items-center gap-2">
              <Calendar :size="15" class="text-emerald-400" /> Kalender Emosi Mingguan
            </h2>
            <div class="flex items-center gap-3 text-[10px] text-white/35">
              <span class="flex items-center gap-1"><span class="w-2 h-2 rounded-full bg-emerald-400 inline-block"></span> Stabil</span>
              <span class="flex items-center gap-1"><span class="w-2 h-2 rounded-full bg-yellow-400 inline-block"></span> Distress</span>
              <span class="flex items-center gap-1"><span class="w-2 h-2 rounded-full bg-red-400 inline-block"></span> Krisis</span>
            </div>
          </div>
          <div class="grid grid-cols-7 gap-2 sm:gap-3">
            <div v-for="day in moodStore.weeklyData" :key="day.day" class="flex flex-col items-center gap-2 group">
              <span class="text-[10px] text-white/40 font-medium">{{ day.day }}</span>
              <div :class="['w-10 h-10 rounded-xl flex items-center justify-center text-lg border transition-all duration-300 group-hover:scale-110 group-hover:-translate-y-0.5 cursor-default', dayStyle(day.emotion)]">
                {{ dayEmoji(day.emotion) }}
              </div>
              <span :class="['text-[10px] font-bold', dayScoreColor(day.emotion)]">{{ day.score }}</span>
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




const stats = computed(() => [
  { label: 'Total Sesi', value: moodStore.stats.totalSessions, icon: Activity, color: 'text-purple-400', bg: 'bg-purple-500/15', cardBg: 'bg-purple-500/5', cardBorder: 'border-purple-500/15', badgeBg: 'bg-purple-500/15', glowBg: 'bg-purple-500' },
  { label: 'Hari Berturut-turut', value: `${moodStore.stats.streak} 🔥`, icon: Flame, color: 'text-orange-400', bg: 'bg-orange-500/15', cardBg: 'bg-orange-500/5', cardBorder: 'border-orange-500/15', badgeBg: 'bg-orange-500/15', glowBg: 'bg-orange-500' },
  { label: 'Rata-rata Skor', value: moodStore.stats.avgScore, icon: TrendingUp, color: 'text-cyan-400', bg: 'bg-cyan-500/15', cardBg: 'bg-cyan-500/5', cardBorder: 'border-cyan-500/15', badgeBg: 'bg-cyan-500/15', glowBg: 'bg-cyan-500' },
  { label: 'Stabilitas', value: `${moodStore.stats.stabilityPercent}%`, icon: ShieldCheck, color: 'text-emerald-400', bg: 'bg-emerald-500/15', cardBg: 'bg-emerald-500/5', cardBorder: 'border-emerald-500/15', badgeBg: 'bg-emerald-500/15', glowBg: 'bg-emerald-500' },
])

const moodInsight = computed(() => {
  const d = moodStore.emotionDistribution
  const t = (d.Hijau || 0) + (d.Kuning || 0) + (d.Merah || 0)
  if (t === 0) return 'Belum ada data sesi minggu ini.'
  const pct = t > 0 ? Math.round(((d.Hijau || 0) / t) * 100) : 0
  if (pct >= 70) return 'Kondisi emosionalmu sebagian besar stabil minggu ini. Pertahankan!'
  if (pct >= 40) return 'Ada beberapa momen distress. Coba pertahankan rutinitas self-care.'
  return 'Minggu ini cukup berat. Jangan lupa untuk istirahat dan bicarakan perasaanmu.'
})

const distribution = computed(() => {
  const d = moodStore.emotionDistribution
  const t = (d.Hijau || 0) + (d.Kuning || 0) + (d.Merah || 0)
  return [
    { label: 'Stabil', emoji: '🟢', pct: t > 0 ? Math.round((d.Hijau / t) * 100) : 0, count: d.Hijau || 0, color: 'text-emerald-400', bar: 'bg-gradient-to-r from-emerald-500 to-teal-500' },
    { label: 'Distress', emoji: '🟡', pct: t > 0 ? Math.round((d.Kuning / t) * 100) : 0, count: d.Kuning || 0, color: 'text-yellow-400', bar: 'bg-gradient-to-r from-yellow-500 to-amber-500' },
    { label: 'Krisis', emoji: '🔴', pct: t > 0 ? Math.round((d.Merah / t) * 100) : 0, count: d.Merah || 0, color: 'text-red-400', bar: 'bg-gradient-to-r from-red-500 to-rose-500' },
  ]
})

function dayEmoji(e) { return { Hijau: '😌', Kuning: '😟', Merah: '😰' }[e] || '❓' }
function dayStyle(e) {
  return { Hijau: 'border-emerald-500/40 bg-emerald-500/10 shadow-[0_0_8px_rgba(16,185,129,0.15)]', Kuning: 'border-yellow-500/40 bg-yellow-500/10 shadow-[0_0_8px_rgba(234,179,8,0.15)]', Merah: 'border-red-500/40 bg-red-500/10 shadow-[0_0_8px_rgba(239,68,68,0.15)]' }[e] || 'border-white/10 bg-white/5'
}
function dayScoreColor(e) {
  return { Hijau: 'text-emerald-400', Kuning: 'text-yellow-400', Merah: 'text-red-400' }[e] || 'text-white/35'
}

function handleLogout() { auth.logout(); router.push('/') }
</script>
