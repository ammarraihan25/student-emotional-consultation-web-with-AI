import { defineStore } from 'pinia'
import { ref } from 'vue'
import { getChatHistory } from '@/api/chat'

export const useMoodStore = defineStore('mood', () => {
  const weeklyData = ref([])
  const stats = ref({
    totalSessions: 0,
    streak: 0,
    avgScore: 0,
    stabilityPercent: 100,
  })

  const emotionDistribution = ref({
    Hijau: 0,
    Kuning: 0,
    Merah: 0,
  })

  const isLoading = ref(false)

  async function fetchMoodData() {
    isLoading.value = true
    try {
      const history = await getChatHistory()
      if (history && history.length > 0) {
        // 1. Distribution
        const dist = { Hijau: 0, Kuning: 0, Merah: 0 }
        let totalScore = 0
        let hijauCount = 0
        
        history.forEach(item => {
          const ind = item.risk_indicator || 'Hijau'
          dist[ind] = (dist[ind] || 0) + 1
          totalScore += item.total_score || 0
          if (ind === 'Hijau') hijauCount++
        })
        
        emotionDistribution.value = dist
        
        // 2. Stats
        stats.value.totalSessions = history.length
        stats.value.avgScore = Math.round(totalScore / history.length)
        stats.value.stabilityPercent = Math.round((hijauCount / history.length) * 100)
        
        // Compute streak (consecutive days with chat sessions)
        const uniqueDates = [...new Set(history.map(item => new Date(item.created_at).toDateString()))]
        let currentStreak = 0
        let checkDate = new Date()
        
        while (true) {
          if (uniqueDates.includes(checkDate.toDateString())) {
            currentStreak++
            checkDate.setDate(checkDate.getDate() - 1)
          } else {
            break
          }
        }
        stats.value.streak = currentStreak

        // 3. Weekly Data (last 7 entries chronologically)
        const daysOfWeek = ['Min', 'Sen', 'Sel', 'Rab', 'Kam', 'Jum', 'Sab']
        const last7 = [...history].reverse().slice(-7)
        
        weeklyData.value = last7.map(item => {
          const d = new Date(item.created_at)
          const labelMap = { Hijau: 'Stabil', Kuning: 'Distress', Merah: 'Krisis' }
          return {
            day: daysOfWeek[d.getDay()],
            score: item.total_score,
            emotion: item.risk_indicator || 'Hijau',
            label: labelMap[item.risk_indicator || 'Hijau']
          }
        })
      } else {
        // Default empty states
        weeklyData.value = [
          { day: 'Sen', score: 0, emotion: 'Hijau', label: 'Stabil' },
          { day: 'Sel', score: 0, emotion: 'Hijau', label: 'Stabil' },
          { day: 'Rab', score: 0, emotion: 'Hijau', label: 'Stabil' },
          { day: 'Kam', score: 0, emotion: 'Hijau', label: 'Stabil' },
          { day: 'Jum', score: 0, emotion: 'Hijau', label: 'Stabil' },
          { day: 'Sab', score: 0, emotion: 'Hijau', label: 'Stabil' },
          { day: 'Min', score: 0, emotion: 'Hijau', label: 'Stabil' },
        ]
        stats.value = {
          totalSessions: 0,
          streak: 0,
          avgScore: 0,
          stabilityPercent: 100,
        }
        emotionDistribution.value = {
          Hijau: 0,
          Kuning: 0,
          Merah: 0,
        }
      }
    } catch (err) {
      console.error('Failed to load mood tracking data', err)
    } finally {
      isLoading.value = false
    }
  }

  return { weeklyData, stats, emotionDistribution, isLoading, fetchMoodData }
})

