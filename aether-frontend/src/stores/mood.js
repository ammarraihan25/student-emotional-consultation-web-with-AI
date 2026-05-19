import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useMoodStore = defineStore('mood', () => {
  // Mock data for demo
  const weeklyData = ref([
    { day: 'Sen', score: 12, emotion: 'Hijau', label: 'Stabil' },
    { day: 'Sel', score: 45, emotion: 'Kuning', label: 'Distress' },
    { day: 'Rab', score: 28, emotion: 'Hijau', label: 'Stabil' },
    { day: 'Kam', score: 65, emotion: 'Kuning', label: 'Distress' },
    { day: 'Jum', score: 18, emotion: 'Hijau', label: 'Stabil' },
    { day: 'Sab', score: 82, emotion: 'Merah', label: 'Krisis' },
    { day: 'Min', score: 22, emotion: 'Hijau', label: 'Stabil' },
  ])

  const stats = ref({
    totalSessions: 14,
    streak: 5,
    avgScore: 39,
    stabilityPercent: 71,
  })

  const emotionDistribution = ref({
    Hijau: 8,
    Kuning: 4,
    Merah: 2,
  })

  return { weeklyData, stats, emotionDistribution }
})
