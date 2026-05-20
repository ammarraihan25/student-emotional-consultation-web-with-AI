<template>
  <div class="min-h-screen bg-[#050b18] overflow-x-hidden">
    <Navbar />

    <!-- Floating BG Blobs -->
    <div class="fixed inset-0 pointer-events-none overflow-hidden z-0">
      <div class="absolute top-[-10%] left-[-5%] w-96 h-96 rounded-full bg-purple-700/20 blur-[120px] animate-float"></div>
      <div class="absolute top-[30%] right-[-8%] w-80 h-80 rounded-full bg-cyan-600/15 blur-[100px] animate-float2"></div>
      <div class="absolute bottom-[10%] left-[20%] w-72 h-72 rounded-full bg-indigo-700/20 blur-[100px] animate-float3"></div>
    </div>

    <!-- HERO -->
    <section class="relative min-h-screen flex items-center justify-center pt-24 pb-16 px-4">
      <div class="max-w-5xl mx-auto text-center z-10">
        <!-- Badge -->
        <div class="inline-flex items-center gap-2 glass border border-purple-500/30 rounded-full px-4 py-2 mb-8 animate-fade-in">
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
          <span class="text-xs text-white/70 font-medium">AI Mental Health Platform untuk Mahasiswa</span>
        </div>

        <!-- Headline with typewriter -->
        <h1 class="text-5xl sm:text-6xl lg:text-7xl font-black leading-tight mb-6 animate-slide-up">
          <span class="text-white">Pahami </span>
          <span class="gradient-text">Emosimu</span>
          <br />
          <span class="text-white/90">Bersama AI</span>
        </h1>

        <p class="text-lg sm:text-xl text-white/55 max-w-2xl mx-auto mb-10 leading-relaxed animate-slide-up" style="animation-delay:0.1s">
          Aether membantu mahasiswa mengenali kondisi emosional melalui chatbot AI berbasis NLP dan Rule-Based Scoring.
          <span class="text-purple-400 font-medium"> Kamu tidak sendirian.</span>
        </p>

        <!-- CTA Buttons -->
        <div class="flex flex-col sm:flex-row items-center justify-center gap-4 mb-16 animate-slide-up" style="animation-delay:0.2s">
          <router-link to="/register"
            class="btn-glow text-white font-bold px-8 py-4 rounded-2xl text-base flex items-center gap-2 w-full sm:w-auto justify-center">
            <MessageSquare :size="18" /> Mulai Percakapan
          </router-link>
          <a href="#features"
            class="btn-outline-glow font-semibold px-8 py-4 rounded-2xl text-base flex items-center gap-2 w-full sm:w-auto justify-center">
            <Compass :size="18" /> Jelajahi Fitur
          </a>
        </div>

        <!-- Floating Dashboard Preview -->
        <div class="relative max-w-3xl mx-auto animate-slide-up" style="animation-delay:0.3s">
          <div class="glass gradient-border rounded-3xl p-4 sm:p-6 shadow-[0_0_60px_rgba(168,85,247,0.15)]">
            <div class="flex items-center gap-2 mb-4">
              <div class="w-3 h-3 rounded-full bg-red-400/70"></div>
              <div class="w-3 h-3 rounded-full bg-yellow-400/70"></div>
              <div class="w-3 h-3 rounded-full bg-emerald-400/70"></div>
              <div class="flex-1 ml-2 h-5 glass rounded-full flex items-center px-3">
                <span class="text-xs text-white/30">aether.ai/chat</span>
              </div>
            </div>
            <!-- Mock chat preview -->
            <div class="space-y-3 text-left">
              <div class="flex gap-3">
                <div class="w-7 h-7 rounded-lg bg-gradient-to-br from-purple-700 to-indigo-800 flex items-center justify-center text-xs shrink-0">Æ</div>
                <div class="glass rounded-2xl rounded-tl-sm px-4 py-2 text-xs text-white/80 max-w-xs">Halo! Ceritakan apa yang kamu rasakan hari ini 💙</div>
              </div>
              <div class="flex gap-3 flex-row-reverse">
                <div class="w-7 h-7 rounded-lg bg-gradient-to-br from-purple-600 to-cyan-500 flex items-center justify-center text-xs font-bold shrink-0">M</div>
                <div class="bg-gradient-to-br from-purple-600 to-purple-700 rounded-2xl rounded-tr-sm px-4 py-2 text-xs text-white max-w-xs">Aku burnout banget sama tugas kuliah...</div>
              </div>
              <div class="flex gap-3">
                <div class="w-7 h-7 rounded-lg bg-gradient-to-br from-purple-700 to-indigo-800 flex items-center justify-center text-xs shrink-0">Æ</div>
                <div class="flex flex-col gap-1.5">
                  <div class="glass rounded-2xl rounded-tl-sm px-4 py-2 text-xs text-white/80 max-w-xs">Pasti pusing ya kalau semuanya numpuk. Coba tarik napas dulu 🌿</div>
                  <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-semibold bg-yellow-500/15 border border-yellow-500/40 text-yellow-400 w-fit">
                    <span class="w-1.5 h-1.5 rounded-full bg-yellow-400 animate-pulse"></span> Distress Emosional (42)
                  </span>
                </div>
              </div>
            </div>
          </div>
          <!-- Glow under card -->
          <div class="absolute inset-x-8 bottom-0 h-px bg-gradient-to-r from-transparent via-purple-500/60 to-transparent blur-sm"></div>
        </div>
      </div>
    </section>

    <!-- FEATURES -->
    <section id="features" class="section-padding relative z-10">
      <div class="max-w-7xl mx-auto">
        <div class="text-center mb-14">
          <span class="text-xs text-purple-400 font-semibold uppercase tracking-widest mb-3 block">Fitur Unggulan</span>
          <h2 class="text-3xl sm:text-4xl font-bold text-white mb-4">Dirancang untuk <span class="gradient-text">Kesejahteraan</span> Kamu</h2>
          <p class="text-white/50 max-w-xl mx-auto">Platform AI komprehensif yang memahami, menganalisis, dan mendukung kondisi emosional mahasiswa.</p>
        </div>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
          <FeatureCard v-for="f in features" :key="f.title" v-bind="f" />
        </div>
      </div>
    </section>

    <!-- HOW IT WORKS -->
    <section id="how-it-works" class="section-padding relative z-10">
      <div class="max-w-5xl mx-auto">
        <div class="text-center mb-14">
          <span class="text-xs text-cyan-400 font-semibold uppercase tracking-widest mb-3 block">Alur Sistem</span>
          <h2 class="text-3xl sm:text-4xl font-bold text-white mb-4">Cara <span class="gradient-text">Aether</span> Bekerja</h2>
        </div>
        <div class="flex flex-col gap-0">
          <div v-for="(step, i) in steps" :key="i" class="flex gap-6 items-start">
            <div class="flex flex-col items-center">
              <div :class="['w-12 h-12 rounded-2xl flex items-center justify-center font-bold text-lg border-2 shrink-0', step.style]">{{ i+1 }}</div>
              <div v-if="i < steps.length-1" class="w-px flex-1 min-h-[3rem] bg-gradient-to-b from-purple-500/40 to-transparent my-1"></div>
            </div>
            <div class="glass rounded-2xl p-5 mb-4 flex-1 glass-hover">
              <div class="flex items-center gap-3 mb-2">
                <component :is="step.icon" :size="18" :class="step.iconColor" />
                <h3 class="font-semibold text-white text-sm">{{ step.title }}</h3>
              </div>
              <p class="text-xs text-white/50 leading-relaxed">{{ step.desc }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- EMOTION CLASSIFICATION -->
    <section id="emotion" class="section-padding relative z-10">
      <div class="max-w-5xl mx-auto">
        <div class="text-center mb-14">
          <span class="text-xs text-emerald-400 font-semibold uppercase tracking-widest mb-3 block">Sistem Klasifikasi</span>
          <h2 class="text-3xl sm:text-4xl font-bold text-white mb-4">3 Level <span class="gradient-text">Indikator</span> Emosi</h2>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
          <div v-for="level in emotionLevels" :key="level.label"
            :class="['glass rounded-3xl p-7 border text-center transition-all duration-300 hover:-translate-y-1', level.border]">
            <div :class="['text-5xl mb-4 inline-block', level.glow]">{{ level.emoji }}</div>
            <h3 :class="['text-xl font-bold mb-1', level.textColor]">{{ level.label }}</h3>
            <p class="text-xs text-white/50 mb-4">Skor: {{ level.range }}</p>
            <p class="text-sm text-white/70 leading-relaxed">{{ level.desc }}</p>
          </div>
        </div>
        <!-- Example analysis -->
        <div class="glass gradient-border rounded-2xl p-6 max-w-2xl mx-auto">
          <p class="text-xs text-white/40 mb-3 font-medium uppercase tracking-wider">Contoh Analisis Real-Time</p>
          <div class="glass rounded-xl p-4 mb-4 text-sm text-white/80 italic">"Aku burnout banget sama tugas kuliah, deadline numpuk dan nggak ada habisnya..."</div>
          <div class="flex items-center gap-3 flex-wrap">
            <span class="text-xs text-white/40">→ Hasil:</span>
            <EmotionBadge emotion="Kuning" :score="42" />
            <span class="text-xs text-white/40">Skor: 42 | NLP: burnout (+4), deadline (+6), tugas numpuk (+6)</span>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA BANNER -->
    <section class="section-padding relative z-10">
      <div class="max-w-3xl mx-auto text-center">
        <div class="glass gradient-border rounded-3xl p-10 sm:p-14">
          <h2 class="text-3xl sm:text-4xl font-black text-white mb-4">Siap Memulai?</h2>
          <p class="text-white/55 mb-8 text-lg">Bergabung dengan Aether dan mulai kenali kondisi emosionalmu hari ini.</p>
          <router-link to="/register" class="btn-glow text-white font-bold px-10 py-4 rounded-2xl text-base inline-flex items-center gap-2">
            <Sparkles :size="18" /> Mulai Sekarang — Gratis
          </router-link>
        </div>
      </div>
    </section>

    <!-- FOOTER -->
    <footer class="border-t border-white/8 py-8 px-4 text-center z-10 relative">
      <div class="flex items-center justify-center gap-2 mb-3">
        <div class="w-6 h-6 rounded-lg bg-gradient-to-br from-purple-600 to-cyan-500 flex items-center justify-center text-white font-black text-xs">Æ</div>
        <span class="font-bold text-white/80">Aether</span>
      </div>
      <p class="text-xs text-white/30">© 2024 Aether AI Mental Health Platform · Dibuat dengan 💜 untuk mahasiswa Indonesia</p>
    </footer>
  </div>
</template>

<script setup>
import { Brain, Shield, TrendingUp, BookOpen, AlertTriangle, Heart, Lock, Activity, MessageSquare, Compass, Sparkles, User, Cpu, Zap } from '@lucide/vue'
import Navbar from '@/components/layout/Navbar.vue'
import FeatureCard from '@/components/ui/FeatureCard.vue'
import EmotionBadge from '@/components/ui/EmotionBadge.vue'

const features = [
  { title: 'AI Emotion Detection', description: 'Deteksi emosi real-time dari teks curhatan menggunakan NLP berbasis Rule-Based Scoring.', icon: Brain, color: 'purple' },
  { title: 'NLP Text Analysis', description: 'Analisis teks mendalam: keyword matching, context detection, dan scoring calculation.', icon: Cpu, color: 'cyan' },
  { title: 'Crisis Detection', description: 'Deteksi dini kata kunci risiko tinggi dan berikan intervensi sebelum terlambat.', icon: AlertTriangle, color: 'red' },
  { title: 'Mood Tracking', description: 'Pantau tren emosionalmu dengan grafik mingguan dan analitik visual.', icon: TrendingUp, color: 'emerald' },
  { title: 'Empathetic AI', description: 'Respons AI yang empatik, personal, dan non-judgmental — seperti teman curhat terbaik.', icon: Heart, color: 'purple' },
  { title: 'Resource Center', description: 'Akses artikel, video meditasi, breathing exercise, dan tips self-healing.', icon: BookOpen, color: 'cyan' },
  { title: 'Risk Indicator', description: 'Indikator visual 🟢🟡🔴 yang jelas dan rekomendasi otomatis sesuai kondisi.', icon: Activity, color: 'emerald' },
  { title: 'Private & Secure', description: 'Data percakapanmu terenkripsi dan privat. Kami menjaga kepercayaanmu.', icon: Lock, color: 'purple' },
]

const steps = [
  { title: 'Input Pesan', desc: 'Mahasiswa mengirim curahan hati melalui antarmuka chat yang ramah dan aman.', icon: MessageSquare, iconColor: 'text-purple-400', style: 'border-purple-500/50 bg-purple-500/10 text-purple-300' },
  { title: 'NLP Text Processing', desc: 'Sistem memproses teks: normalisasi, tokenisasi, dan keyword extraction.', icon: Cpu, iconColor: 'text-cyan-400', style: 'border-cyan-500/50 bg-cyan-500/10 text-cyan-300' },
  { title: 'Rule-Based Scoring', desc: 'Mesin NLP menghitung skor dari 4 kategori: masalah, urgensi, risiko, dan regulasi positif.', icon: Zap, iconColor: 'text-yellow-400', style: 'border-yellow-500/50 bg-yellow-500/10 text-yellow-300' },
  { title: 'Emotion Classification', desc: 'Skor dikonversi ke indikator: 🟢 Stabil / 🟡 Distress / 🔴 Krisis.', icon: Activity, iconColor: 'text-emerald-400', style: 'border-emerald-500/50 bg-emerald-500/10 text-emerald-300' },
  { title: 'AI Response & Rekomendasi', desc: 'Gemini AI menghasilkan respons empatik CBT-based dan sistem memberikan rekomendasi tindakan.', icon: Brain, iconColor: 'text-purple-400', style: 'border-purple-500/50 bg-purple-500/10 text-purple-300' },
]

const emotionLevels = [
  { emoji: '🟢', label: 'Stabil', range: '0 – 35', desc: 'Kondisi emosional dalam batas normal. Tetap jaga keseimbangan dan rutinitas positifmu.', border: 'border-emerald-500/30', textColor: 'text-emerald-400', glow: 'animate-pulse-glow-green' },
  { emoji: '🟡', label: 'Distress Emosional', range: '36 – 70', desc: 'Terdapat tekanan emosional yang signifikan. Disarankan berbicara dengan teman atau konselor.', border: 'border-yellow-500/30', textColor: 'text-yellow-400', glow: 'animate-pulse-glow-yellow' },
  { emoji: '🔴', label: 'Krisis', range: '> 70', desc: 'Indikator risiko tinggi terdeteksi. Segera hubungi konselor atau layanan darurat kesehatan jiwa.', border: 'border-red-500/30', textColor: 'text-red-400', glow: 'animate-pulse-glow-red' },
]
</script>
