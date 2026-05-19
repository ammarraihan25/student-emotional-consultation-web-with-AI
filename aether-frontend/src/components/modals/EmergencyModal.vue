<template>
  <Teleport to="body">
    <Transition name="modal">
      <div v-if="show" class="fixed inset-0 z-50 flex items-center justify-center p-4">
        <!-- Backdrop -->
        <div class="absolute inset-0 bg-black/70 backdrop-blur-sm" @click="$emit('close')"></div>

        <!-- Modal Card -->
        <div class="relative w-full max-w-md glass rounded-3xl border border-red-500/30 overflow-hidden animate-pulse-glow-red">
          <!-- Top glow bar -->
          <div class="h-1 w-full bg-gradient-to-r from-red-600 via-red-400 to-orange-400"></div>

          <div class="p-8">
            <!-- Header -->
            <div class="flex flex-col items-center text-center mb-6">
              <div class="w-20 h-20 rounded-full bg-red-500/20 border-2 border-red-500/40 flex items-center justify-center mb-4 animate-pulse">
                <AlertTriangle :size="36" class="text-red-400" />
              </div>
              <h2 class="text-2xl font-bold text-white mb-2">Kamu Tidak Sendirian</h2>
              <p class="text-sm text-white/60 leading-relaxed">
                Sistem mendeteksi kamu mungkin membutuhkan dukungan segera. Kami peduli dengan kondisimu.
              </p>
            </div>

            <!-- Crisis resources -->
            <div class="space-y-3 mb-6">
              <p class="text-xs text-white/40 uppercase tracking-wider font-medium">Hubungi Segera:</p>
              <a v-for="hotline in hotlines" :key="hotline.name"
                :href="hotline.href"
                class="flex items-center gap-3 glass-hover rounded-xl p-3 border border-white/10 group"
              >
                <div :class="['w-10 h-10 rounded-lg flex items-center justify-center shrink-0', hotline.bg]">
                  <component :is="hotline.icon" :size="18" :class="hotline.iconColor" />
                </div>
                <div>
                  <p class="text-sm font-semibold text-white">{{ hotline.name }}</p>
                  <p class="text-xs text-white/50">{{ hotline.number }}</p>
                </div>
                <ExternalLink :size="14" class="ml-auto text-white/20 group-hover:text-white/50 transition-colors" />
              </a>
            </div>

            <!-- Breathing exercise -->
            <div class="glass rounded-2xl p-4 border border-blue-500/20 mb-6">
              <div class="flex items-center gap-2 mb-2">
                <Wind :size="16" class="text-blue-400" />
                <span class="text-sm font-medium text-blue-300">Latihan Napas Cepat</span>
              </div>
              <p class="text-xs text-white/50 leading-relaxed">
                Tarik napas 4 detik → Tahan 7 detik → Hembuskan 8 detik. Ulangi 3x.
              </p>
            </div>

            <!-- Actions -->
            <div class="flex gap-3">
              <button
                @click="$emit('close')"
                class="flex-1 py-3 rounded-xl text-sm font-medium text-white/60 border border-white/15 hover:bg-white/5 transition-all"
              >
                Kembali ke Chat
              </button>
              <a
                href="tel:119"
                class="flex-1 py-3 rounded-xl text-sm font-bold text-white text-center bg-gradient-to-r from-red-600 to-red-500 hover:from-red-500 hover:to-red-400 transition-all shadow-[0_0_20px_rgba(239,68,68,0.4)]"
              >
                Hubungi 119
              </a>
            </div>
          </div>
        </div>
      </div>
    </Transition>
  </Teleport>
</template>

<script setup>
import { AlertTriangle, Phone, Heart, Wind, ExternalLink } from '@lucide/vue'

defineProps({ show: { type: Boolean, default: false } })
defineEmits(['close'])

const hotlines = [
  { name: 'Into The Light', number: '119 ext 8 (24 jam)', href: 'tel:119', bg: 'bg-red-500/15', icon: Phone, iconColor: 'text-red-400' },
  { name: 'Yayasan Pulih', number: '(021) 788-42580', href: 'tel:02178842580', bg: 'bg-purple-500/15', icon: Heart, iconColor: 'text-purple-400' },
  { name: 'Konselor Kampus', number: 'Hubungi BK / Psikolog', href: '#', bg: 'bg-blue-500/15', icon: Heart, iconColor: 'text-blue-400' },
]
</script>

<style scoped>
.modal-enter-active, .modal-leave-active { transition: all 0.3s ease; }
.modal-enter-from, .modal-leave-to { opacity: 0; transform: scale(0.95); }
</style>
