import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import re
from nlp_engine import calculate_emotion_score # Memanggil mesin yang kita buat tadi
from predefined_responses import PREDEFINED_RESPONSES

def clean_message(msg: str) -> str:
    msg = msg.lower().strip()
    msg = re.sub(r'[.,\/#!$%\^&\*;:{}=\-_`~()?]+$', '', msg).strip()
    return msg

NORMALIZED_PREDEFINED_RESPONSES = {clean_message(k): v for k, v in PREDEFINED_RESPONSES.items()}

# Memuat isi file .env ke dalam sistem
load_dotenv()

app = FastAPI()

# Mengizinkan akses dari aplikasi Laravel
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:8080", "http://localhost:8080", "http://web-konseling.test",
        "http://localhost:5173", "http://127.0.0.1:5173",   # Vite dev server (aether-frontend)
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatInput(BaseModel):
    message: str

@app.post("/analyze-emotion")
def analyze_emotion(data: ChatInput):
    
    # 1. Lakukan Perhitungan dengan modul nlp_engine.py
    score, indicator, details = calculate_emotion_score(data.message)

    # 2. Bersihkan pesan untuk pencarian jawaban kustom presisi tinggi
    msg_cleaned = clean_message(data.message)

    ai_reply = NORMALIZED_PREDEFINED_RESPONSES.get(msg_cleaned)

    # 3. Jika tidak ada di database kustom, gunakan Gemini AI
    if not ai_reply:
        system_prompt = f"""
        Kamu adalah chatbot konselor sebaya (peer counselor) untuk mahasiswa bernama Aether. 
        Seorang mahasiswa datang dan curhat: "{data.message}"
        
        Hasil deteksi sistem: Dia berada di indikator warna {indicator} (Skor: {score}).
        
        Instruksi wajib:
        1. Berikan respon penuh empati, validasi perasaannya, jangan menggurui.
        2. Jika indikator Kuning/Merah, sisipkan teknik CBT (misal: mengatur napas, melihat masalah dari sudut pandang lain).
        3. Gunakan bahasa kasual mahasiswa (gunakan 'aku' dan 'kamu').
        4. Balasan harus singkat (maksimal 3 paragraf).
        
        Contoh gaya bahasa yang HARUS kamu tiru (berdasarkan database kami):
        - "Pasti pusing ya kalau semuanya numpuk. Coba tarik napas dulu, kita urutkan satu-satu yuk."
        - "Aku dengerin kok. Sedih itu wajar banget, jangan dipendam sendirian ya."
        - "Sistem kampus emang kadang bikin emosi. Sabarin aja, yang penting lulus dan aman!"
        """

        try:
            api_key = os.getenv("GEMINI_API_KEY")
            model_name = "gemini-2.5-flash" 
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={api_key}"
            payload = {
                "contents": [{"parts": [{"text": system_prompt}]}]
            }
            response = requests.post(url, headers={'Content-Type': 'application/json'}, json=payload)
            data_json = response.json()
            ai_reply = data_json['candidates'][0]['content']['parts'][0]['text']
            
        except Exception as e:
            if indicator == "Merah":
                ai_reply = "Aku sangat khawatir padamu sekarang. Beban pikiran yang kamu rasakan itu wajar, tapi tolong jangan menanggungnya sendirian ya. Hubungi seseorang yang kamu percaya segera."
            elif details:
                # Mengambil kata kunci utama untuk memberikan respon spesifik tanpa Gemini
                kata_kunci = details[0]['keyword']
                kategori = details[0]['category']
                
                if "Akademik" in kategori:
                    ai_reply = f"Pasti pusing ya mikirin soal '{kata_kunci}'. Hal-hal berbau akademik memang sering menguras tenaga dan pikiran. Tarik napas dulu yuk, kita selesaikan satu per satu."
                elif "Sosial" in kategori or "Relasi" in kategori:
                    ai_reply = f"Masalah terkait '{kata_kunci}' memang bikin lelah hati. Kecewa atau sedih itu wajar banget. Aku di sini buat dengerin ceritamu sampai kamu merasa lega."
                elif "Internal" in kategori or "Pribadi" in kategori:
                    ai_reply = f"Perasaan '{kata_kunci}' yang kamu rasakan saat ini sangat valid. Gak apa-apa kalau hari ini terasa berat, istirahatlah sejenak dan jangan terlalu keras pada dirimu sendiri."
                elif "Regulasi" in kategori:
                    ai_reply = f"Wah, bagus banget kamu bisa bersikap '{kata_kunci}'! Pertahankan pola pikir positif ini ya, sangat membantu untuk kesehatan mentalmu."
                else:
                    ai_reply = f"Aku mengerti kamu sedang memikirkan soal '{kata_kunci}'. Ingatlah bahwa kamu tidak sendirian, pelan-pelan saja menghadapinya ya."
            else:
                ai_reply = "Aku mendengar keluhanmu. Tarik napas pelan-pelan, segala perasaanmu valid dan kamu pasti bisa melewati fase ini."
            
            print(f"Error API: {e}")

    # 4. Tambahkan rincian analisis ke dalam balasan chat (Fitur breakdown nilai poin keluhan)
    if details:
        breakdown = "\n\n---\n📊 **Analisis Keluhan & Poin Emosi:**\n"
        for d in details:
            sign = "+" if d['points'] > 0 else ""
            breakdown += f"• {d['category']} ('{d['keyword']}'): {sign}{d['points']} Poin\n"
        
        emoji = "🟢" if indicator == "Hijau" else "🟡" if indicator == "Kuning" else "🔴"
        breakdown += f"\n**Total Skor: {score} ({indicator} {emoji})**"
        
        ai_reply += breakdown

    # 5. Kembalikan data lengkap ke frontend Laravel/Vue
    return {
        "pesan_asli": data.message,
        "total_skor": score,
        "indikator": indicator,
        "ai_response": ai_reply,
        "details": details
    }