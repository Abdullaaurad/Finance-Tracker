<script setup lang="ts">
import { ref } from 'vue'
import Header from '../components/Header.vue'
import Sidebar from '../components/Sidebar.vue'

// Mock data - replace with actual data from API
const currentIncome = ref<number>(8293)
const currentExpenses = ref<number>(305)
const totalBalance = ref<number>(24093.00)
const userName = ref<string>('Jones')

const incomeData = ref([
  { month: 'Jan', value: 6500 },
  { month: 'Feb', value: 7200 },
  { month: 'Mar', value: 7800 },
  { month: 'Apr', value: 8293 },
])

const expenseData = ref([
  { day: 1, value: 45 },
  { day: 2, value: 32 },
  { day: 3, value: 28 },
  { day: 4, value: 52 },
  { day: 5, value: 38 },
  { day: 6, value: 42 },
  { day: 7, value: 48 },
])

const transactions = ref([
  { id: 1, name: 'Starbucks', amount: -30.44, date: '02 Apr 25', icon: '☕', number: '#76248' },
  { id: 2, name: 'Walmart', amount: -198.98, date: '02 Apr 25', icon: '🛒', number: '#78257' },
  { id: 3, name: 'Inc. Zara', amount: -79.56, date: '01 Apr 25', icon: '👔', number: '#95337' },
  { id: 4, name: 'Walmart', amount: -234.25, date: '31 Mar 25', icon: '🛒', number: '#76935' },
  { id: 5, name: 'Robert Fox', amount: -81.02, date: '28 Mar 25', icon: '👤', number: '#45336' },
  { id: 6, name: 'eBay', amount: -46.61, date: '26 Mar 25', icon: '🛍️', number: '#83256' },
])

const familyMembers = ref([
  { id: 1, name: 'Sarah Jones', avatar: '👩', balance: 5420.00 },
  { id: 2, name: 'Mike Jones', avatar: '👨', balance: 3250.00 },
  { id: 3, name: 'Emma Jones', avatar: '👧', balance: 1850.00 },
])

const selectedPeriod = ref<string>('This week')
const selectedCategory = ref<string>('Category: Expenses')
const selectedMembers = ref<string>('All members')
</script>

<template>
  <div class="dashboard-layout">
    <Sidebar />
    
    <div class="main-wrapper">
      <Header />
      
      <main class="dashboard-content">
        <div class="page-title">
          <h1>Cards</h1>
          <button class="see-all-btn">See all</button>
        </div>

        <!-- Top Row: Card, Income, Expenses, Profile -->
        <div class="top-section">
          <!-- Credit Card -->
          <div class="card-widget glass-card">
            <div class="credit-card">
              <div class="card-header">
                <span class="bank-name">K Bank</span>
                <div class="card-logo">
                  <div class="circle red"></div>
                  <div class="circle yellow"></div>
                </div>
              </div>
              <div class="card-chip"></div>
              <div class="card-number">1234 5678 9009 8765</div>
              <div class="card-footer">
                <div class="card-holder">
                  <div class="card-label">JASON JONES</div>
                  <div class="card-expiry">03/28</div>
                </div>
                <div class="contactless">
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                    <path d="M12 6C15.31 6 18 8.69 18 12M12 2C17.52 2 22 6.48 22 12M12 10C13.1 10 14 10.9 14 12" 
                          stroke="white" stroke-width="2" stroke-linecap="round"/>
                  </svg>
                </div>
              </div>
            </div>
          </div>

          <!-- Income Chart -->
          <div class="stat-widget glass-card">
            <div class="stat-header">
              <div>
                <h3>Your Income</h3>
                <p class="stat-subtitle">Current month</p>
              </div>
              <button class="expand-btn">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <polyline points="15 3 21 3 21 9"/>
                  <polyline points="9 21 3 21 3 15"/>
                  <line x1="21" y1="3" x2="14" y2="10"/>
                  <line x1="3" y1="21" x2="10" y2="14"/>
                </svg>
              </button>
            </div>
            <div class="stat-amount">${{ currentIncome.toLocaleString() }}</div>
            <div class="mini-chart income-chart">
              <svg viewBox="0 0 200 60" preserveAspectRatio="none">
                <defs>
                  <linearGradient id="incomeGradient" x1="0%" y1="0%" x2="0%" y2="100%">
                    <stop offset="0%" stop-color="rgba(99, 102, 241, 0.3)" />
                    <stop offset="100%" stop-color="rgba(99, 102, 241, 0)" />
                  </linearGradient>
                </defs>
                <path d="M0,50 L50,35 L100,25 L150,20 L200,10" 
                      fill="none" 
                      stroke="#6366f1" 
                      stroke-width="2"/>
                <path d="M0,50 L50,35 L100,25 L150,20 L200,10 L200,60 L0,60 Z" 
                      fill="url(#incomeGradient)"/>
              </svg>
            </div>
          </div>

          <!-- Expenses Chart -->
          <div class="stat-widget glass-card">
            <div class="stat-header">
              <div>
                <h3>Your Expenses</h3>
                <p class="stat-subtitle">Current month</p>
              </div>
              <button class="expand-btn">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <polyline points="15 3 21 3 21 9"/>
                  <polyline points="9 21 3 21 3 15"/>
                  <line x1="21" y1="3" x2="14" y2="10"/>
                  <line x1="3" y1="21" x2="10" y2="14"/>
                </svg>
              </button>
            </div>
            <div class="stat-amount">${{ currentExpenses }}</div>
            <div class="mini-chart expense-chart">
              <div class="bar-chart">
                <div v-for="(item, index) in expenseData" :key="index" class="bar" :style="{ height: `${(item.value / 60) * 100}%` }"></div>
              </div>
            </div>
          </div>

          <!-- Profile Card -->
          <div class="profile-widget glass-card">
            <div class="stat-header">
              <h3>Profile</h3>
              <button class="expand-btn">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <polyline points="15 3 21 3 21 9"/>
                  <polyline points="9 21 3 21 3 15"/>
                  <line x1="21" y1="3" x2="14" y2="10"/>
                  <line x1="3" y1="21" x2="10" y2="14"/>
                </svg>
              </button>
            </div>
            <div class="profile-info">
              <div class="profile-avatar">
                <img src="https://i.pravatar.cc/150?img=12" alt="Profile" />
              </div>
              <div class="profile-name">{{ userName }}</div>
              <div class="profile-balance">
                <span class="balance-label">Total Balance</span>
                <span class="balance-amount">${{ totalBalance.toLocaleString('en-US', { minimumFractionDigits: 2 }) }}</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Bottom Row: Statistics Chart and Transactions -->
        <div class="bottom-section">
          <!-- Statistics Chart -->
          <div class="statistics-widget glass-card">
            <div class="widget-header">
              <h3>Statistic</h3>
              <div class="filters">
                <select v-model="selectedMembers" class="filter-select">
                  <option>All members</option>
                  <option>Sarah Jones</option>
                  <option>Mike Jones</option>
                  <option>Emma Jones</option>
                </select>
                <select v-model="selectedCategory" class="filter-select">
                  <option>Category: Expenses</option>
                  <option>Category: Income</option>
                  <option>Category: All</option>
                </select>
                <select v-model="selectedPeriod" class="filter-select">
                  <option>This week</option>
                  <option>This month</option>
                  <option>This year</option>
                </select>
              </div>
            </div>
            <div class="chart-container">
              <div class="chart-y-axis">
                <span>$350</span>
                <span>$300</span>
                <span>$250</span>
                <span>$200</span>
                <span>$150</span>
                <span>$100</span>
                <span>$0</span>
              </div>
              <div class="chart-area">
                <svg viewBox="0 0 600 200" preserveAspectRatio="none">
                  <defs>
                    <linearGradient id="chartGradient1" x1="0%" y1="0%" x2="0%" y2="100%">
                      <stop offset="0%" stop-color="rgba(139, 92, 246, 0.3)" />
                      <stop offset="100%" stop-color="rgba(139, 92, 246, 0)" />
                    </linearGradient>
                    <linearGradient id="chartGradient2" x1="0%" y1="0%" x2="0%" y2="100%">
                      <stop offset="0%" stop-color="rgba(99, 102, 241, 0.2)" />
                      <stop offset="100%" stop-color="rgba(99, 102, 241, 0)" />
                    </linearGradient>
                  </defs>
                  <!-- Area 1 -->
                  <path d="M0,120 Q100,80 200,100 T400,90 T600,70" 
                        fill="none" 
                        stroke="#8b5cf6" 
                        stroke-width="2.5"/>
                  <path d="M0,120 Q100,80 200,100 T400,90 T600,70 L600,200 L0,200 Z" 
                        fill="url(#chartGradient1)"/>
                  
                  <!-- Area 2 -->
                  <path d="M0,150 Q100,130 200,140 T400,120 T600,110" 
                        fill="none" 
                        stroke="#6366f1" 
                        stroke-width="2"/>
                  <path d="M0,150 Q100,130 200,140 T400,120 T600,110 L600,200 L0,200 Z" 
                        fill="url(#chartGradient2)"/>
                  
                  <!-- Data point -->
                  <circle cx="300" cy="95" r="6" fill="#8b5cf6"/>
                  <circle cx="300" cy="95" r="3" fill="white"/>
                </svg>
                
                <!-- Tooltip -->
                <div class="chart-tooltip" style="left: 50%; top: 40%;">
                  <div class="tooltip-avatar">
                    <img src="https://i.pravatar.cc/150?img=5" alt="Jason" />
                  </div>
                  <div class="tooltip-content">
                    <span class="tooltip-name">Jason</span>
                    <span class="tooltip-value">$234</span>
                  </div>
                </div>
                
                <div class="chart-x-axis">
                  <span>Mar 27</span>
                  <span>Mar 28</span>
                  <span>Mar 29</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Transactions & Family Members -->
          <div class="right-column">
            <!-- Transactions List -->
            <div class="transactions-widget glass-card">
              <div class="widget-header">
                <h3>Transactions</h3>
                <button class="see-all-btn small">See all</button>
              </div>
              <div class="transactions-list">
                <div v-for="transaction in transactions" :key="transaction.id" class="transaction-item">
                  <div class="transaction-icon">{{ transaction.icon }}</div>
                  <div class="transaction-details">
                    <div class="transaction-name">{{ transaction.name }}</div>
                    <div class="transaction-date">{{ transaction.date }}</div>
                  </div>
                  <div class="transaction-right">
                    <div class="transaction-amount" :class="{ negative: transaction.amount < 0 }">
                      {{ transaction.amount < 0 ? '-' : '+' }}${{ Math.abs(transaction.amount).toFixed(2) }}
                    </div>
                    <div class="transaction-number">{{ transaction.number }}</div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Family Members -->
            <div class="family-widget glass-card">
              <div class="widget-header">
                <h3>Family members</h3>
                <button class="switch-account-btn">Switch account</button>
              </div>
              <div class="family-list">
                <div v-for="member in familyMembers" :key="member.id" class="family-member">
                  <div class="member-avatar">{{ member.avatar }}</div>
                  <div class="member-info">
                    <div class="member-name">{{ member.name }}</div>
                    <div class="member-balance">${{ member.balance.toLocaleString('en-US', { minimumFractionDigits: 2 }) }}</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<style scoped>
* {
  box-sizing: border-box;
}

.dashboard-layout {
  display: flex;
  min-height: 100vh;
  background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 50%, #0f0f0f 100%);
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
}

.main-wrapper {
  flex: 1;
  margin-left: 240px;
  display: flex;
  flex-direction: column;
  transition: margin-left 0.3s ease;
}

.dashboard-content {
  flex: 1;
  padding: 24px;
  overflow-y: auto;
}

/* Page Title */
.page-title {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
}

.page-title h1 {
  font-size: 28px;
  font-weight: 600;
  color: #ffffff;
  margin: 0;
}

.see-all-btn {
  padding: 8px 16px;
  background: rgba(30, 30, 40, 0.6);
  border: 1px solid rgba(216, 196, 255, 0.2);
  border-radius: 8px;
  color: #94a3b8;
  font-size: 13px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.see-all-btn:hover {
  background: rgba(30, 30, 40, 0.9);
  border-color: rgba(216, 196, 255, 0.4);
  color: #e2e8f0;
}

.see-all-btn.small {
  padding: 4px 12px;
  font-size: 12px;
}

/* Glass Card Effect */
.glass-card {
  background: linear-gradient(135deg, rgba(30, 30, 30, 0.6) 0%, rgba(20, 20, 20, 0.4) 100%);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(216, 196, 255, 0.2);
  border-radius: 16px;
  padding: 20px;
  transition: all 0.3s ease;
}

.glass-card:hover {
  border-color: rgba(216, 196, 255, 0.3);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}

/* Top Section */
.top-section {
  display: grid;
  grid-template-columns: 1.2fr 1fr 1fr 1fr;
  gap: 20px;
  margin-bottom: 20px;
}

/* Credit Card */
.card-widget {
  padding: 0;
  overflow: hidden;
}

.credit-card {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 24px;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  min-height: 200px;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.bank-name {
  color: #ffffff;
  font-size: 18px;
  font-weight: 600;
}

.card-logo {
  display: flex;
  gap: -8px;
}

.circle {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  opacity: 0.9;
}

.circle.red {
  background: #eb001b;
  margin-right: -8px;
}

.circle.yellow {
  background: #f79e1b;
}

.card-chip {
  width: 40px;
  height: 32px;
  background: linear-gradient(135deg, #ffd700, #ffed4e);
  border-radius: 6px;
  margin-bottom: 16px;
}

.card-number {
  color: #ffffff;
  font-size: 18px;
  font-weight: 500;
  letter-spacing: 2px;
  margin-bottom: 16px;
}

.card-footer {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
}

.card-holder {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.card-label {
  color: rgba(255, 255, 255, 0.8);
  font-size: 11px;
  font-weight: 500;
}

.card-expiry {
  color: #ffffff;
  font-size: 13px;
}

.contactless {
  color: #ffffff;
}

/* Stat Widgets */
.stat-widget {
  display: flex;
  flex-direction: column;
}

.stat-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 12px;
}

.stat-header h3 {
  font-size: 14px;
  font-weight: 600;
  color: #ffffff;
  margin: 0 0 4px 0;
}

.stat-subtitle {
  font-size: 11px;
  color: #64748b;
  margin: 0;
}

.expand-btn {
  background: none;
  border: none;
  color: #64748b;
  cursor: pointer;
  padding: 4px;
  transition: color 0.2s;
}

.expand-btn:hover {
  color: #94a3b8;
}

.stat-amount {
  font-size: 28px;
  font-weight: 700;
  color: #ffffff;
  margin-bottom: 12px;
}

.mini-chart {
  flex: 1;
  min-height: 60px;
}

.mini-chart svg {
  width: 100%;
  height: 100%;
}

.bar-chart {
  display: flex;
  align-items: flex-end;
  gap: 4px;
  height: 100%;
  padding-bottom: 4px;
}

.bar {
  flex: 1;
  background: linear-gradient(180deg, #6366f1, #8b5cf6);
  border-radius: 2px;
  min-height: 8px;
  transition: all 0.3s ease;
}

.bar:hover {
  opacity: 0.8;
}

/* Profile Widget */
.profile-widget {
  display: flex;
  flex-direction: column;
}

.profile-info {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  margin-top: 8px;
}

.profile-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  overflow: hidden;
  border: 3px solid rgba(216, 196, 255, 0.3);
  margin-bottom: 12px;
}

.profile-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.profile-name {
  font-size: 18px;
  font-weight: 600;
  color: #ffffff;
  margin-bottom: 8px;
}

.profile-balance {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.balance-label {
  font-size: 11px;
  color: #64748b;
}

.balance-amount {
  font-size: 22px;
  font-weight: 700;
  color: #ffffff;
}

/* Bottom Section */
.bottom-section {
  display: grid;
  grid-template-columns: 1.5fr 1fr;
  gap: 20px;
}

/* Statistics Widget */
.statistics-widget {
  display: flex;
  flex-direction: column;
}

.widget-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.widget-header h3 {
  font-size: 16px;
  font-weight: 600;
  color: #ffffff;
  margin: 0;
}

.filters {
  display: flex;
  gap: 8px;
}

.filter-select {
  padding: 6px 12px;
  background: rgba(30, 30, 40, 0.6);
  border: 1px solid rgba(216, 196, 255, 0.2);
  border-radius: 8px;
  color: #94a3b8;
  font-size: 12px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.filter-select:hover {
  border-color: rgba(216, 196, 255, 0.4);
}

.chart-container {
  display: flex;
  gap: 12px;
  flex: 1;
}

.chart-y-axis {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 10px 0;
  font-size: 11px;
  color: #64748b;
}

.chart-area {
  flex: 1;
  position: relative;
  display: flex;
  flex-direction: column;
}

.chart-area svg {
  width: 100%;
  height: 180px;
}

.chart-tooltip {
  position: absolute;
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 12px;
  background: rgba(20, 20, 30, 0.95);
  border: 1px solid rgba(216, 196, 255, 0.3);
  border-radius: 8px;
  transform: translate(-50%, -100%);
  margin-top: -8px;
}

.tooltip-avatar {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  overflow: hidden;
  border: 2px solid #8b5cf6;
}

.tooltip-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.tooltip-content {
  display: flex;
  flex-direction: column;
}

.tooltip-name {
  font-size: 12px;
  color: #94a3b8;
}

.tooltip-value {
  font-size: 14px;
  font-weight: 600;
  color: #ffffff;
}

.chart-x-axis {
  display: flex;
  justify-content: space-around;
  padding-top: 12px;
  font-size: 11px;
  color: #64748b;
}

/* Right Column */
.right-column {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

/* Transactions Widget */
.transactions-widget {
  flex: 1;
}

.transactions-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
  max-height: 340px;
  overflow-y: auto;
  padding-right: 4px;
}

.transaction-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px;
  background: rgba(30, 30, 40, 0.3);
  border-radius: 10px;
  transition: all 0.2s;
}

.transaction-item:hover {
  background: rgba(30, 30, 40, 0.5);
}

.transaction-icon {
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(216, 196, 255, 0.1);
  border-radius: 8px;
  font-size: 18px;
}

.transaction-details {
  flex: 1;
}

.transaction-name {
  font-size: 13px;
  font-weight: 500;
  color: #e2e8f0;
  margin-bottom: 2px;
}

.transaction-date {
  font-size: 11px;
  color: #64748b;
}

.transaction-right {
  text-align: right;
}

.transaction-amount {
  font-size: 13px;
  font-weight: 600;
  color: #10b981;
  margin-bottom: 2px;
}

.transaction-amount.negative {
  color: #ef4444;
}

.transaction-number {
  font-size: 11px;
  color: #64748b;
}

/* Family Widget */
.family-widget {
  
}

.switch-account-btn {
  padding: 4px 12px;
  background: rgba(99, 102, 241, 0.15);
  border: 1px solid rgba(216, 196, 255, 0.3);
  border-radius: 8px;
  color: #a5b4fc;
  font-size: 12px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.switch-account-btn:hover {
  background: rgba(99, 102, 241, 0.25);
  border-color: rgba(216, 196, 255, 0.4);
}

.family-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.family-member {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px;
  background: rgba(30, 30, 40, 0.3);
  border-radius: 10px;
  transition: all 0.2s;
  cursor: pointer;
}

.family-member:hover {
  background: rgba(30, 30, 40, 0.5);
}

.member-avatar {
  width: 44px;
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
  border-radius: 50%;
  font-size: 22px;
}

.member-info {
  flex: 1;
}

.member-name {
  font-size: 13px;
  font-weight: 500;
  color: #e2e8f0;
  margin-bottom: 4px;
}

.member-balance {
  font-size: 15px;
  font-weight: 600;
  color: #ffffff;
}

/* Scrollbar Styling */
.transactions-list::-webkit-scrollbar {
  width: 4px;
}

.transactions-list::-webkit-scrollbar-track {
  background: transparent;
}

.transactions-list::-webkit-scrollbar-thumb {
  background: rgba(216, 196, 255, 0.2);
  border-radius: 2px;
}

.transactions-list::-webkit-scrollbar-thumb:hover {
  background: rgba(216, 196, 255, 0.3);
}

/* Responsive Design */
@media (max-width: 1400px) {
  .top-section {
    grid-template-columns: 1fr 1fr;
  }
  
  .bottom-section {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 1024px) {
  .main-wrapper {
    margin-left: 72px;
  }
}

@media (max-width: 768px) {
  .main-wrapper {
    margin-left: 0;
  }
  
  .dashboard-content {
    padding: 16px;
  }
  
  .page-title h1 {
    font-size: 24px;
  }
  
  .top-section {
    grid-template-columns: 1fr;
  }
  
  .filters {
    flex-direction: column;
    width: 100%;
  }
  
  .filter-select {
    width: 100%;
  }
  
  .chart-container {
    flex-direction: column;
  }
  
  .chart-y-axis {
    flex-direction: row;
    justify-content: space-between;
  }
}

@media (max-width: 480px) {
  .page-title {
    flex-direction: column;
    align-items: flex-start;
    gap: 12px;
  }
  
  .widget-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 12px;
  }
  
  .stat-amount {
    font-size: 24px;
  }
  
  .card-number {
    font-size: 16px;
  }
}
</style>