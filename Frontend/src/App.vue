<script setup lang="ts">
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { initializeAuth } from './composables/useAuth'

const router = useRouter()

onMounted(() => {
  // Initialize authentication state from localStorage
  const isAuthenticated = initializeAuth()
  
  // Handle root path redirect
  if (window.location.pathname === '/') {
    if (isAuthenticated) {
      router.push('/Dashboard')
    } else {
      router.push('/landing')
    }
  }
})
</script>

<template>
    <router-view />
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>