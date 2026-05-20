<template>
  <div class="min-h-screen bg-[#050b18] flex">
    <Sidebar :sessions="[]" :show-history="false" @logout="handleLogout" />

    <div class="flex-1 md:ml-64 overflow-y-auto">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 py-8">
        <!-- Header -->
        <div class="mb-8">
          <h1 class="text-2xl font-bold text-white mb-1">Resource <span class="gradient-text">Center</span></h1>
          <p class="text-sm text-white/50">Artikel, video, dan latihan untuk kesehatan mentalmu</p>
        </div>

        <!-- Category filter -->
        <div class="flex flex-wrap gap-2 mb-8">
          <button v-for="cat in categories" :key="cat"
            @click="activeCategory = cat"
            :class="[
              'px-4 py-2 rounded-xl text-sm font-medium transition-all duration-200',
              activeCategory === cat
                ? 'bg-purple-500/30 text-purple-300 border border-purple-500/50'
                : 'glass border border-white/10 text-white/50 hover:text-white/80 hover:border-white/20'
            ]">
            {{ cat }}
          </button>
        </div>

        <!-- Resources Grid -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-5">
          <ResourceCard
            v-for="res in filteredResources"
            :key="res.id"
            v-bind="res"
            @click="openResource(res)"
          />
        </div>

        <!-- Empty state -->
        <div v-if="filteredResources.length === 0" class="text-center py-20">
          <BookOpen :size="48" class="text-white/15 mx-auto mb-4" />
          <p class="text-white/40">Tidak ada resource dalam kategori ini</p>
        </div>
      </div>
    </div>

    <!-- Resource Modal -->
    <Teleport to="body">
      <Transition name="modal">
        <div v-if="selectedResource" class="fixed inset-0 z-50 flex items-center justify-center p-4">
          <div class="absolute inset-0 bg-black/70 backdrop-blur-sm" @click="selectedResource = null"></div>
          <div class="relative glass gradient-border rounded-3xl p-8 max-w-lg w-full z-10">
            <button @click="selectedResource = null" class="absolute top-4 right-4 text-white/40 hover:text-white transition-colors">
              <X :size="20" />
            </button>
            <div class="text-5xl mb-4">{{ selectedResource.emoji }}</div>
            <span :class="['text-xs font-semibold px-2.5 py-1 rounded-full mb-3 inline-block', selectedResource.categoryStyle]">{{ selectedResource.category }}</span>
            <h2 class="text-xl font-bold text-white mb-3">{{ selectedResource.title }}</h2>
            <p class="text-sm text-white/60 leading-relaxed mb-6">{{ selectedResource.fullDescription || selectedResource.description }}</p>
            <div class="flex items-center gap-3 text-xs text-white/40">
              <Clock :size="13" /> {{ selectedResource.duration }}
            </div>
          </div>
        </div>
      </Transition>
    </Teleport>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { BookOpen, X, Clock } from '@lucide/vue'
import { useAuthStore } from '@/stores/auth'
import Sidebar from '@/components/layout/Sidebar.vue'
import ResourceCard from '@/components/ui/ResourceCard.vue'

const auth = useAuthStore()
const router = useRouter()

const activeCategory = ref('Semua')
const selectedResource = ref(null)
const categories = ['Semua', 'Artikel', 'Video', 'Meditasi', 'Breathing', 'Tips']

const resources = [
  { id:1, title: 'Mengenali Tanda-tanda Burnout Akademik', description: 'Burnout bukan hanya kelelahan biasa. Pelajari tanda-tanda awal dan cara mengatasinya sebelum makin parah.', category: 'Artikel', duration: '7 menit', emoji: '📚', thumbnail: 'from-purple-900/60 to-indigo-900/60', fullDescription: 'Burnout akademik adalah kondisi kelelahan fisik, mental, dan emosional yang disebabkan oleh tekanan akademis yang berkepanjangan. Tanda-tandanya meliputi: kehilangan motivasi belajar, sering sakit, sulit berkonsentrasi, dan merasa tidak berguna. Kunci mengatasi burnout adalah: istirahat terstruktur, bicara dengan orang terpercaya, dan atur ulang ekspektasi diri.' },
  { id:2, title: 'Teknik Pernapasan 4-7-8 untuk Meredakan Stres', description: 'Latihan napas sederhana yang terbukti secara ilmiah meredakan kecemasan dalam 5 menit.', category: 'Breathing', duration: '5 menit', emoji: '🌬️', thumbnail: 'from-blue-900/60 to-cyan-900/60' },
  { id:3, title: 'Meditasi Pagi: Memulai Hari dengan Tenang', description: 'Panduan meditasi 10 menit untuk memulai hari dengan pikiran jernih dan penuh energi positif.', category: 'Meditasi', duration: '10 menit', emoji: '🧘', thumbnail: 'from-emerald-900/60 to-teal-900/60' },
  { id:4, title: 'Cara Berbicara dengan Dosen yang Menakutkan', description: 'Strategi komunikasi efektif untuk menghadapi dosen galak tanpa kehilangan kepercayaan diri.', category: 'Tips', duration: '6 menit', emoji: '🎓', thumbnail: 'from-orange-900/60 to-amber-900/60' },
  { id:5, title: 'Body Scan Meditation untuk Tidur Lebih Nyenyak', description: 'Teknik meditasi body scan 15 menit yang membantu tubuh dan pikiran rileks sebelum tidur.', category: 'Meditasi', duration: '15 menit', emoji: '🌙', thumbnail: 'from-indigo-900/60 to-purple-900/60' },
  { id:6, title: 'Video: Mindfulness untuk Mahasiswa Sibuk', description: 'Panduan mindfulness praktis yang bisa dilakukan di sela jadwal kuliah yang padat.', category: 'Video', duration: '12 menit', emoji: '🎥', thumbnail: 'from-pink-900/60 to-rose-900/60' },
  { id:7, title: 'Journaling: Cara Efektif Melepas Beban', description: 'Menulis jurnal bukan sekadar diary. Temukan teknik journaling terapeutik yang mudah dan powerful.', category: 'Tips', duration: '5 menit', emoji: '✍️', thumbnail: 'from-yellow-900/60 to-amber-900/60' },
  { id:8, title: 'Breathing Exercise: Box Breathing Technique', description: 'Teknik pernapasan kotak yang digunakan tentara dan atlet untuk mengelola tekanan tinggi.', category: 'Breathing', duration: '3 menit', emoji: '⬜', thumbnail: 'from-sky-900/60 to-blue-900/60' },
]

const filteredResources = computed(() =>
  activeCategory.value === 'Semua'
    ? resources
    : resources.filter(r => r.category === activeCategory.value)
)

function openResource(res) { selectedResource.value = res }
function handleLogout() { auth.logout(); router.push('/') }
</script>

<style scoped>
.modal-enter-active, .modal-leave-active { transition: all 0.3s ease; }
.modal-enter-from, .modal-leave-to { opacity: 0; transform: scale(0.95); }
</style>
