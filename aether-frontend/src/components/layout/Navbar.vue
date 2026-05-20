<template>
  <nav
    :class="[
      'fixed top-0 left-0 right-0 z-50 transition-all duration-500',
      scrolled ? 'glass border-b border-white/8 py-3' : 'py-5 bg-transparent'
    ]"
  >
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between">
      <!-- Logo -->
      <router-link to="/" class="flex items-center gap-3 group">
        <div class="relative">
          <div class="w-9 h-9 rounded-xl bg-gradient-to-br from-purple-600 to-cyan-500 flex items-center justify-center shadow-lg group-hover:scale-110 transition-transform">
            <span class="text-white font-black text-lg">Æ</span>
          </div>
          <div class="absolute inset-0 rounded-xl bg-gradient-to-br from-purple-600 to-cyan-500 blur-md opacity-50 group-hover:opacity-80 transition-opacity"></div>
        </div>
        <span class="font-bold text-xl tracking-tight">
          <span class="gradient-text">Aether</span>
        </span>
      </router-link>

      <!-- Desktop Nav -->
      <div class="hidden md:flex items-center gap-8">
        <a href="#features" class="text-sm text-white/70 hover:text-white transition-colors duration-200 font-medium">Fitur</a>
        <a href="#how-it-works" class="text-sm text-white/70 hover:text-white transition-colors duration-200 font-medium">Cara Kerja</a>
        <a href="#emotion" class="text-sm text-white/70 hover:text-white transition-colors duration-200 font-medium">Klasifikasi</a>
      </div>

      <!-- CTA -->
      <div class="hidden md:flex items-center gap-3">
        <router-link to="/login" class="text-sm text-white/70 hover:text-white transition-colors px-4 py-2 font-medium">
          Masuk
        </router-link>
        <router-link
          to="/register"
          class="btn-glow text-white text-sm font-semibold px-5 py-2.5 rounded-xl"
        >
          Mulai Gratis
        </router-link>
      </div>

      <!-- Mobile Menu Toggle -->
      <button
        @click="mobileOpen = !mobileOpen"
        class="md:hidden p-2 rounded-lg text-white/70 hover:text-white hover:bg-white/10 transition-all"
        aria-label="Toggle menu"
      >
        <component :is="mobileOpen ? X : Menu" :size="22" />
      </button>
    </div>

    <!-- Mobile Drawer -->
    <transition name="mobile-menu">
      <div v-if="mobileOpen" class="md:hidden glass border-t border-white/8 mt-1">
        <div class="px-4 py-4 flex flex-col gap-3">
          <a href="#features" @click="mobileOpen = false" class="text-white/80 hover:text-white py-2 text-sm font-medium">Fitur</a>
          <a href="#how-it-works" @click="mobileOpen = false" class="text-white/80 hover:text-white py-2 text-sm font-medium">Cara Kerja</a>
          <a href="#emotion" @click="mobileOpen = false" class="text-white/80 hover:text-white py-2 text-sm font-medium">Klasifikasi</a>
          <hr class="border-white/10 my-1" />
          <router-link to="/login" class="text-white/80 hover:text-white py-2 text-sm font-medium">Masuk</router-link>
          <router-link to="/register" class="btn-glow text-white text-sm font-semibold px-4 py-2.5 rounded-xl text-center">
            Mulai Gratis
          </router-link>
        </div>
      </div>
    </transition>
  </nav>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { Menu, X } from '@lucide/vue'

const scrolled = ref(false)
const mobileOpen = ref(false)

function onScroll() { scrolled.value = window.scrollY > 20 }
onMounted(() => window.addEventListener('scroll', onScroll))
onUnmounted(() => window.removeEventListener('scroll', onScroll))
</script>

<style scoped>
.mobile-menu-enter-active, .mobile-menu-leave-active { transition: all 0.3s ease; }
.mobile-menu-enter-from, .mobile-menu-leave-to { opacity: 0; transform: translateY(-10px); }
</style>
