// Authentication composable for managing persistent authentication state
import { ref, computed } from 'vue'

// Local storage keys
const AUTH_USER_KEY = 'finance-tracker-user'
const AUTH_USERNAME_KEY = 'finance-tracker-username'
const AUTH_TOKEN_KEY = 'finance-tracker-token'
const AUTH_EXP_KEY = 'finance-tracker-exp'

// Reactive authentication state
const userId = ref<number | null>(null)
const username = ref<string | null>(null)
const isAuthenticated = ref<boolean>(false)

// Load authentication from localStorage on app start
export const initializeAuth = () => {
  try {
    const storedUserId = localStorage.getItem(AUTH_USER_KEY)
    const storedUsername = localStorage.getItem(AUTH_USERNAME_KEY)
    const storedExp = localStorage.getItem(AUTH_EXP_KEY)
    
    // Check if token is expired
    if (storedExp) {
      const expirationTime = parseInt(storedExp)
      const currentTime = Date.now()
      
      if (currentTime < expirationTime) {
        // Token is still valid, restore auth state
        if (storedUserId) {
          userId.value = parseInt(storedUserId)
        }
        if (storedUsername) {
          username.value = storedUsername
        }
        isAuthenticated.value = true
        return true
      } else {
        // Token expired, clear storage
        clearAuthStorage()
      }
    }
  } catch (error) {
    console.error('Failed to initialize authentication:', error)
    clearAuthStorage()
  }
  return false
}

// Clear authentication storage
export const clearAuthStorage = () => {
  localStorage.removeItem(AUTH_USER_KEY)
  localStorage.removeItem(AUTH_USERNAME_KEY) 
  localStorage.removeItem(AUTH_EXP_KEY)
  localStorage.removeItem(AUTH_TOKEN_KEY)
  
  // Reset reactive state
  userId.value = null
  username.value = null
  isAuthenticated.value = false
}

// Set authentication data
export const setAuthData = (newUserId: number | null, newUsername: string | null, token?: string) => {
  // Validate input data
  if (!newUserId || !newUsername) {
    console.error('Invalid authentication data provided')
    return
  }
  
  userId.value = newUserId
  username.value = newUsername
  isAuthenticated.value = true
  
  // Store in localStorage (persist across page refreshes)
  localStorage.setItem(AUTH_USER_KEY, newUserId.toString())
  localStorage.setItem(AUTH_USERNAME_KEY, newUsername)
  
  // Set token expiration (30 minutes from now)
  const expirationTime = Date.now() + (30 * 60 * 1000)
  localStorage.setItem(AUTH_EXP_KEY, expirationTime.toString())
  
  if (token) {
    localStorage.setItem(AUTH_TOKEN_KEY, token)
  }
}

// Authentication composable
export const useAuth = () => {
  // Computed values
  const isLoggedIn = computed(() => isAuthenticated.value && userId.value !== null && username.value !== null)
  
  // Actions
  const login = (newUserId: number | null, newUsername: string | null, token?: string) => {
    setAuthData(newUserId, newUsername, token)
  }
  
  const logout = () => {
    clearAuthStorage()
  }
  
  const checkAuth = () => {
    return initializeAuth()
  }
  
  return {
    userId,
    username,
    isAuthenticated,
    isLoggedIn,
    login,
    logout,
    checkAuth
  }
}

// Helper function to check if user should be on login page
export const shouldRedirectToLogin = () => {
  return !initializeAuth()
}

// Helper function to check if user should be redirected from protected pages
export const shouldRedirectFromProtected = () => {
  return !initializeAuth()
}