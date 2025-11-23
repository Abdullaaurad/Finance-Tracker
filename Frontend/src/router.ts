import { createRouter, createWebHistory } from 'vue-router'
import Login from './screens/login.vue'
import Signup from './screens/Signup.vue'
import Landing from './screens/Landing.vue'
import Home from './screens/Dashboard.vue'
import { initializeAuth } from './composables/useAuth'

const routes = [
  {
    path: '/',
    redirect: '/landing'
  },
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
  },
  {
    path: '/Dashboard',
    name: 'Dashboard',
    component: Home,
    meta: { requiresAuth: true }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// Navigation guard to check authentication
router.beforeEach((to, from, next) => {
  const isAuthenticated = initializeAuth()
  
  // If user is authenticated and trying to access login/signup, redirect to home
  if (isAuthenticated && (to.path === '/login' || to.path === '/signup')) {
    next('/home')
    return
  }
  
  if (to.matched.some(record => record.meta.requiresAuth)) {
    // This route requires authentication
    if (!isAuthenticated) {
      // User is not authenticated, redirect to login
      next('/login')
    } else {
      // User is authenticated, proceed
      next()
    }
  } else {
    // This route doesn't require authentication, proceed
    next()
  }
})

export default router