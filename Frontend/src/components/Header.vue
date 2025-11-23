<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { UserIcon, Cog6ToothIcon, ArrowRightOnRectangleIcon, BellIcon } from '@heroicons/vue/24/outline'
import { UserIcon as  UserIconSolid } from '@heroicons/vue/24/solid'
import { useAuth } from '../composables/useAuth'

const router = useRouter()
const { username, logout } = useAuth()
const searchQuery = ref<string>('')
const showNotifications = ref<boolean>(false)
const showUserMenu = ref<boolean>(false)

// Mock notification count - replace with actual data
const notificationCount = ref<number>(3)

const handleSearch = () => {
  if (searchQuery.value.trim()) {
    // Implement search logic
    console.log('Searching for:', searchQuery.value)
  }
}

const toggleNotifications = () => {
  showNotifications.value = !showNotifications.value
  showUserMenu.value = false
}

const toggleUserMenu = () => {
  showUserMenu.value = !showUserMenu.value
  showNotifications.value = false
}

const handleLogout = () => {
  logout() // Clear authentication state
  router.push('/login') // Redirect to login page
}
</script>

<template>
  <header class="header">
    <div class="header-content">
      <!-- Search Bar -->
      <div class="search-container">
        <svg 
          class="search-icon" 
          width="20" 
          height="20" 
          viewBox="0 0 24 24" 
          fill="none" 
          stroke="currentColor"
          stroke-width="2"
        >
          <circle cx="11" cy="11" r="8"/>
          <path d="m21 21-4.35-4.35"/>
        </svg>
        <input
          v-model="searchQuery"
          type="text"
          placeholder="Search"
          class="search-input"
          @keyup.enter="handleSearch"
        />
      </div>

      <!-- Right Side Actions -->
      <div class="header-actions">
        <!-- Notification Bell -->
        <div class="action-button-wrapper">
          <button 
            class="action-button notification-button" 
            @click="toggleNotifications"
            :class="{ active: showNotifications }"
          >
            <BellIcon class="icon-20" :style="{ color: 'white' }" />
            <span v-if="notificationCount > 0" class="notification-badge">
              {{ notificationCount }}
            </span>
          </button>

          <!-- Notification Dropdown -->
          <div v-if="showNotifications" class="dropdown notification-dropdown">
            <div class="dropdown-header">
              <h3>Notifications</h3>
              <button class="mark-read">Mark all as read</button>
            </div>
            <div class="notification-list">
              <div class="notification-item">
                <div class="notification-icon">💰</div>
                <div class="notification-content">
                  <p class="notification-title">Payment received</p>
                  <p class="notification-time">2 hours ago</p>
                </div>
              </div>
              <div class="notification-item">
                <div class="notification-icon">📊</div>
                <div class="notification-content">
                  <p class="notification-title">Monthly report ready</p>
                  <p class="notification-time">5 hours ago</p>
                </div>
              </div>
              <div class="notification-item">
                <div class="notification-icon">⚠️</div>
                <div class="notification-content">
                  <p class="notification-title">Low balance alert</p>
                  <p class="notification-time">1 day ago</p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Settings Button -->
        <button class="action-button">
          <Cog6ToothIcon class="icon-20" :style="{ color: 'white' }" />
        </button>

        <!-- User Menu Button -->
        <div class="action-button-wrapper">
          <button 
            class="action-button user-button" 
            @click="toggleUserMenu"
            :class="{ active: showUserMenu }"
          >
            <UserIcon class="icon-20" :style="{ color: 'white' }" fill="stroke" />
          </button>

          <!-- User Dropdown -->
          <div v-if="showUserMenu" class="dropdown user-dropdown">
            <div class="dropdown-user-info">
              <div class="user-avatar">
                <UserIconSolid class="icon-18" :style="{ height: 25, width: 25}" />
              </div>
              <div>
                <p class="user-name">{{ username || 'User' }}</p>
                <p class="user-email">{{ username ? `${username}@example.com` : 'user@example.com' }}</p>
              </div>
            </div>
            <button class="dropdown-item" @click="router.push('/profile')">
              <UserIcon class="icon-18" :style="{ height: 20, width: 20}" />
              Profile
            </button>
            <div class="dropdown-divider"></div>
            <button class="dropdown-item logout" @click="handleLogout">
              <ArrowRightOnRectangleIcon class="icon-18"  :style="{ height: 20, width: 20}"/>
              Logout
            </button>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>

<style scoped>
.header {
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(15, 15, 15, 0.8);
  backdrop-filter: blur(20px);
  border-bottom: 1px solid rgba(216, 196, 255, 0.15);
  padding: 16px 24px;
}

.header-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  max-width: 1400px;
  margin: 0 auto;
}

/* Search Bar */
.search-container {
  position: relative;
  flex: 0 0 640px;
}

.search-icon {
  position: absolute;
  left: 14px;
  top: 50%;
  transform: translateY(-50%);
  color: #cfcfcf;
  pointer-events: none;
}

.search-input {
  width: 100%;
  padding: 10px 14px 10px 42px;
  background: linear-gradient(to right, rgba(54, 54, 67, 0.9), rgba(15, 15, 15, 0.3));
  border: 1px solid rgba(216, 196, 255, 0.2);
  border-radius: 10px;
  color: #e2e8f0;
  font-size: 14px;
  font-family: inherit;
  transition: all 0.3s ease;
}

.search-input::placeholder {
  color: #cfcfcf;
}

.search-input:focus {
  outline: none;
  border-color: rgba(216, 196, 255, 0.4);
  background: rgba(30, 30, 40, 0.8);
}

/* Header Actions */
.header-actions {
  display: flex;
  align-items: center;
  gap: 12px;
}

.action-button-wrapper {
  position: relative;
}

.action-button {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  background: rgba(30, 30, 40, 0.6);
  border: 1px solid rgba(216, 196, 255, 0.2);
  border-radius: 10px;
  color: #94a3b8;
  cursor: pointer;
  transition: all 0.3s ease;
}

.action-button:hover,
.action-button.active {
  background: rgba(30, 30, 40, 0.9);
  border-color: rgba(216, 196, 255, 0.4);
  color: #e2e8f0;
}

.notification-badge {
  position: absolute;
  top: -4px;
  right: -4px;
  min-width: 18px;
  height: 18px;
  padding: 0 5px;
  background: #ef4444;
  border: 2px solid rgba(15, 15, 15, 0.9);
  border-radius: 9px;
  color: #fff;
  font-size: 11px;
  font-weight: 600;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Dropdowns */
.dropdown {
  position: absolute;
  top: calc(100% + 8px);
  right: 0;
  min-width: 280px;
  background: rgba(20, 20, 30, 0.95);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(216, 196, 255, 0.3);
  border-radius: 12px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
  overflow: hidden;
  animation: dropdownSlide 0.2s ease;
}

.icon-20,
.icon-18 {
  color: #94a3b8;
  stroke: currentColor;
  flex-shrink: 0;
}

.icon-20 {
  width: 20px;
  height: 20px;
}

.icon-18 {
  width: 18px;
  height: 18px;
}

/* Icons should turn white on hover */
.action-button:hover .icon-20,
.action-button:hover .icon-18 {
  color: #ffffff;
}

/* User avatar icon should always be white */
.user-avatar .icon-18 {
  color: #ffffff;
}

/* Dropdown item icons */
.dropdown-item .icon-18 {
  color: #94a3b8;
}

.dropdown-item:hover .icon-18 {
  color: #e2e8f0;
}

.dropdown-item.logout .icon-18 {
  color: #ef4444;
}

@keyframes dropdownSlide {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Notification Dropdown */
.dropdown-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px;
  border-bottom: 1px solid rgba(216, 196, 255, 0.15);
}

.dropdown-header h3 {
  margin: 0;
  color: #e2e8f0;
  font-size: 16px;
  font-weight: 600;
}

.mark-read {
  background: none;
  border: none;
  color: #6366f1;
  font-size: 13px;
  cursor: pointer;
  padding: 0;
  transition: color 0.2s;
}

.mark-read:hover {
  color: #818cf8;
}

.notification-list {
  max-height: 320px;
  overflow-y: auto;
}

.notification-item {
  display: flex;
  gap: 12px;
  padding: 14px 16px;
  border-bottom: 1px solid rgba(216, 196, 255, 0.1);
  transition: background 0.2s;
  cursor: pointer;
}

.notification-item:last-child {
  border-bottom: none;
}

.notification-item:hover {
  background: rgba(216, 196, 255, 0.05);
}

.notification-icon {
  font-size: 24px;
  flex-shrink: 0;
}

.notification-content {
  flex: 1;
}

.notification-title {
  margin: 0 0 4px 0;
  color: #e2e8f0;
  font-size: 14px;
  font-weight: 500;
}

.notification-time {
  margin: 0;
  color: #64748b;
  font-size: 12px;
}

/* User Dropdown */
.dropdown-user-info {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 16px;
  border-bottom: 1px solid rgba(216, 196, 255, 0.15);
}

.user-avatar {
  width: 40px;
  height: 40px;
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  flex-shrink: 0;
}

.user-name {
  margin: 0 0 2px 0;
  color: #e2e8f0;
  font-size: 14px;
  font-weight: 600;
}

.user-email {
  margin: 0;
  color: #64748b;
  font-size: 12px;
}

.dropdown-divider {
  height: 1px;
  background: rgba(216, 196, 255, 0.15);
  margin: 8px 0;
}

.dropdown-item {
  width: 100%;
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 16px;
  background: none;
  border: none;
  color: #94a3b8;
  font-size: 14px;
  text-align: left;
  cursor: pointer;
  transition: all 0.2s;
  font-family: inherit;
  margin-top: 6px;
}

.dropdown-item:hover {
  background: rgba(216, 196, 255, 0.05);
  color: #e2e8f0;
}

.dropdown-item.logout {
  color: #ef4444;
}

.dropdown-item.logout:hover {
  background: rgba(239, 68, 68, 0.1);
}

.user-dropdown{
  padding-bottom: 6px;
}

/* Responsive */
@media (max-width: 768px) {
  .header {
    padding: 12px 16px;
  }

  .search-container {
    flex: 1;
    max-width: none;
  }

  .header-actions {
    gap: 8px;
  }

  .action-button {
    width: 36px;
    height: 36px;
  }

  .dropdown {
    min-width: 260px;
  }
}
</style>