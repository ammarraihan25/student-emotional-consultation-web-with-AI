<template>
  <aside
    :class="[
      'fixed left-0 top-0 h-full z-40 flex flex-col transition-all duration-300',
      'glass border-r border-white/8',
      collapsed ? 'w-16' : 'w-64',
      mobileOpen ? 'translate-x-0' : '-translate-x-full md:translate-x-0'
    ]"
  >
    <!-- Logo -->
    <div class="flex items-center gap-3 px-4 py-5 border-b border-white/8">
      <div class="relative shrink-0">
        <div class="w-8 h-8 rounded-lg bg-gradient-to-br from-purple-600 to-cyan-500 flex items-center justify-center">
          <span class="text-white font-black text-sm">Æ</span>
        </div>
        <div class="absolute inset-0 rounded-lg bg-gradient-to-br from-purple-600 to-cyan-500 blur-sm opacity-50"></div>
      </div>
      <span v-if="!collapsed" class="font-bold text-lg gradient-text">Aether</span>
      <button
        @click="collapsed = !collapsed"
        class="ml-auto text-white/40 hover:text-white/80 transition-colors hidden md:block"
      >
        <component :is="collapsed ? ChevronRight : ChevronLeft" :size="16" />
      </button>
    </div>

    <!-- New Chat -->
    <div class="px-3 pt-4 pb-2">
      <button
        @click="$emit('new-chat')"
        :class="[
          'w-full flex items-center gap-3 px-3 py-2.5 rounded-xl transition-all duration-200',
          'bg-gradient-to-r from-purple-600/20 to-cyan-500/10 border border-purple-500/30',
          'hover:border-purple-500/60 hover:from-purple-600/30 group',
          collapsed ? 'justify-center' : ''
        ]"
      >
        <SquarePen :size="17" class="text-purple-400 shrink-0 group-hover:scale-110 transition-transform" />
        <span v-if="!collapsed" class="text-sm font-medium text-white/90">New Chat</span>
      </button>
    </div>

    <!-- Navigation -->
    <nav class="flex-1 px-3 py-2 overflow-y-auto">
      <!-- Menu items -->
      <div class="space-y-1 mb-4">
        <SidebarItem v-for="item in navItems" :key="item.name"
          :icon="item.icon" :label="item.label" :to="item.to"
          :collapsed="collapsed" :active="$route.name === item.name"
        />
      </div>

      <!-- Recent Sessions (only in chat) -->
      <div v-if="!collapsed && showHistory" class="mt-4">
        <p class="text-xs text-white/30 font-medium px-3 mb-2 uppercase tracking-wider">Riwayat</p>
        <div v-for="session in sessions" :key="session.id"
          @click="$emit('select-session', session.id)"
          :class="[
            'flex items-center gap-2 px-3 py-2 rounded-lg cursor-pointer transition-all group text-sm',
            session.active
              ? 'bg-white/10 text-white'
              : 'text-white/50 hover:text-white/80 hover:bg-white/5'
          ]"
        >
          <MessageSquare :size="14" class="shrink-0" />
          <span class="truncate text-xs">{{ session.title }}</span>
          <span v-if="session.active" class="ml-auto w-1.5 h-1.5 rounded-full bg-purple-400 animate-pulse shrink-0"></span>
        </div>
      </div>
    </nav>

    <!-- User Profile -->
    <div class="px-3 pb-4 border-t border-white/8 pt-3">
      <div :class="['flex items-center gap-3 px-3 py-2 rounded-xl hover:bg-white/5 transition-all cursor-pointer', collapsed ? 'justify-center' : '']">
        <div class="w-8 h-8 rounded-lg bg-gradient-to-br from-purple-500 to-cyan-400 flex items-center justify-center shrink-0">
          <span class="text-white text-xs font-bold">{{ userInitial }}</span>
        </div>
        <div v-if="!collapsed" class="min-w-0">
          <p class="text-sm font-medium text-white/90 truncate">{{ userName }}</p>
          <p class="text-xs text-white/40 truncate">{{ userEmail }}</p>
        </div>
        <button v-if="!collapsed" @click="$emit('logout')" class="ml-auto text-white/30 hover:text-red-400 transition-colors">
          <LogOut :size="15" />
        </button>
      </div>
    </div>
  </aside>

  <!-- Mobile overlay -->
  <div v-if="mobileOpen" @click="$emit('close-mobile')" class="fixed inset-0 bg-black/50 z-30 md:hidden"></div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRoute } from 'vue-router'
import {
  MessageSquare, BarChart2, BookOpen, History, User, LogOut,
  SquarePen, ChevronLeft, ChevronRight
} from '@lucide/vue'
import { useAuthStore } from '@/stores/auth'
import SidebarItem from './SidebarItem.vue'

const props = defineProps({
  sessions: { type: Array, default: () => [] },
  mobileOpen: { type: Boolean, default: false },
  showHistory: { type: Boolean, default: true }
})
defineEmits(['new-chat', 'select-session', 'logout', 'close-mobile'])

const $route = useRoute()
const auth = useAuthStore()
const collapsed = ref(false)

const navItems = [
  { name: 'chat', label: 'Chat', to: '/chat', icon: MessageSquare },
  { name: 'mood', label: 'Mood Tracking', to: '/mood', icon: BarChart2 },
  { name: 'resources', label: 'Resource Center', to: '/resources', icon: BookOpen },
]

const userName = computed(() => auth.user?.name || 'Mahasiswa')
const userEmail = computed(() => auth.user?.email || '')
const userInitial = computed(() => userName.value.charAt(0).toUpperCase())
</script>
