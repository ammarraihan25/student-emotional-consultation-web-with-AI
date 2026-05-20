import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { analyzeEmotion, getChatHistory } from '@/api/chat'

export const useChatStore = defineStore('chat', () => {
  const currentSessionId = ref('active')
  const messages = ref([
    {
      id: 'welcome',
      role: 'assistant',
      content: 'Halo! Aku Aether, teman AI-mu. 👋\n\nCeritakan apa yang kamu rasakan hari ini. Aku di sini untuk mendengarkan dan membantumu memahami emosimu.',
      timestamp: new Date(),
      emotion: null,
      score: null
    }
  ])

  // Dynamically group past chats as history sessions in the sidebar
  const sessions = computed(() => {
    const userMsgs = messages.value.filter(m => m.role === 'user')
    const list = [
      { id: 'active', title: 'Sesi Aktif', date: new Date().toLocaleDateString('id-ID'), active: currentSessionId.value === 'active' }
    ]
    userMsgs.forEach(m => {
      const cleanTitle = m.content.length > 25 ? m.content.substring(0, 25) + '...' : m.content
      list.push({
        id: m.id,
        title: cleanTitle,
        date: new Date(m.timestamp).toLocaleDateString('id-ID'),
        active: currentSessionId.value === m.id
      })
    })
    // Show active first, then past history in reverse chronological order
    const [active, ...historyList] = list
    return [active, ...historyList.reverse()]
  })

  // Filter messages shown in ChatWindow based on selected session in the sidebar
  const displayedMessages = computed(() => {
    if (currentSessionId.value === 'active') {
      return messages.value
    }
    const idx = messages.value.findIndex(m => m.id === currentSessionId.value)
    if (idx === -1) return messages.value
    // Display all messages up to this specific user prompt and its AI response
    return messages.value.slice(0, idx + 2)
  })

  const isTyping = ref(false)
  const isAnalyzing = ref(false)
  const currentEmotion = ref(null) // 'Hijau' | 'Kuning' | 'Merah'
  const currentScore = ref(0)
  const currentDetails = ref([])
  const showEmergencyModal = ref(false)
  const isLoaded = ref(false)

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

  async function loadHistory() {
    isTyping.value = true
    try {
      const history = await getChatHistory()
      if (history && history.length > 0) {
        const loadedMessages = []
        const chronologicalHistory = [...history].reverse()
        
        // Helper to format date
        const baseTime = chronologicalHistory[0]?.created_at ? new Date(chronologicalHistory[0].created_at).getTime() : Date.now()

        loadedMessages.push({
          id: 'welcome',
          role: 'assistant',
          content: 'Halo! Aku Aether, teman AI-mu. 👋\n\nCeritakan apa yang kamu rasakan hari ini. Aku di sini untuk mendengarkan dan membantumu memahami emosimu.',
          timestamp: new Date(baseTime - 1000),
          emotion: null,
          score: null
        })

        chronologicalHistory.forEach(record => {
          loadedMessages.push({
            id: record.id + '_user',
            role: 'user',
            content: record.user_message,
            timestamp: new Date(record.created_at),
            emotion: null,
            score: null
          })
          loadedMessages.push({
            id: record.id + '_ai',
            role: 'assistant',
            content: record.ai_response,
            timestamp: new Date(record.created_at),
            emotion: record.risk_indicator,
            score: record.total_score
          })
        })
        
        messages.value = loadedMessages

        // Update current emotion and score to the latest one
        const latest = chronologicalHistory[chronologicalHistory.length - 1]
        currentEmotion.value = latest.risk_indicator
        currentScore.value = latest.total_score
      }
      isLoaded.value = true
    } catch (err) {
      console.error('Failed to load history', err)
    } finally {
      isTyping.value = false
    }
  }

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
    currentSessionId.value = 'active'
    messages.value = [{
      id: 'welcome',
      role: 'assistant',
      content: 'Sesi baru dimulai! Ceritakan apa yang kamu rasakan hari ini. 💙',
      timestamp: new Date(),
      emotion: null,
      score: null
    }]
    currentEmotion.value = null
    currentScore.value = 0
    currentDetails.value = []
  }

  function selectSession(id) {
    currentSessionId.value = id
    
    // If selecting a specific message exchange, update current analytics panel details
    if (id !== 'active') {
      const userMsgIdx = messages.value.findIndex(m => m.id === id)
      if (userMsgIdx !== -1) {
        const aiMsg = messages.value[userMsgIdx + 1]
        if (aiMsg && aiMsg.role === 'assistant') {
          currentEmotion.value = aiMsg.emotion
          currentScore.value = aiMsg.score
        }
      }
    } else {
      // Restore to latest
      const latestAiMsg = [...messages.value].reverse().find(m => m.role === 'assistant' && m.score !== null)
      if (latestAiMsg) {
        currentEmotion.value = latestAiMsg.emotion
        currentScore.value = latestAiMsg.score
      }
    }
  }

  return {
    sessions, currentSessionId, messages, displayedMessages,
    isTyping, isAnalyzing,
    currentEmotion, currentScore, currentDetails, emotionLabel, emotionColor,
    sessionScore, sessionEmotion,
    showEmergencyModal, isLoaded,
    sendMessage, newSession, selectSession, loadHistory
  }
})
