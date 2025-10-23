import { createRouter, createWebHistory } from 'vue-router'
import Login from './screens/login.vue'
import Signup from './screens/Signup.vue'

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router