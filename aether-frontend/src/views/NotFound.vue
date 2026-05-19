<template>
  <div class="min-h-screen bg-[#050b18] flex items-center justify-center px-4">
    <div class="text-center z-10">
      <div class="text-8xl mb-6">🌌</div>
      <h1 class="text-5xl font-black gradient-text mb-4">404</h1>
      <p class="text-white/60 text-lg mb-8">Halaman yang kamu cari tidak ditemukan</p>
      <router-link to="/" class="btn-glow text-white font-bold px-8 py-3.5 rounded-2xl inline-flex items-center gap-2">
        <Home :size="18" /> Kembali ke Beranda
      </router-link>
    </div>
    <div class="fixed inset-0 pointer-events-none">
      <div class="absolute top-1/4 left-1/4 w-72 h-72 rounded-full bg-purple-700/20 blur-[120px] animate-float"></div>
      <div class="absolute bottom-1/4 right-1/4 w-72 h-72 rounded-full bg-cyan-600/15 blur-[100px] animate-float2"></div>
    </div>
  </div>
</template>

<script setup>
import { Home } from '@lucide/vue'
</script>
