<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const email = ref('')
const password = ref('')
const confirmPassword = ref('')

const handleSignup = () => {
  if (password.value !== confirmPassword.value) {
    alert('Passwords do not match')
    return
  }
  // TODO: Implement signup logic
  console.log('Signup:', email.value, password.value)
  // After successful signup, redirect to login or dashboard
  // router.push('/login')
}

const goToLogin = () => {
  router.push('/login')
}
</script>

<template>
  <div class="signup-container">
    <h2>Sign Up</h2>
    <form @submit.prevent="handleSignup">
      <div class="form-group">
        <label for="email">Email:</label>
        <input
          id="email"
          v-model="email"
          type="email"
          required
        />
      </div>
      <div class="form-group">
        <label for="password">Password:</label>
        <input
          id="password"
          v-model="password"
          type="password"
          required
        />
      </div>
      <div class="form-group">
        <label for="confirmPassword">Confirm Password:</label>
        <input
          id="confirmPassword"
          v-model="confirmPassword"
          type="password"
          required
        />
      </div>
      <button type="submit">Sign Up</button>
    </form>
    <p>
      Already have an account?
      <button @click="goToLogin" class="link-button">Login</button>
    </p>
  </div>
</template>

<style scoped>
.signup-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
}

input {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  width: 100%;
  padding: 10px;
  background-color: #28a745;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #218838;
}

.link-button {
  background: none;
  border: none;
  color: #007bff;
  text-decoration: underline;
  cursor: pointer;
  padding: 0;
}

.link-button:hover {
  color: #0056b3;
}
</style>