import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { analyzeEmotion } from '@/api/chat'

export const useChatStore = defineStore('chat', () => {
  const sessions = ref([
    { id: 1, title: 'Sesi Hari Ini', date: new Date().toLocaleDateString('id-ID'), active: true },
    { id: 2, title: 'Kemarin', date: new Date(Date.now() - 86400000).toLocaleDateString('id-ID'), active: false },
  ])
  const currentSessionId = ref(1)
  const messages = ref([
    {
      id: 1,
      role: 'assistant',
      content: 'Halo! Aku Aether, teman AI-mu. 👋\n\nCeritakan apa yang kamu rasakan hari ini. Aku di sini untuk mendengarkan dan membantumu memahami emosimu.',
      timestamp: new Date(),
      emotion: null,
      score: null
    }
  ])
  const isTyping = ref(false)
  const isAnalyzing = ref(false)
  const currentEmotion = ref(null) // 'Hijau' | 'Kuning' | 'Merah'
  const currentScore = ref(0)
  const currentDetails = ref([])
  const showEmergencyModal = ref(false)

  const emotionLabel = computed(() => {
    const map = { Hijau: 'Stabil', Kuning: 'Distress Emosional', Merah: 'Krisis' }
    return currentEmotion.value ? map[currentEmotion.value] : 'Belum terdeteksi'
  })

  const emotionColor = computed(() => {
    const map = { Hijau: 'emerald', Kuning: 'yellow', Merah: 'red' }
    return currentEmotion.value ? map[currentEmotion.value] : 'gray'
  })

  // Calculated overall session scores and emotions (maximum/worst-case of all turns in current session)
  const sessionScores = computed(() => {
    return messages.value
      .filter(m => m.role === 'assistant' && m.score !== null)
      .map(m => m.score)
  })

  const sessionScore = computed(() => {
    const scores = sessionScores.value
    if (scores.length === 0) return 0
    return Math.max(...scores)
  })

  const sessionEmotion = computed(() => {
    const score = sessionScore.value
    if (sessionScores.value.length === 0) return null
    return score > 70 ? 'Merah' : score >= 36 ? 'Kuning' : 'Hijau'
  })

  async function sendMessage(text) {
    if (!text.trim()) return

    // Add user message
    messages.value.push({
      id: Date.now(),
      role: 'user',
      content: text,
      timestamp: new Date(),
      emotion: null,
      score: null
    })

    isTyping.value = true
    isAnalyzing.value = true

    try {
      const result = await analyzeEmotion(text)
      const { total_skor, indikator, ai_response, details } = result

      currentScore.value = total_skor
      currentEmotion.value = indikator
      currentDetails.value = details || []

      // Show emergency modal for red indicator
      if (indikator === 'Merah') {
        showEmergencyModal.value = true
      }

      // Simulate typing delay
      await new Promise(r => setTimeout(r, 800))
      isTyping.value = false
      isAnalyzing.value = false

      messages.value.push({
        id: Date.now() + 1,
        role: 'assistant',
        content: ai_response,
        timestamp: new Date(),
        emotion: indikator,
        score: total_skor
      })
    } catch (err) {
      isTyping.value = false
      isAnalyzing.value = false
      messages.value.push({
        id: Date.now() + 1,
        role: 'assistant',
        content: 'Maaf, aku sedang mengalami gangguan koneksi. Coba lagi sebentar ya. 🙏',
        timestamp: new Date(),
        emotion: null,
        score: null
      })
    }
  }

  function newSession() {
    const id = Date.now()
    sessions.value.unshift({ id, title: 'Sesi Baru', date: new Date().toLocaleDateString('id-ID'), active: true })
    sessions.value = sessions.value.map(s => ({ ...s, active: s.id === id }))
    currentSessionId.value = id
    messages.value = [{
      id: 1,
      role: 'assistant',
      content: 'Sesi baru dimulai! Ceritakan apa yang kamu rasakan hari ini. 💙',
      timestamp: new Date(),
      emotion: null,
      score: null
    }]
    currentEmotion.value = null
    currentScore.value = 0
  }

  function selectSession(id) {
    sessions.value = sessions.value.map(s => ({ ...s, active: s.id === id }))
    currentSessionId.value = id
  }

  return {
    sessions, currentSessionId, messages,
    isTyping, isAnalyzing,
    currentEmotion, currentScore, currentDetails, emotionLabel, emotionColor,
    sessionScore, sessionEmotion,
    showEmergencyModal,
    sendMessage, newSession, selectSession
  }
})
