import axios from 'axios'
import { PREDEFINED_RESPONSES } from './predefined_responses.js'

// Direct call to FastAPI on port 8000 (via Vite proxy /ai → http://127.0.0.1:8000)
const aiClient = axios.create({
  baseURL: '/ai',
  timeout: 30000,
  headers: { 'Content-Type': 'application/json' }
})

// Helper to normalize messages for robust matching
function cleanMessage(msg) {
  if (!msg) return ''
  return msg.toLowerCase().trim().replace(/[.,\/#!$%\^&\*;:{}=\-_`~()?]+$/, '').trim()
}

// Build normalized dictionary at startup
const normalizedPredefined = {}
for (const [key, value] of Object.entries(PREDEFINED_RESPONSES)) {
  normalizedPredefined[cleanMessage(key)] = value
}

/**
 * Analyze emotion via Python FastAPI NLP engine
 * POST /ai/analyze-emotion → FastAPI → returns { pesan_asli, total_skor, indikator, ai_response }
 *
 * TODO: Route this through Laravel API (/api/chat) once backend is ready
 */
export async function analyzeEmotion(message) {
  try {
    const response = await aiClient.post('/analyze-emotion', { message })
    return response.data
  } catch (err) {
    // Fallback mock for demo when FastAPI is not running
    console.warn('[Aether] FastAPI offline — using mock response')
    return mockAnalyze(message)
  }
}

function mockAnalyze(message) {
  const text = message.toLowerCase()
  let score = 10

  // Simple keyword scoring for demo
  if (text.includes('burnout') || text.includes('lelah')) score += 35
  if (text.includes('skripsi') || text.includes('deadline')) score += 20
  if (text.includes('nangis') || text.includes('sedih')) score += 25
  if (text.includes('bunuh diri') || text.includes('mengakhiri hidup')) score += 60
  if (text.includes('gapapa') || text.includes('semangat')) score -= 10
  score = Math.max(0, Math.min(100, score))

  const indikator = score > 70 ? 'Merah' : score >= 36 ? 'Kuning' : 'Hijau'
  
  // Check if it's one of the predefined responses first
  const cleaned = cleanMessage(message)
  let ai_response = normalizedPredefined[cleaned]

  if (!ai_response) {
    const responses = {
      Hijau: 'Wah, kayaknya kamu lagi oke-oke aja nih! Tetap jaga semangatnya ya. Kalau ada yang mau diceritain, aku selalu di sini. 😊',
      Kuning: 'Aku dengerin kok. Kayaknya kamu lagi menanggung banyak beban ya? Wajar banget ngerasa kayak gitu. Coba ceritain lebih lanjut, yuk kita urutkan satu-satu bareng-bareng. 💛',
      Merah: 'Aku sangat khawatir sama kamu sekarang. Perasaan seperti ini terlalu berat untuk ditanggung sendirian. Tolong hubungi seseorang yang kamu percaya segera, ya. Kamu tidak sendirian. ❤️'
    }
    ai_response = responses[indikator]
  }

  return {
    pesan_asli: message,
    total_skor: score,
    indikator,
    ai_response
  }
}

export async function getChatHistory() {
  // TODO: GET /api/chat/history
  return []
}
