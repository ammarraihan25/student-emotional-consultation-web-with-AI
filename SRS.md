# Software Requirements Specification (SRS)
## AETHER - Platform Konsultasi Kesehatan Mental Mahasiswa Berbasis AI

**Versi:** 1.0 | **Status:** Active Development | **Tanggal:** Juni 2024

---

## 1. Deskripsi Sistem

**AETHER** adalah platform konsultasi kesehatan mental real-time untuk mahasiswa dengan AI counselor yang menggunakan NLP untuk analisis emosi dan Gemini API untuk respons berempati berbasis CBT (Cognitive Behavioral Therapy).

### Arsitektur 3-Tier
```
Frontend (Vue 3 + Vite)          Backend (Laravel 13)         AI Engine (Python + FastAPI)
Port: 5173                       Port: 8080                   Port: 8000
├─ Chat Interface               ├─ Authentication (Sanctum)  ├─ NLP Scoring
├─ Mood Tracking               ├─ Chat Management            ├─ Gemini AI
├─ Resources Center            ├─ User Management            ├─ Predefined Responses
└─ Analytics                   └─ Database (MySQL)           └─ Crisis Detection
```

---

## 2. FRONTEND REQUIREMENTS

### Features
| Feature | Component | Status |
|---------|-----------|--------|
| Landing Page | LandingPage.vue | ✓ |
| Login/Register | LoginPage.vue, RegisterPage.vue | ✓ |
| Chat Interface | ChatPage.vue, ChatWindow.vue | ✓ |
| Mood Tracking | MoodTracking.vue + MoodChart.vue | ✓ |
| Resource Center | ResourceCenter.vue | ✓ |
| User Profile | ProfilePage.vue | ⏳ |
| Emergency Modal | EmergencyModal.vue | ✓ |

### Tech Stack
- Vue 3 (Composition API)
- Vite (Build Tool)
- Tailwind CSS v4
- Pinia (State Management)
- Axios (HTTP Client)
- Chart.js (Visualization)

### State Management (Pinia)
```javascript
// Auth Store
auth.js: {isAuthenticated, user, token, isLoading, error}

// Chat Store  
chat.js: {sessions, messages, currentSessionId, isAnalyzing, sessionScore, sessionEmotion, showEmergencyModal}

// Mood Store
mood.js: {weeklyStats, averageScore, moodDistribution, isLoading}
```

### Key Endpoints (Frontend → Backend)
```
POST   /api/register           # Register user
POST   /api/login              # Login with email/password
POST   /api/demo-login         # Quick demo login
POST   /api/logout             # Logout
GET    /api/user               # Get current user
POST   /api/chat/analyze       # Send message for analysis
GET    /api/chat/history       # Get chat history
DELETE /api/chat/:id           # Delete chat session
GET    /api/mood/weekly        # Get mood statistics
```

---

## 3. BACKEND REQUIREMENTS

### Features
| Feature | Controller | Status |
|---------|-----------|--------|
| User Registration | AuthController::register() | ✓ |
| User Login | AuthController::login() | ✓ |
| Demo Login | AuthController::demoLogin() | ✓ |
| Chat Analysis | ChatController::analyze() | ✓ |
| Chat History | ChatController::history() | ✓ |
| Mood Statistics | ChatController (methods) | ✓ |

### Tech Stack
- Laravel Framework 13
- PHP 8.3+
- Laravel Sanctum (Token Auth)
- MySQL Database
- Eloquent ORM

### Database Schema
```sql
-- Users Table
CREATE TABLE users (
  id BIGINT PRIMARY KEY,
  name VARCHAR(255),
  email VARCHAR(255) UNIQUE,
  password VARCHAR(255) -- bcrypt hashed,
  last_emotional_status ENUM('Hijau','Kuning','Merah'),
  created_at, updated_at
);

-- Chat Sessions Table
CREATE TABLE chat_sessions (
  id BIGINT PRIMARY KEY,
  user_id BIGINT -- FK,
  user_message TEXT,
  ai_response TEXT,
  risk_indicator ENUM('Hijau','Kuning','Merah'),
  total_score INT(0-100),
  details JSON,
  created_at, updated_at,
  INDEX(user_id, created_at)
);
```

### API Endpoints Detail

**POST /api/register**
```json
Request: {name, email, password, password_confirmation}
Response: {id, name, email, token, message: "Registrasi berhasil"}
```

**POST /api/login**
```json
Request: {email, password}
Response: {id, name, email, token, message: "Login berhasil"}
```

**POST /api/chat/analyze** (auth required)
```json
Request: {message: "Aku stres banget sama tugas kuliah"}
Response: {
  pesan_asli, 
  total_skor: 65,
  indikator: "Kuning",
  ai_response: "Aku dengerin kok...",
  details: [{category, keyword, points}, ...]
}
```

**GET /api/chat/history** (auth required)
```json
Response: [{id, user_message, ai_response, risk_indicator, total_score, created_at}, ...]
```

### Key Functions
- **Password Hashing:** bcrypt (Laravel Hash facade)
- **JWT Token:** Laravel Sanctum (personal access tokens)
- **AI Integration:** HTTP call to Python FastAPI with 30s timeout
- **Fallback:** Local keyword-based response if AI server offline
- **Database:** Eloquent relationships (User → ChatSessions)

---

## 4. API & NLP ENGINE REQUIREMENTS

### Tech Stack
- FastAPI (Python)
- Uvicorn Server (Port 8000)
- Google Gemini 2.5-Flash API
- NLTK (NLP)

### Endpoint: POST /analyze-emotion
```json
Request: {message: "Aku stres banget..."}
Response: {
  pesan_asli,
  total_skor: 0-100,
  indikator: "Hijau|Kuning|Merah",
  ai_response: "...",
  details: [...]
}
```

### NLP Scoring Engine (nlp_engine.py)

**4 Scoring Categories:**
1. **Masalah (0-40 poin):** Keywords untuk akademik/sosial (tugas, skripsi, teman, bully, dst)
2. **Urgensi (0-30 poin):** Keywords emosi intensif (stres, sedih, takut, cemas, burnout, dst)
3. **Krisis (0-20 poin):** Keywords bahaya diri (bunuh diri, mengakhiri hidup, dst)
4. **Regulasi Positif (-20 poin max):** Keywords positif (semangat, lega, optimis, dst)

**Score Formula:**
```
total_score = MIN(100, MAX(0, 
  base(10) + akademik_score + urgensi_score + krisis_score - positif_score
))
```

**Classification:**
- 🟢 **Hijau (0-35):** Stabil
- 🟡 **Kuning (36-70):** Distress Emosional
- 🔴 **Merah (>70):** Krisis

### Response Generation Pipeline

**Priority 1: Predefined Responses (170+ patterns)**
- Normalized message matching → Return pre-written response instantly
- Benefit: Sub-millisecond response, 100% accuracy

**Priority 2: Google Gemini API (if no match)**
```python
system_prompt = """
Kamu adalah chatbot konselor sebaya (peer counselor) untuk mahasiswa.
Curhat: "{message}"
Status: {indicator} (Skor: {score})

Instruksi:
1. Berikan respons penuh empati, validasi perasaan
2. Jika Kuning/Merah: sisipkan teknik CBT (napas, perspective shift)
3. Gunakan bahasa kasual mahasiswa ('aku', 'kamu')
4. Maksimal 3 paragraf
"""
# Call Gemini API → Return response
```

**Priority 3: Fallback (if Gemini timeout)**
- Use keyword-based response from category matching

### CORS Configuration
```python
allow_origins: [
  "http://127.0.0.1:8080",  # Laravel
  "http://localhost:8080",
  "http://localhost:5173",   # Vue dev
  "http://127.0.0.1:5173"
]
```

---

## 5. DATA FLOW & USER JOURNEY

### Chat Processing Flow
```
1. User types message in Vue frontend
   ↓
2. Frontend: POST /api/chat/analyze {message}
   ↓
3. Laravel Backend: 
   - Validate message (required, max 5000 chars)
   - Get authenticated user
   - Forward to Python AI: HTTP POST :8000/analyze-emotion
   ↓
4. Python AI Engine:
   - Normalize text (slang → standard Indonesian)
   - Run NLP scoring → Calculate score + indicator
   - Check predefined responses
   - Call Gemini API (if needed) → Generate response
   - Append analysis breakdown
   ↓
5. Laravel Backend:
   - Save to DB: ChatSession (user_id, message, response, score, indicator)
   - Update user.last_emotional_status
   - Return response to frontend
   ↓
6. Vue Frontend:
   - Display AI response with typewriter animation
   - Update EmotionBadge (score + indicator)
   - Show AnalyticsPanel breakdown
   - Trigger EmergencyModal if Merah
   - Update Mood Chart data
```

### Authentication Flow
```
1. User → Frontend: email + password
2. POST /api/login
3. Backend: Verify password (bcrypt) + Generate Sanctum token
4. Frontend: Store JWT in localStorage + Set Authorization header
5. Subsequent requests: Authorization: Bearer {token}
6. Backend: auth:sanctum middleware validates token
```

---

## 6. SECURITY REQUIREMENTS

| Requirement | Implementation | Status |
|-------------|-----------------|--------|
| Password hashing | bcrypt (Laravel Hash) | ✓ |
| Authentication | JWT via Sanctum | ✓ |
| Protected routes | auth:sanctum middleware | ✓ |
| Input validation | Laravel validation rules | ✓ |
| SQL injection prevention | Eloquent ORM | ✓ |
| XSS protection | Vue template escaping | ✓ |
| CSRF protection | Laravel middleware | ✓ |
| Rate limiting | 50 req/min per user (planned) | ⏳ |
| Crisis detection | NLP keyword matching | ✓ |
| Emergency resources | Modal with hotlines | ✓ |

---

## 7. PERFORMANCE TARGETS

| Metric | Target |
|--------|--------|
| Analyze endpoint latency | < 2s (predefined), < 5s (Gemini) |
| Frontend FCP | < 2s |
| Frontend LCP | < 3s |
| Database query | < 500ms |
| API response | < 1s |

---

## 8. SETUP & DEPLOYMENT

### Local Development
```bash
# Terminal 1: Backend (Port 8080)
cd web-konseling
composer install && cp .env.example .env
php artisan key:generate && php artisan migrate
php artisan serve --port=8080

# Terminal 2: AI Engine (Port 8000)
cd ai-konseling
python -m venv venv && source venv/bin/activate
pip install fastapi uvicorn requests pydantic python-dotenv
echo "GEMINI_API_KEY=your_key" > .env
uvicorn main:app --reload --port 8000

# Terminal 3: Frontend (Port 5173)
cd aether-frontend
npm install && npm run dev
```

### Production Checklist
- [ ] Enable HTTPS/TLS
- [ ] Set APP_ENV=production
- [ ] Configure CORS for production domain
- [ ] Setup database backups (daily)
- [ ] Enable error monitoring (Sentry)
- [ ] Configure rate limiting
- [ ] Setup environment variables in .env (secrets)
- [ ] Enable database encryption

---

## 9. TECHNOLOGY SUMMARY

| Layer | Tech | Version |
|-------|------|---------|
| **Frontend** | Vue 3 | 3.4.29 |
| | Vite | 5.3.1 |
| | Tailwind | 4.0.0 |
| | Pinia | 2.1.7 |
| **Backend** | Laravel | 13.0 |
| | PHP | 8.3+ |
| | Sanctum | 4.3 |
| | MySQL | 5.7+ |
| **AI** | FastAPI | Latest |
| | Python | 3.10+ |
| | Gemini API | 2.5-Flash |
| | NLTK | Latest |

---

## 10. FEATURES SUMMARY

### ✓ Implemented
- User registration & login (JWT + Sanctum)
- Real-time chat with AI counselor
- Emotion analysis (NLP + Gemini)
- Mood tracking & visualization
- Emergency crisis detection & modal
- Resource center (tips, meditation)
- Chat history management
- Responsive design (mobile + desktop)

### ⏳ Planned
- User profile & settings
- Export mood data (CSV/PDF)
- Rate limiting
- Advanced filtering & search
- Video resources
- Integration with professional counselors
- Mobile app (React Native)

---

## 11. Glossary

| Term | Meaning |
|------|---------|
| **Hijau** | Green - Stable emotional status (0-35) |
| **Kuning** | Yellow - Emotional distress (36-70) |
| **Merah** | Red - Crisis status (>70) |
| **NLP** | Natural Language Processing |
| **CBT** | Cognitive Behavioral Therapy |
| **Sanctum** | Laravel API authentication package |
| **Predefined Response** | Pre-written therapeutic response |
| **Gemini** | Google's generative AI model |
| **Pinia** | Vue 3 state management |

---

**Document Version:** 1.0  
**Last Updated:** Juni 2024  
**Next Review:** Desember 2024
