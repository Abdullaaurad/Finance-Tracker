<script lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'

</script>

<template>
  <div class="home-container">
    <h1>Welcome to the Finance Tracker App</h1>
    <p>Manage your finances effectively and efficiently.</p>
    <router-link to="/login">
      <button class="home-button">Login</button>
    </router-link>
    <router-link to="/signup">
      <button class="home-button">Sign Up</button>
    </router-link>
  </div>
</template>