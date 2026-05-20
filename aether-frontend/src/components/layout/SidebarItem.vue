<template>
  <router-link
    :to="to"
    :class="[
      'flex items-center gap-3 px-3 py-2.5 rounded-xl transition-all duration-200 group text-sm font-medium',
      active
        ? 'bg-purple-500/20 text-purple-300 border border-purple-500/30'
        : 'text-white/50 hover:text-white/80 hover:bg-white/5',
      collapsed ? 'justify-center' : ''
    ]"
  >
    <component :is="icon" :size="18" :class="active ? 'text-purple-400' : 'group-hover:text-white/80'" class="shrink-0" />
    <span v-if="!collapsed">{{ label }}</span>
  </router-link>
</template>

<script setup>
defineProps({
  icon: Object,
  label: String,
  to: String,
  active: Boolean,
  collapsed: Boolean
})
</script>
