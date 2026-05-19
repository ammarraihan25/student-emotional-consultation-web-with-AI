import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
from nlp_engine import calculate_emotion_score # Memanggil mesin yang kita buat tadi

# Memuat isi file .env ke dalam sistem
load_dotenv()

app = FastAPI()

# Mengizinkan akses dari aplikasi Laravel
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8080", "http://localhost:8080", "http://web-konseling.test"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatInput(BaseModel):
    message: str

@app.post("/analyze-emotion")
def analyze_emotion(data: ChatInput):
    
    # 1. Lakukan Perhitungan dengan modul nlp_engine.py
    score, indicator = calculate_emotion_score(data.message)

    # 2. Instruksi ke Gemini (memasukkan contoh tabel gaya bahasa)
    system_prompt = f"""
    Kamu adalah chatbot konselor sebaya (peer counselor) untuk mahasiswa. 
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

    # 3. Tembak ke API Google secara langsung
    try:
        # API Key 
        api_key = os.getenv("GEMINI_API_KEY")
        
        # Masukkan nama model yang sudah berhasil terdeteksi aktif di komputermu sebelumnya
        # (misalnya: gemini-1.5-flash-latest atau gemini-2.5-flash)
        model_name = "gemini-2.5-flash" 
        
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={api_key}"
        
        payload = {
            "contents": [{"parts": [{"text": system_prompt}]}]
        }
        
        response = requests.post(url, headers={'Content-Type': 'application/json'}, json=payload)
        data_json = response.json()
        
        # Mengambil teks balasan dari struktur JSON Google
        ai_reply = data_json['candidates'][0]['content']['parts'][0]['text']
        
    except Exception as e:
        ai_reply = "Maaf, sistem AI sedang gangguan. Tarik napas pelan-pelan, kamu pasti bisa melewati ini."
        print(f"Error API: {e}")

    # 4. Kembalikan data lengkap ke frontend Laravel
    return {
        "pesan_asli": data.message,
        "total_skor": score,
        "indikator": indicator,
        "ai_response": ai_reply
    }