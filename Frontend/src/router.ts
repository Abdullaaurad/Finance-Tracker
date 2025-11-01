import { createRouter, createWebHistory } from 'vue-router'
import Login from './screens/login.vue'
import Signup from './screens/Signup.vue'
import Landing from './screens/Landing.vue'

const routes = [
  {
    path: '/landing',
    name: 'Landing',
    component: Landing
  },
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