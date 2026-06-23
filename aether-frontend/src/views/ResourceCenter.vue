<template>
  <div class="min-h-screen bg-[#050b18] flex">
    <Sidebar :sessions="[]" :show-history="false" @logout="handleLogout" />

    <div class="flex-1 md:ml-64 overflow-y-auto">
      
      <!-- ── TOP HEADER BAR ── -->
      <div class="sticky top-0 z-30 bg-[#050b18]/90 backdrop-blur-xl border-b border-white/5">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 py-3 flex items-center justify-between gap-4">
          <!-- Title + breadcrumb -->
          <div class="flex items-center gap-3 min-w-0">
            <div class="w-8 h-8 rounded-lg bg-gradient-to-br from-teal-500 to-cyan-600 flex items-center justify-center shrink-0">
              <BookOpen :size="15" class="text-white" />
            </div>
            <div class="min-w-0">
              <h1 class="text-sm font-bold text-white truncate">Resource Center</h1>
              <p class="text-[10px] text-white/40 hidden sm:block">Artikel &amp; Panduan Kesehatan Mental</p>
            </div>
          </div>

          <!-- Search bar -->
          <div class="flex-1 max-w-md relative">
            <Search :size="14" class="absolute left-3 top-1/2 -translate-y-1/2 text-white/30 pointer-events-none" />
            <input
              v-model="searchQuery"
              type="text"
              placeholder="Cari artikel, tips, meditasi..."
              class="w-full bg-white/5 border border-white/8 hover:border-white/15 focus:border-purple-500/50 rounded-xl pl-9 pr-4 py-2 text-sm text-white placeholder-white/30 outline-none transition-all"
            />
          </div>

          <!-- Category pills scroll -->
          <div class="hidden lg:flex items-center gap-2 shrink-0">
            <button
              v-for="cat in categories"
              :key="cat.name"
              @click="activeCategory = cat.name"
              :class="[
                'px-3 py-1.5 rounded-full text-xs font-semibold transition-all whitespace-nowrap',
                activeCategory === cat.name
                  ? `${cat.activeBg} ${cat.activeText}`
                  : 'text-white/50 hover:text-white/80 hover:bg-white/8'
              ]"
            >
              {{ cat.label }}
            </button>
          </div>
        </div>

        <!-- Mobile categories -->
        <div class="lg:hidden flex gap-2 overflow-x-auto px-4 pb-3 scrollbar-hide">
          <button
            v-for="cat in categories"
            :key="cat.name"
            @click="activeCategory = cat.name"
            :class="[
              'px-3 py-1.5 rounded-full text-xs font-semibold transition-all whitespace-nowrap shrink-0',
              activeCategory === cat.name
                ? `${cat.activeBg} ${cat.activeText}`
                : 'glass border border-white/10 text-white/50'
            ]"
          >{{ cat.label }}</button>
        </div>
      </div>

      <div class="max-w-7xl mx-auto px-4 sm:px-6 py-8">

        <!-- ── HERO FEATURED ARTICLE ── -->
        <div
          v-if="activeCategory === 'Semua' && !searchQuery"
          @click="openResource(featuredArticle)"
          class="relative rounded-3xl overflow-hidden cursor-pointer group mb-10 hover:shadow-[0_0_60px_rgba(16,185,129,0.15)] transition-all duration-500"
        >
          <!-- BG gradient -->
          <div class="absolute inset-0 bg-gradient-to-br from-teal-900/70 via-emerald-900/50 to-[#050b18]"></div>
          <div class="absolute inset-0 bg-gradient-to-r from-[#050b18]/60 via-transparent to-transparent"></div>
          <!-- Decorative orbs -->
          <div class="absolute -top-20 -right-20 w-72 h-72 rounded-full bg-emerald-500/10 blur-[80px]"></div>
          <div class="absolute -bottom-10 right-32 w-48 h-48 rounded-full bg-teal-500/10 blur-[60px]"></div>

          <div class="relative z-10 flex flex-col lg:flex-row items-start lg:items-center gap-8 p-8 lg:p-12">
            <!-- Text side -->
            <div class="flex-1 space-y-4">
              <div class="flex items-center gap-3">
                <span class="px-3 py-1 rounded-full text-xs font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">
                  ✦ ARTIKEL PILIHAN
                </span>
                <span class="text-xs text-white/40">{{ featuredArticle.readTime }} · {{ featuredArticle.author }}</span>
              </div>
              <h2 class="text-2xl sm:text-3xl lg:text-4xl font-black text-white leading-tight group-hover:text-emerald-200 transition-colors">
                {{ featuredArticle.title }}
              </h2>
              <p class="text-white/65 text-sm sm:text-base leading-relaxed max-w-xl">
                {{ featuredArticle.fullDescription }}
              </p>
              <div class="flex items-center gap-4">
                <button class="bg-gradient-to-r from-emerald-500 to-teal-600 text-white text-sm font-bold px-6 py-2.5 rounded-xl flex items-center gap-2 hover:shadow-[0_0_20px_rgba(16,185,129,0.4)] transition-all group-hover:scale-105">
                  Baca Artikel <ArrowRight :size="15" />
                </button>
                <div class="flex items-center gap-1.5 text-xs text-white/40">
                  <Heart :size="13" />
                  <span>{{ featuredArticle.likes }} suka</span>
                </div>
              </div>
            </div>

            <!-- Visual side - decorative card -->
            <div class="shrink-0 w-full lg:w-56 xl:w-72">
              <div class="relative">
                <div class="w-full h-44 lg:h-52 rounded-2xl bg-gradient-to-br from-emerald-500/20 to-teal-600/10 border border-emerald-500/20 flex items-center justify-center backdrop-blur-sm">
                  <span class="text-8xl lg:text-9xl select-none animate-float">{{ featuredArticle.emoji }}</span>
                </div>
                <div class="absolute inset-x-4 -bottom-2 h-4 bg-emerald-500/20 blur-lg rounded-full"></div>
              </div>
            </div>
          </div>
        </div>

        <!-- ── MAIN CONTENT GRID ── -->
        <div class="grid grid-cols-1 xl:grid-cols-4 gap-8">

          <!-- Left: Articles -->
          <div class="xl:col-span-3 space-y-8">

            <!-- Section title -->
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-3">
                <div class="w-1 h-6 rounded-full bg-gradient-to-b from-purple-500 to-cyan-500"></div>
                <h2 class="text-base font-bold text-white">
                  {{ activeCategory === 'Semua' ? 'Semua Artikel' : `Kategori: ${activeCategory}` }}
                  <span class="text-white/30 font-normal text-sm ml-2">({{ filteredResources.length }} artikel)</span>
                </h2>
              </div>
              <div class="flex items-center gap-2">
                <button @click="viewMode = 'grid'" :class="['p-2 rounded-lg transition-all', viewMode === 'grid' ? 'bg-purple-500/20 text-purple-400' : 'text-white/30 hover:text-white/60']">
                  <LayoutGrid :size="16" />
                </button>
                <button @click="viewMode = 'list'" :class="['p-2 rounded-lg transition-all', viewMode === 'list' ? 'bg-purple-500/20 text-purple-400' : 'text-white/30 hover:text-white/60']">
                  <LayoutList :size="16" />
                </button>
              </div>
            </div>

            <!-- GRID VIEW -->
            <div v-if="viewMode === 'grid'" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
              <ArticleCard
                v-for="res in filteredResources"
                :key="res.id"
                :article="res"
                @click="openResource(res)"
              />
            </div>

            <!-- LIST VIEW -->
            <div v-else class="space-y-4">
              <ArticleListItem
                v-for="res in filteredResources"
                :key="res.id"
                :article="res"
                @click="openResource(res)"
              />
            </div>

            <!-- Empty state -->
            <div v-if="filteredResources.length === 0" class="text-center py-20 space-y-4">
              <div class="w-16 h-16 rounded-2xl bg-white/5 flex items-center justify-center mx-auto">
                <SearchX :size="28" class="text-white/20" />
              </div>
              <p class="text-white/50 text-sm">Tidak ada artikel yang cocok dengan pencarianmu.</p>
              <button @click="searchQuery = ''; activeCategory = 'Semua'" class="text-xs text-purple-400 hover:text-purple-300 underline">Reset filter</button>
            </div>
          </div>

          <!-- Right: Sidebar widgets -->
          <div class="space-y-6">

            <!-- Trending topics -->
            <div class="glass rounded-2xl p-5 border border-white/8">
              <h3 class="text-xs font-bold text-white/60 uppercase tracking-widest mb-4 flex items-center gap-2">
                <TrendingUp :size="13" class="text-orange-400" /> Trending Topik
              </h3>
              <div class="space-y-3">
                <button
                  v-for="(topic, i) in trendingTopics"
                  :key="topic"
                  @click="searchQuery = topic"
                  class="w-full text-left flex items-center gap-3 group hover:bg-white/5 rounded-xl p-2 -mx-2 transition-all"
                >
                  <span class="text-xs font-black text-white/20 w-4 shrink-0">{{ String(i + 1).padStart(2, '0') }}</span>
                  <div class="flex-1 min-w-0">
                    <p class="text-sm text-white/80 group-hover:text-white font-medium truncate transition-colors">{{ topic }}</p>
                  </div>
                  <ArrowRight :size="12" class="text-white/20 group-hover:text-purple-400 shrink-0 transition-all group-hover:translate-x-0.5" />
                </button>
              </div>
            </div>

            <!-- Quick tip of the day -->
            <div class="relative rounded-2xl overflow-hidden">
              <div class="absolute inset-0 bg-gradient-to-br from-purple-900/70 to-indigo-900/60"></div>
              <div class="absolute inset-0 bg-gradient-to-t from-[#050b18]/60 to-transparent"></div>
              <div class="relative z-10 p-5">
                <div class="flex items-center gap-2 mb-3">
                  <Sparkles :size="13" class="text-yellow-400" />
                  <span class="text-[10px] font-bold text-yellow-400/80 uppercase tracking-widest">Tips Hari Ini</span>
                </div>
                <p class="text-sm text-white/85 leading-relaxed font-medium italic">"{{ dailyTip.text }}"</p>
                <div class="mt-3 flex items-center gap-2">
                  <div class="w-5 h-5 rounded-full bg-purple-500/30 flex items-center justify-center text-xs">{{ dailyTip.authorEmoji }}</div>
                  <span class="text-[10px] text-white/40">{{ dailyTip.source }}</span>
                </div>
              </div>
            </div>

            <!-- Categories overview -->
            <div class="glass rounded-2xl p-5 border border-white/8">
              <h3 class="text-xs font-bold text-white/60 uppercase tracking-widest mb-4">Jelajahi Topik</h3>
              <div class="grid grid-cols-2 gap-2">
                <button
                  v-for="cat in categories.filter(c => c.name !== 'Semua')"
                  :key="cat.name"
                  @click="activeCategory = cat.name"
                  :class="[
                    'flex flex-col items-center gap-1.5 p-3 rounded-xl border transition-all group cursor-pointer',
                    activeCategory === cat.name
                      ? `${cat.activeBg} border-current`
                      : 'border-white/8 hover:border-white/20 hover:bg-white/5'
                  ]"
                >
                  <span class="text-xl">{{ cat.icon }}</span>
                  <span :class="['text-[10px] font-semibold transition-colors', activeCategory === cat.name ? cat.activeText : 'text-white/50 group-hover:text-white/80']">
                    {{ cat.label }}
                  </span>
                </button>
              </div>
            </div>

            <!-- Helpline CTA -->
            <div class="relative rounded-2xl overflow-hidden border border-red-500/20">
              <div class="absolute inset-0 bg-gradient-to-br from-red-900/30 to-rose-900/20"></div>
              <div class="relative z-10 p-5 space-y-3">
                <div class="flex items-center gap-2">
                  <AlertTriangle :size="15" class="text-red-400" />
                  <span class="text-xs font-bold text-red-400 uppercase tracking-wider">Butuh Bantuan Segera?</span>
                </div>
                <p class="text-xs text-white/65 leading-relaxed">Jika kamu atau seseorang membutuhkan bantuan segera, jangan ragu untuk menghubungi layanan berikut:</p>
                <div class="space-y-2">
                  <div class="bg-white/5 rounded-xl px-3 py-2 text-xs">
                    <p class="text-white/90 font-bold">Into The Light Indonesia</p>
                    <p class="text-white/50">119 ext 8</p>
                  </div>
                  <div class="bg-white/5 rounded-xl px-3 py-2 text-xs">
                    <p class="text-white/90 font-bold">Yayasan Pulih</p>
                    <p class="text-white/50">(021) 788-42580</p>
                  </div>
                </div>
              </div>
            </div>

          </div>
        </div>
      </div>
    </div>

    <!-- ── ARTICLE DETAIL MODAL ── -->
    <Teleport to="body">
      <Transition name="modal">
        <div v-if="selectedResource" class="fixed inset-0 z-50 flex items-center justify-center p-4">
          <div class="absolute inset-0 bg-black/80 backdrop-blur-md" @click="selectedResource = null"></div>
          <div class="relative w-full max-w-2xl max-h-[90vh] overflow-y-auto z-10">
            <!-- Modal card -->
            <div class="glass rounded-3xl overflow-hidden border border-white/10 shadow-2xl">
              <!-- Hero image area -->
              <div :class="['relative h-48 bg-gradient-to-br flex items-center justify-center', selectedResource.thumbnail]">
                <span class="text-8xl select-none animate-float">{{ selectedResource.emoji }}</span>
                <div class="absolute inset-0 bg-gradient-to-t from-[#050b18]/80 to-transparent"></div>
                <!-- Close button -->
                <button
                  @click="selectedResource = null"
                  class="absolute top-4 right-4 w-8 h-8 rounded-full bg-black/40 backdrop-blur-sm text-white/70 hover:text-white flex items-center justify-center transition-all hover:bg-black/60"
                >
                  <X :size="16" />
                </button>
                <!-- Category badge -->
                <div class="absolute bottom-4 left-5">
                  <span :class="['text-xs font-bold px-3 py-1 rounded-full', categoryStyle(selectedResource.category)]">
                    {{ selectedResource.category }}
                  </span>
                </div>
              </div>

              <!-- Content -->
              <div class="p-6 sm:p-8 space-y-5">
                <!-- Meta info -->
                <div class="flex items-center gap-4 text-xs text-white/40 flex-wrap">
                  <div class="flex items-center gap-1.5">
                    <Clock :size="12" />
                    <span>{{ selectedResource.readTime || selectedResource.duration }}</span>
                  </div>
                  <div class="flex items-center gap-1.5">
                    <User :size="12" />
                    <span>{{ selectedResource.author || 'Tim Aether' }}</span>
                  </div>
                  <div class="flex items-center gap-1.5">
                    <Heart :size="12" />
                    <span>{{ selectedResource.likes || 0 }} suka</span>
                  </div>
                </div>

                <h2 class="text-xl sm:text-2xl font-black text-white leading-snug">{{ selectedResource.title }}</h2>

                <!-- Article body -->
                <div class="space-y-4 text-sm text-white/75 leading-relaxed">
                  <p>{{ selectedResource.fullDescription || selectedResource.description }}</p>
                  
                  <!-- Key points -->
                  <div v-if="selectedResource.keyPoints" class="bg-white/4 rounded-xl p-4 border border-white/8 space-y-2">
                    <p class="text-xs font-bold text-purple-300 uppercase tracking-wider mb-3">📌 Poin-Poin Penting</p>
                    <div v-for="pt in selectedResource.keyPoints" :key="pt" class="flex items-start gap-2.5">
                      <span class="text-emerald-400 text-base leading-none mt-0.5">✓</span>
                      <span class="text-white/70 text-xs leading-relaxed">{{ pt }}</span>
                    </div>
                  </div>
                </div>

                <!-- Tags -->
                <div class="flex flex-wrap gap-2">
                  <span
                    v-for="tag in (selectedResource.tags || [])"
                    :key="tag"
                    class="px-2.5 py-1 rounded-full text-[10px] font-semibold bg-white/5 text-white/50 border border-white/8"
                  >#{{ tag }}</span>
                </div>

                <!-- Footer CTA -->
                <div class="flex items-center justify-between pt-2 border-t border-white/8">
                  <div class="flex items-center gap-2 text-xs text-white/40">
                    <BookOpen :size="12" />
                    <span>Baca lengkap dengan Aether Chat</span>
                  </div>
                  <button
                    @click="selectedResource = null"
                    class="text-xs font-semibold px-4 py-2 rounded-xl bg-purple-500/20 text-purple-300 hover:bg-purple-500/30 transition-all border border-purple-500/20"
                  >
                    Tutup
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </Transition>
    </Teleport>
  </div>
</template>

<script setup>
import { ref, computed, defineComponent, h } from 'vue'
import { useRouter } from 'vue-router'
import {
  BookOpen, X, Clock, Search, SearchX, TrendingUp, Sparkles,
  ArrowRight, Heart, LayoutGrid, LayoutList, AlertTriangle, User
} from '@lucide/vue'
import { useAuthStore } from '@/stores/auth'
import Sidebar from '@/components/layout/Sidebar.vue'

const auth = useAuthStore()
const router = useRouter()

const activeCategory = ref('Semua')
const selectedResource = ref(null)
const searchQuery = ref('')
const viewMode = ref('grid')

const categories = [
  { name: 'Semua', label: 'Semua', icon: '🗂️', activeBg: 'bg-white/10', activeText: 'text-white' },
  { name: 'Artikel', label: 'Artikel', icon: '📄', activeBg: 'bg-purple-500/20', activeText: 'text-purple-300' },
  { name: 'Self-Care', label: 'Self-Care', icon: '💆', activeBg: 'bg-pink-500/20', activeText: 'text-pink-300' },
  { name: 'Meditasi', label: 'Meditasi', icon: '🧘', activeBg: 'bg-emerald-500/20', activeText: 'text-emerald-300' },
  { name: 'Breathing', label: 'Pernapasan', icon: '🌬️', activeBg: 'bg-blue-500/20', activeText: 'text-blue-300' },
  { name: 'CBT', label: 'Tips CBT', icon: '🧠', activeBg: 'bg-yellow-500/20', activeText: 'text-yellow-300' },
  { name: 'Akademik', label: 'Akademik', icon: '🎓', activeBg: 'bg-orange-500/20', activeText: 'text-orange-300' },
]

const trendingTopics = [
  'Cara Mengatasi Burnout Kuliah',
  'Teknik Pernapasan Anti Panik',
  'Tidur Berkualitas untuk Mahasiswa',
  'Cara Berbicara Soal Mental Health',
  'Journaling Terapeutik Harian',
]

const dailyTips = [
  { text: 'Kamu tidak harus produktif setiap saat. Istirahat juga bagian dari proses.', source: 'Aether Mental Tips', authorEmoji: '💜' },
  { text: 'Perasaanmu valid. Kamu tidak harus menjelaskan dirimu pada semua orang.', source: 'Psychology Today', authorEmoji: '🧠' },
  { text: 'Ambil napas dalam 4 detik, tahan 4 detik, hembuskan 4 detik. Ulangi.', source: 'Box Breathing Technique', authorEmoji: '🌬️' },
  { text: 'Satu langkah kecil hari ini lebih baik dari tidak sama sekali.', source: 'CBT Principle', authorEmoji: '✨' },
]
const dailyTip = dailyTips[new Date().getDay() % dailyTips.length]

const resources = [
  {
    id: 1, title: 'Mengenali Tanda-tanda Burnout Akademik Sebelum Terlambat',
    description: 'Burnout bukan hanya kelelahan biasa. Pelajari tanda-tanda awal dan cara mengatasinya.',
    category: 'Artikel', readTime: '7 menit baca', author: 'dr. Aether AI', emoji: '📚',
    thumbnail: 'from-purple-900/70 to-indigo-900/60', likes: 248,
    tags: ['burnout', 'akademik', 'stres', 'mahasiswa'],
    fullDescription: 'Burnout akademik adalah kondisi kelelahan fisik, mental, dan emosional yang disebabkan oleh tekanan akademis yang berkepanjangan. Gejalanya meliputi kehilangan motivasi belajar, sering sakit kepala, sulit berkonsentrasi, dan perasaan tidak berguna. Penelitian menunjukkan 67% mahasiswa mengalami burnout setidaknya sekali dalam setahun.',
    keyPoints: [
      'Burnout berbeda dengan kelelahan biasa — berlangsung berminggu-minggu',
      'Tanda awal: tidak bisa menikmati hal yang dulu kamu suka',
      'Jalan keluar: atur ulang prioritas, bicara ke konselor, ambil jeda terstruktur',
      'Tidur 7-8 jam adalah salah satu "obat" terbaik untuk burnout',
    ],
  },
  {
    id: 2, title: 'Teknik Pernapasan 4-7-8: Matikan Mode Panik dalam 5 Menit',
    description: 'Latihan napas sederhana yang terbukti secara ilmiah meredakan kecemasan akut.',
    category: 'Breathing', readTime: '5 menit baca', author: 'Tim Aether', emoji: '🌬️',
    thumbnail: 'from-blue-900/70 to-cyan-900/60', likes: 312,
    tags: ['pernapasan', 'kecemasan', 'relaksasi'],
    fullDescription: 'Teknik 4-7-8 dikembangkan oleh Dr. Andrew Weil, dan merupakan salah satu cara tercepat untuk menstabilkan sistem saraf. Caranya: tarik napas 4 detik → tahan 7 detik → hembuskan perlahan 8 detik. Ulangi 4 kali. Efeknya terasa dalam hitungan menit.',
    keyPoints: [
      'Aktifkan sistem saraf parasimpatis yang menenangkan',
      'Efektif untuk serangan panik, kecemasan ujian, atau insomnia',
      'Bisa dilakukan di mana saja — bahkan di toilet kampus',
      'Lakukan 4 siklus untuk hasil optimal',
    ],
  },
  {
    id: 3, title: 'Meditasi Pagi 10 Menit: Mulai Hari dengan Tenang dan Fokus',
    description: 'Panduan meditasi sederhana yang bisa dilakukan setelah bangun tidur.',
    category: 'Meditasi', readTime: '10 menit', author: 'Mindful Aether', emoji: '🧘',
    thumbnail: 'from-emerald-900/70 to-teal-900/60', likes: 189,
    tags: ['meditasi', 'mindfulness', 'pagi', 'fokus'],
    fullDescription: 'Cukup 10 menit meditasi setiap pagi dapat meningkatkan fokus, menurunkan kortisol (hormon stres), dan membuat kamu lebih siap menghadapi tantangan hari ini. Duduklah nyaman, tutup mata, dan fokuskan perhatian pada napas. Saat pikiran mengembara, kembalikan dengan lembut.',
    keyPoints: [
      'Tidak perlu pengalaman — cukup duduk dan bernapas',
      'Lakukan segera setelah bangun sebelum memegang HP',
      'Konsisten 21 hari untuk melihat perubahan signifikan',
      'Gunakan timer agar tidak was-was soal waktu',
    ],
  },
  {
    id: 4, title: 'Menghadapi Dosen Galak dan Situasi Akademik yang Menekan',
    description: 'Strategi komunikasi efektif untuk menghadapi tekanan dari lingkungan akademik.',
    category: 'Akademik', readTime: '6 menit baca', author: 'Tim Konselor', emoji: '🎓',
    thumbnail: 'from-orange-900/70 to-amber-900/60', likes: 156,
    tags: ['akademik', 'komunikasi', 'stres', 'dosen'],
    fullDescription: 'Tekanan dari lingkungan akademik — termasuk dosen yang menakutkan — adalah salah satu pemicu stres terbesar mahasiswa. Kuncinya adalah memisahkan antara gaya komunikasi dosen dengan kualitas dirimu sebagai mahasiswa. Kamu bisa mempersiapkan diri, membawa teman, atau berbicara di saat yang tepat.',
    keyPoints: [
      'Persiapkan pertanyaan sebelum menemui dosen',
      'Berbicara dengan suara tenang dan kontak mata',
      'Ingat: kamu berhak mendapat penjelasan yang layak',
      'Minta bantuan kakak angkatan atau konselor jika perlu',
    ],
  },
  {
    id: 5, title: 'Body Scan: Teknik Meditasi untuk Tidur Nyenyak Malam Ini',
    description: 'Panduan body scan 15 menit sebelum tidur untuk mengusir pikiran yang berputar.',
    category: 'Meditasi', readTime: '15 menit', author: 'Mindful Aether', emoji: '🌙',
    thumbnail: 'from-indigo-900/70 to-purple-900/60', likes: 203,
    tags: ['meditasi', 'tidur', 'insomnia', 'relaksasi'],
    fullDescription: 'Body scan adalah teknik memindai tubuh dari ujung kepala hingga kaki, menyadari setiap sensasi tanpa menghakimi. Ini sangat efektif untuk mahasiswa yang pikiran kerjanya tidak bisa berhenti. Dengan body scan, kamu "memindahkan" perhatian dari pikiran ke tubuh fisik, yang membuat otak lebih mudah beristirahat.',
    keyPoints: [
      'Berbaring nyaman di tempat tidur',
      'Mulai dari ubun-ubun, turun ke dahi, wajah, leher...',
      'Perhatikan sensasi — hangat, tegang, santai',
      'Jangan paksa tidur — cukup biarkan tubuh rileks',
    ],
  },
  {
    id: 6, title: 'Self-Care Bukan Sekadar Skincare: Panduan Lengkap Merawat Diri',
    description: 'Makna sejati self-care yang jauh lebih dalam dari sekadar "me time" di sosmed.',
    category: 'Self-Care', readTime: '8 menit baca', author: 'Tim Aether', emoji: '💆',
    thumbnail: 'from-pink-900/70 to-rose-900/60', likes: 294,
    tags: ['self-care', 'kesehatan', 'wellness', 'mental'],
    fullDescription: 'Self-care bukan hanya mandi air hangat atau beli es krim. Self-care sejati mencakup menjaga pola tidur, membatasi toxic relationships, berkata "tidak" pada hal yang menguras energi, dan memenuhi kebutuhan emosional diri sendiri. Ini adalah kebutuhan dasar, bukan kemewahan.',
    keyPoints: [
      'Physical: tidur cukup, makan bergizi, olahraga ringan',
      'Emotional: izinkan diri merasakan emosi tanpa menghakimi',
      'Social: jaga koneksi dengan orang yang mendukungmu',
      'Digital: detoks dari media sosial secara berkala',
    ],
  },
  {
    id: 7, title: 'Journaling Terapeutik: Cara Melepas Beban yang Terpendam',
    description: 'Teknik journaling yang direkomendasikan psikolog untuk mahasiswa aktif.',
    category: 'CBT', readTime: '5 menit baca', author: 'Tim Konselor', emoji: '✍️',
    thumbnail: 'from-yellow-900/70 to-amber-900/60', likes: 178,
    tags: ['journaling', 'CBT', 'menulis', 'refleksi'],
    fullDescription: 'Journaling terapeutik berbeda dengan diary biasa. Teknik ini menggunakan panduan pertanyaan reflektif untuk membantu kamu memahami pola pikir dan perasaan. Beberapa teknik populer: Gratitude Journaling, Stream of Consciousness, dan CBT Thought Record. Cukup 10 menit sebelum tidur.',
    keyPoints: [
      'Tulis 3 hal yang kamu syukuri setiap malam',
      'Tuliskan pikiran negatif → tantang dengan bukti nyata',
      'Jangan edit tulisanmu — biarkan mengalir bebas',
      'Konsisten lebih penting daripada panjang tulisan',
    ],
  },
  {
    id: 8, title: 'Box Breathing: Teknik Pernapasan Tentara untuk Mahasiswa Stres',
    description: 'Teknik pernapasan kotak yang digunakan Navy SEAL untuk tetap tenang di bawah tekanan.',
    category: 'Breathing', readTime: '3 menit baca', author: 'Tim Aether', emoji: '⬜',
    thumbnail: 'from-sky-900/70 to-blue-900/60', likes: 267,
    tags: ['pernapasan', 'stres', 'fokus', 'kecemasan'],
    fullDescription: 'Box breathing (pernapasan kotak) adalah teknik 4 langkah: tarik napas 4 detik → tahan 4 detik → hembuskan 4 detik → tahan 4 detik. Siklus ini membentuk "kotak". Teknik ini digunakan oleh pasukan elit untuk tetap fokus dan tenang dalam situasi stres ekstrem. Kamu bisa menggunakannya sebelum ujian, presentasi, atau saat kecemasan datang.',
    keyPoints: [
      'Lakukan 4-6 siklus untuk hasil maksimal',
      'Efektif dalam 5 menit pertama',
      'Bisa dilakukan sambil duduk, berdiri, bahkan berjalan',
      'Gabungkan dengan visualisasi positif untuk efek lebih kuat',
    ],
  },
  {
    id: 9, title: 'Mengenal Cognitive Behavioral Therapy (CBT) dan Bagaimana Ini Bisa Membantumu',
    description: 'Pengenalan ringan soal terapi kognitif perilaku yang bisa dipraktikkan sendiri.',
    category: 'CBT', readTime: '9 menit baca', author: 'dr. Aether AI', emoji: '🧠',
    thumbnail: 'from-violet-900/70 to-purple-900/60', likes: 321,
    tags: ['CBT', 'terapi', 'pikiran', 'perilaku'],
    fullDescription: 'CBT adalah salah satu pendekatan terapi psikologis yang paling terbukti efektif, terutama untuk kecemasan dan depresi. Inti dari CBT adalah: pikiran → perasaan → perilaku. Dengan mengubah cara berpikir, kamu bisa mengubah perasaan dan perilakumu. Chatbot Aether dirancang dengan prinsip-prinsip CBT untuk memberikan respons yang empatik dan konstruktif.',
    keyPoints: [
      'Identifikasi "pikiran otomatis negatif" yang muncul',
      'Tanya: Apakah ada bukti yang mendukung pikiran ini?',
      'Ganti dengan pikiran yang lebih seimbang dan realistis',
      'CBT bisa dipelajari sendiri, tapi lebih optimal dengan konselor',
    ],
  },
]

const featuredArticle = resources[8] // CBT article as featured

const filteredResources = computed(() => {
  let list = resources.filter(r => r.id !== featuredArticle.id || activeCategory.value !== 'Semua')
  if (activeCategory.value !== 'Semua') {
    list = resources.filter(r => r.category === activeCategory.value)
  }
  if (searchQuery.value) {
    const q = searchQuery.value.toLowerCase()
    list = list.filter(r =>
      r.title.toLowerCase().includes(q) ||
      r.description.toLowerCase().includes(q) ||
      (r.tags || []).some(t => t.includes(q))
    )
  }
  return list
})

function categoryStyle(cat) {
  const map = {
    Artikel: 'bg-purple-500/20 text-purple-300 border border-purple-500/30',
    'Self-Care': 'bg-pink-500/20 text-pink-300 border border-pink-500/30',
    Meditasi: 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/30',
    Breathing: 'bg-blue-500/20 text-blue-300 border border-blue-500/30',
    CBT: 'bg-yellow-500/20 text-yellow-300 border border-yellow-500/30',
    Akademik: 'bg-orange-500/20 text-orange-300 border border-orange-500/30',
  }
  return map[cat] || map.Artikel
}

function openResource(res) { selectedResource.value = res }
function handleLogout() { auth.logout(); router.push('/') }
</script>

<!-- Inline sub-components -->
<script>
import { defineComponent, h } from 'vue'
import { Clock, Heart, ArrowRight, BookOpen, User } from '@lucide/vue'

const categoryColors = {
  Artikel: 'bg-purple-500/20 text-purple-300',
  'Self-Care': 'bg-pink-500/20 text-pink-300',
  Meditasi: 'bg-emerald-500/20 text-emerald-300',
  Breathing: 'bg-blue-500/20 text-blue-300',
  CBT: 'bg-yellow-500/20 text-yellow-300',
  Akademik: 'bg-orange-500/20 text-orange-300',
}

// Grid card component
export const ArticleCard = defineComponent({
  name: 'ArticleCard',
  props: { article: Object },
  emits: ['click'],
  setup(props, { emit }) {
    return () => h('div', {
      class: 'glass rounded-2xl overflow-hidden border border-white/8 group cursor-pointer hover:border-white/20 hover:-translate-y-1 transition-all duration-300 hover:shadow-[0_8px_30px_rgba(0,0,0,0.4)] flex flex-col',
      onClick: () => emit('click')
    }, [
      // Thumbnail
      h('div', { class: `relative h-36 bg-gradient-to-br overflow-hidden ${props.article.thumbnail}` }, [
        h('div', { class: 'absolute inset-0 flex items-center justify-center text-5xl group-hover:scale-110 transition-transform duration-500 select-none' }, props.article.emoji),
        h('div', { class: 'absolute inset-0 bg-gradient-to-t from-black/50 to-transparent' }),
        h('span', { class: `absolute top-3 left-3 text-[10px] font-bold px-2 py-0.5 rounded-full ${categoryColors[props.article.category] || categoryColors.Artikel}` }, props.article.category),
        h('div', { class: 'absolute bottom-2 right-2 flex items-center gap-1 text-[10px] text-white/60' }, [
          h(Heart, { size: 10 }), h('span', {}, props.article.likes)
        ])
      ]),
      // Body
      h('div', { class: 'p-4 flex flex-col flex-1' }, [
        h('h3', { class: 'text-sm font-bold text-white group-hover:text-purple-300 transition-colors line-clamp-2 mb-1.5' }, props.article.title),
        h('p', { class: 'text-[11px] text-white/50 leading-relaxed line-clamp-2 flex-1' }, props.article.description),
        h('div', { class: 'flex items-center justify-between mt-3 pt-3 border-t border-white/5' }, [
          h('div', { class: 'flex items-center gap-1.5 text-[10px] text-white/35' }, [
            h(Clock, { size: 10 }), h('span', {}, props.article.readTime)
          ]),
          h('div', { class: 'flex items-center gap-1 text-[10px] text-purple-400/70 group-hover:text-purple-300 transition-colors font-semibold' }, [
            'Baca', h(ArrowRight, { size: 10, class: 'group-hover:translate-x-0.5 transition-transform' })
          ])
        ])
      ])
    ])
  }
})

// List item component
export const ArticleListItem = defineComponent({
  name: 'ArticleListItem',
  props: { article: Object },
  emits: ['click'],
  setup(props, { emit }) {
    return () => h('div', {
      class: 'glass rounded-xl border border-white/8 p-4 flex items-center gap-4 group cursor-pointer hover:border-white/20 hover:bg-white/5 transition-all duration-300',
      onClick: () => emit('click')
    }, [
      // Emoji thumb
      h('div', { class: `w-14 h-14 rounded-xl bg-gradient-to-br ${props.article.thumbnail} flex items-center justify-center text-2xl shrink-0 group-hover:scale-105 transition-transform` }, props.article.emoji),
      // Content
      h('div', { class: 'flex-1 min-w-0' }, [
        h('div', { class: 'flex items-center gap-2 mb-1' }, [
          h('span', { class: `text-[10px] font-bold px-2 py-0.5 rounded-full ${categoryColors[props.article.category] || categoryColors.Artikel}` }, props.article.category),
          h('span', { class: 'text-[10px] text-white/30' }, props.article.readTime)
        ]),
        h('h3', { class: 'text-sm font-bold text-white group-hover:text-purple-300 transition-colors line-clamp-1' }, props.article.title),
        h('p', { class: 'text-[11px] text-white/50 line-clamp-1 mt-0.5' }, props.article.description)
      ]),
      // Arrow
      h('div', { class: 'shrink-0 text-white/20 group-hover:text-purple-400 transition-all group-hover:translate-x-1' }, [h(ArrowRight, { size: 16 })])
    ])
  }
})
</script>

<style scoped>
.modal-enter-active, .modal-leave-active { transition: all 0.3s ease; }
.modal-enter-from, .modal-leave-to { opacity: 0; transform: scale(0.96); }
.scrollbar-hide { scrollbar-width: none; }
.scrollbar-hide::-webkit-scrollbar { display: none; }
</style>
