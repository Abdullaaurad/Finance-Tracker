<script setup lang="ts">
import { ref, computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import Logo from '../assets/logo.png'

const router = useRouter()
const route = useRoute()

const isSidebarCollapsed = ref<boolean>(false)

interface MenuItem {
  name: string
  icon: string
  path: string
  badge?: number
}

const menuItems: MenuItem[] = [
  { name: 'Dashboard', icon: 'dashboard', path: '/Dashboard' },
  { name: 'Wallet', icon: 'wallet', path: '/wallet' },
  { name: 'Analytics', icon: 'analytics', path: '/analytics' },
  { name: 'Transactions', icon: 'transactions', path: '/transactions' },
  { name: 'Orders', icon: 'orders', path: '/orders' },
  { name: 'Account', icon: 'account', path: '/account' },
]

const isActive = (path: string) => {
  return route.path === path
}

const navigateTo = (path: string) => {
  router.push(path)
}

</script>

<template>
  <aside class="sidebar" :class="{ collapsed: isSidebarCollapsed }">
    <div class="sidebar-content">
      <!-- Logo -->
      <div class="logo-container">
        <div class="logo">
            <img :src="Logo" alt="VAULT Logo" width="45" height="45" />
          <span v-if="!isSidebarCollapsed" class="logo-text">VAULT</span>
        </div>
      </div>

      <!-- Navigation Menu -->
      <nav class="nav-menu">
        <button
          v-for="item in menuItems"
          :key="item.path"
          class="nav-item"
          :class="{ active: isActive(item.path) }"
          @click="navigateTo(item.path)"
        >
          <!-- Dashboard Icon -->
          <svg v-if="item.icon === 'dashboard'" class="nav-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <rect x="3" y="3" width="7" height="7" rx="1"/>
            <rect x="14" y="3" width="7" height="7" rx="1"/>
            <rect x="14" y="14" width="7" height="7" rx="1"/>
            <rect x="3" y="14" width="7" height="7" rx="1"/>
          </svg>

          <!-- Wallet Icon -->
          <svg v-else-if="item.icon === 'wallet'" class="nav-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M21 12V7H5a2 2 0 0 1 0-4h14v4"/>
            <path d="M3 5v14a2 2 0 0 0 2 2h16v-5"/>
            <path d="M18 12a2 2 0 0 0 0 4h4v-4Z"/>
          </svg>

          <!-- Analytics Icon -->
          <svg v-else-if="item.icon === 'analytics'" class="nav-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <line x1="12" y1="20" x2="12" y2="10"/>
            <line x1="18" y1="20" x2="18" y2="4"/>
            <line x1="6" y1="20" x2="6" y2="16"/>
          </svg>

          <!-- Transactions Icon -->
          <svg v-else-if="item.icon === 'transactions'" class="nav-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
            <polyline points="14 2 14 8 20 8"/>
            <line x1="16" y1="13" x2="8" y2="13"/>
            <line x1="16" y1="17" x2="8" y2="17"/>
            <polyline points="10 9 9 9 8 9"/>
          </svg>

          <!-- Orders Icon -->
          <svg v-else-if="item.icon === 'orders'" class="nav-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="9" cy="21" r="1"/>
            <circle cx="20" cy="21" r="1"/>
            <path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/>
          </svg>

          <!-- Account Icon -->
          <svg v-else-if="item.icon === 'account'" class="nav-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
            <circle cx="12" cy="7" r="4"/>
          </svg>

          <span v-if="!isSidebarCollapsed" class="nav-text">{{ item.name }}</span>
          
          <span v-if="item.badge && !isSidebarCollapsed" class="nav-badge">{{ item.badge }}</span>
        </button>
      </nav>

      <!-- Bottom Section -->
      <div class="sidebar-footer">
        <button class="nav-item help-center" @click="navigateTo('/help')">
          <svg class="nav-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="12" cy="12" r="10"/>
            <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/>
            <line x1="12" y1="17" x2="12.01" y2="17"/>
          </svg>
          <span v-if="!isSidebarCollapsed" class="nav-text">Help Center</span>
        </button>
      </div>
    </div>
  </aside>
</template>

<style scoped>
.sidebar {
  position: fixed;
  left: 0;
  top: 0;
  bottom: 0;
  width: 240px;
  background: rgba(15, 15, 15, 0.95);
  backdrop-filter: blur(20px);
  border-right: 1px solid rgba(216, 196, 255, 0.15);
  transition: width 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  z-index: 200;
  display: flex;
  flex-direction: column;
}

.sidebar-content {
  display: flex;
  flex-direction: column;
  height: 100%;
  padding: 20px 12px;
}

/* Logo */
.logo-container {
  margin-bottom: 32px;
  padding: 0 8px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.logo {
  display: flex;
  align-items: center;
  gap: 12px;
  color: #ffffff;
}

.logo svg {
  flex-shrink: 0;
}

.logo-text {
  font-size: 30px;
  font-weight: 700;
  letter-spacing: 0.5px;
  background: linear-gradient(135deg, #c2c4ff, #ad8aff);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  white-space: nowrap;
  opacity: 1;
  transition: opacity 0.2s;
}


/* Navigation Menu */
.nav-menu {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.nav-item {
  position: relative;
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 12px 14px;
  background: transparent;
  border: none;
  border-radius: 30px;
  color: #94a3b8;
  font-size: 14px;
  font-weight: 500;
  text-align: left;
  cursor: pointer;
  transition: all 0.3s ease;
  white-space: nowrap;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
}

.nav-item:hover {
  background: linear-gradient(to right, #b699fa8e, #9567ff19);
  color: #e2e8f0;
}

.nav-item.active {
  background: linear-gradient(to right, #b699fa8e, #9567ff19);
  color: #ffffff;
  border: 1px solid rgba(216, 196, 255, 0.466);
}

.sidebar.collapsed .nav-item {
  justify-content: center;
  padding: 12px;
}

.nav-icon {
  flex-shrink: 0;
  transition: transform 0.2s;
  margin-left: 15px;
}

.nav-item:hover .nav-icon {
  transform: scale(1.2);
}

.nav-text {
  flex: 1;
  opacity: 1;
  transition: opacity 0.2s;
}

.sidebar.collapsed .nav-text {
  opacity: 0;
  width: 0;
}

.nav-badge {
  padding: 2px 8px;
  background: #ef4444;
  border-radius: 10px;
  color: #fff;
  font-size: 11px;
  font-weight: 600;
  min-width: 20px;
  text-align: center;
}

.sidebar.collapsed .nav-badge {
  display: none;
}

/* Sidebar Footer */
.sidebar-footer {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-top: auto;
  padding-top: 16px;
  border-top: 1px solid rgba(216, 196, 255, 0.15);
}

.help-center {
  margin-bottom: 8px;
}

.collapse-toggle {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 10px;
  background: rgba(30, 30, 40, 0.6);
  border: 1px solid rgba(216, 196, 255, 0.2);
  border-radius: 8px;
  color: #94a3b8;
  cursor: pointer;
  transition: all 0.3s ease;
}

.collapse-toggle:hover {
  background: rgba(30, 30, 40, 0.9);
  border-color: rgba(216, 196, 255, 0.4);
  color: #e2e8f0;
}

.collapse-icon {
  transition: transform 0.3s ease;
}

.collapse-icon.rotated {
  transform: rotate(180deg);
}

/* Tooltip for collapsed state */
.sidebar.collapsed .nav-item {
  position: relative;
}

.sidebar.collapsed .nav-item::after {
  content: attr(data-tooltip);
  position: absolute;
  left: calc(100% + 12px);
  top: 50%;
  transform: translateY(-50%) scale(0.9);
  padding: 6px 12px;
  background: rgba(20, 20, 30, 0.95);
  border: 1px solid rgba(216, 196, 255, 0.3);
  border-radius: 6px;
  color: #e2e8f0;
  font-size: 13px;
  white-space: nowrap;
  opacity: 0;
  pointer-events: none;
  transition: all 0.2s ease;
  z-index: 1000;
}

.sidebar.collapsed .nav-item:hover::after {
  opacity: 1;
  transform: translateY(-50%) scale(1);
}

/* Responsive */
@media (max-width: 768px) {
  .sidebar {
    transform: translateX(-100%);
  }

  .sidebar.mobile-open {
    transform: translateX(0);
  }

  .sidebar.collapsed {
    width: 240px;
  }
}

/* Scrollbar styling */
.nav-menu::-webkit-scrollbar {
  width: 4px;
}

.nav-menu::-webkit-scrollbar-track {
  background: transparent;
}

.nav-menu::-webkit-scrollbar-thumb {
  background: rgba(216, 196, 255, 0.2);
  border-radius: 2px;
}

.nav-menu::-webkit-scrollbar-thumb:hover {
  background: rgba(216, 196, 255, 0.3);
}
</style>