<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { ArrowTrendingUpIcon, ArrowTrendingDownIcon } from '@heroicons/vue/24/solid'
import Button from '../components/Button.vue'

const router = useRouter()
const mobileMenuOpen = ref(false)

const toggleMobileMenu = () => {
  mobileMenuOpen.value = !mobileMenuOpen.value
}

const navigateToLogin = () => {
  router.push('/login')
}

const navigateToSignup = () => {
  router.push('/signup')
}

const features = [
  { 
    icon: '📊', 
    title: 'Smart Financial Insights', 
    description: 'Get AI-powered insights to understand your spending patterns and make better decisions' 
  },
  { 
    icon: '🎯', 
    title: 'Personalized Financial Goals', 
    description: 'Set and track custom financial goals with automated progress monitoring' 
  },
  { 
    icon: '💳', 
    title: 'Smart Expense Splitting', 
    description: 'Easily split bills with friends, family or colleagues ensuring fair contributions' 
  },
  { 
    icon: '📈', 
    title: 'Automated Budgeting', 
    description: 'Set budgets automatically and get financial predictions for better money management' 
  }
]

const pricingPlans = [
  {
    title: 'Free Plan',
    subtitle: 'For Individual',
    price: '$0',
    features: [
      'Basic tools to manage your money',
      'Real-time balance tracking',
      'Basic cash flow insights',
      'Expense categorization',
      'Community support',
      'Up to 2 linked bank accounts'
    ],
    highlighted: false
  },
  {
    title: 'Pro Plan',
    subtitle: 'For Freelancers',
    price: '$15',
    features: [
      'Advanced insights and automation',
      'Everything in Free Plan, plus:',
      'AI-powered financial insights',
      'Unlimited linked bank accounts',
      'Advanced budgeting tools',
      'Multi-device sync'
    ],
    highlighted: true
  },
  {
    title: 'Enterprise Plan',
    subtitle: 'For Businesses',
    price: '$35',
    features: [
      'Tailored solutions for professionals',
      'Everything in Pro Plan, plus:',
      'Team financial management',
      'Advanced security & role-based access',
      'Dedicated support',
      'Custom reporting & analytics'
    ],
    highlighted: false
  }
]

const accountData = [
  { label: 'Income', amount: '$44,000.00', change: '+2.8%', positive: true },
  { label: 'Expends', amount: '$22,000.00', change: '-1.2%', positive: false }
]

const transactions = [
  { merchant: 'iCloud Monthly', amount: '-$9.99', category: 'Premium' },
  { merchant: 'Netflix', amount: '-$15.99', category: 'Shopping' },
  { merchant: 'Walmart', amount: '-$198.98', category: 'Shopping' }
]
</script>

<template>
  <div class="landing-container">
    <!-- Header -->
    <header class="header">
      <div class="logo">
        <img src="../assets/Logo.png" alt="Logo" class="logo-icon" />
        <span>BudgetBuddy</span>
      </div>
      <nav class="nav">
        <a href="#home">Home</a>
        <a href="#features">Features</a>
        <a href="#benefits">Benefits</a>
        <a href="#testimonials">Testimonials</a>
      </nav>
      <div class="header-buttons">
        <Button variant="primary" @click="navigateToLogin">LogIn</Button>
        <Button variant="primary" @click="navigateToSignup">SignUp</Button>
      </div>
      <button class="mobile-menu-btn" @click="toggleMobileMenu">
        {{ mobileMenuOpen ? '✕' : '☰' }}
      </button>
    </header>

    <!-- Mobile Menu -->
    <div v-if="mobileMenuOpen" class="mobile-menu">
      <a href="#home" @click="toggleMobileMenu">Home</a>
      <a href="#features" @click="toggleMobileMenu">Features</a>
      <a href="#benefits" @click="toggleMobileMenu">Benefits</a>
      <a href="#pricing" @click="toggleMobileMenu">Pricing</a>
      <a href="#testimonials" @click="toggleMobileMenu">Testimonials</a>
      <button class="btn-primary mobile-cta">Get Started</button>
    </div>

    <!-- Hero Section -->
    <section class="hero" id="home">
      <div class="hero-content">
        <h1 class="hero-title">
          Manage Finances<br />
          <span class="gradient-text">Easily and Smartly</span>
        </h1>
        <p class="hero-description">
          BudgetBuddy helps you control spending, track income, and manage savings 
          with an intuitive financial dashboard.
        </p>
        <div class="hero-buttons">
          <button class="btn-cta">Try It Free</button>
        </div>
      </div>

      <div class="hero-visual">
        <!-- Balance Card -->
        <div class="stat-card balance-card">
          <div class="card-header">
            <span class="card-label">My Balance</span>
            <button class="btn-small">Add Transaction</button>
          </div>
          <div class="card-amount">$66,000.00</div>
          <div class="card-change positive">+2.8%</div>
          
          <div class="accounts-row">
            <div v-for="account in accountData" :key="account.label" class="account-item">
              <div class="account-icon" :class="account.label.toLowerCase()">
                <ArrowTrendingUpIcon v-if="account.label === 'Income'" class="icon" />
                <ArrowTrendingDownIcon v-else class="icon" />
              </div>
              <div class="account-info">
                <div class="account-label">{{ account.label }}</div>
                <div class="account-amount">{{ account.amount }}</div>
                <div class="account-change" :class="{ positive: account.positive }">
                  {{ account.change }}
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Cash Flow Card -->
        <div class="stat-card cashflow-card">
          <div class="card-header">
            <span class="card-label">Cash Flow</span>
            <div class="legend">
              <span class="legend-item"><span class="dot income"></span> Income</span>
              <span class="legend-item"><span class="dot expends"></span> Expends</span>
            </div>
          </div>
          <div class="chart-area">
            <svg viewBox="0 0 200 80" class="line-chart">
              <path d="M 0 60 Q 20 45 40 50 T 80 35 Q 120 25 160 40 T 200 30" 
                    fill="none" 
                    stroke="url(#gradient-income)" 
                    stroke-width="3"/>
              <path d="M 0 65 Q 20 55 40 60 T 80 50 Q 120 45 160 55 T 200 50" 
                    fill="none" 
                    stroke="url(#gradient-expends)" 
                    stroke-width="3"/>
              <defs>
                <linearGradient id="gradient-income" x1="0%" y1="0%" x2="100%" y2="0%">
                  <stop offset="0%" style="stop-color:#8b5cf6;stop-opacity:1" />
                  <stop offset="100%" style="stop-color:#6366f1;stop-opacity:1" />
                </linearGradient>
                <linearGradient id="gradient-expends" x1="0%" y1="0%" x2="100%" y2="0%">
                  <stop offset="0%" style="stop-color:#3b82f6;stop-opacity:1" />
                  <stop offset="100%" style="stop-color:#06b6d4;stop-opacity:1" />
                </linearGradient>
              </defs>
            </svg>
          </div>
        </div>

      </div>
    </section>

    <!-- Features Section -->
    <section class="features" id="features">
      <h2 class="section-title">Powerful Features to Elevate Your Financial</h2>
      <p class="section-subtitle">All the tools you need to manage your money—smart, simple, and seamless.</p>
      
      <div class="features-grid">
        <div v-for="feature in features" :key="feature.title" class="feature-card">
          <div class="feature-icon">{{ feature.icon }}</div>
          <h3>{{ feature.title }}</h3>
          <p>{{ feature.description }}</p>
        </div>
      </div>

      <div class="feature-highlight">
        <div class="highlight-content">
          <h3>Comprehensive Financial Overview</h3>
          <p>View your total balance, income, and expenses at a glance to stay on top of your finances.</p>
        </div>
        <div class="highlight-icon">📊</div>
      </div>
    </section>

    <!-- Pricing Section -->
    <section class="pricing" id="pricing">
      <h2 class="section-title">Flexible Plans for Every Need</h2>
      <p class="section-subtitle">
        Choose a plan that fits your financial goals - whether you're an individual or a business.
      </p>
      
      <div class="pricing-grid">
        <div 
          v-for="plan in pricingPlans" 
          :key="plan.title" 
          class="pricing-card"
          :class="{ highlighted: plan.highlighted }"
        >
          <div class="pricing-header">
            <h3>{{ plan.title }}</h3>
            <p class="pricing-subtitle">{{ plan.subtitle }}</p>
            <div class="price">
              <span class="price-amount">{{ plan.price }}</span>
              <span class="price-period">/per month</span>
            </div>
          </div>
          
          <ul class="features-list">
            <li v-for="feature in plan.features" :key="feature">
              <span class="checkmark">✓</span>
              {{ feature }}
            </li>
          </ul>
          
          <button class="btn-pricing" :class="{ primary: plan.highlighted }">
            Get Started
          </button>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="cta">
      <h2>A Smarter Way to Manage Your Money</h2>
      <p>Built for professionals and businesses. BudgetBuddy provides seamless, secure, and intuitive financial management.</p>
      <button class="btn-cta">Start Free Trial</button>
    </section>

    <!-- Footer -->
    <footer class="footer">
      <div class="footer-content">
        <div class="footer-section">
          <div class="logo">
            <img src="../assets/Logo.png" alt="Logo" class="logo-icon" />
            <span>BudgetBuddy</span>
          </div>
          <p class="footer-description">Smart financial management for everyone.</p>
        </div>
        
        <div class="footer-section">
          <h4>Product</h4>
          <a href="#features">Features</a>
          <a href="#pricing">Pricing</a>
          <a href="#security">Security</a>
        </div>
        
        <div class="footer-section">
          <h4>Company</h4>
          <a href="#about">About</a>
          <a href="#blog">Blog</a>
          <a href="#careers">Careers</a>
        </div>
        
        <div class="footer-section">
          <h4>Support</h4>
          <a href="#help">Help Center</a>
          <a href="#contact">Contact</a>
          <a href="#privacy">Privacy</a>
        </div>
      </div>
      
      <div class="footer-bottom">
        <p>&copy; 2024 BudgetBuddy. All rights reserved.</p>
      </div>
    </footer>
  </div>
</template>

<style scoped>
.landing-container {
  max-width: 100%;
  min-height: 100vh;
  background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 50%, #0f0f0f 100%);
  color: #ffffff;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
}

/* Header */
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem 5%;
  border-bottom: 1px solid rgba(148, 147, 147, 0.5);
  position: sticky;
  top: 0;
  background: rgba(10, 10, 10, 0.8);
  backdrop-filter: blur(20px);
  z-index: 100;
  box-shadow: 0px 10px 15px rgba(148, 147, 147, 0.5);
}

.logo {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 1.3rem;
  font-weight: 700;
}

.logo-icon {
  width: 50px;
  height: 50px;
  border-radius: 8px;
  object-fit: contain;
  box-shadow: 0px 5px 5px rgba(148, 147, 147, 0.5);
}

.nav {
  display: flex;
  gap: 2rem;
}

.nav a {
  color: rgba(255, 255, 255, 0.7);
  text-decoration: none;
  transition: color 0.3s;
  font-size: 0.95rem;
}

.nav a:hover {
  color: #ffffff;
}

.header-buttons {
  display: flex;
  gap: 1rem;
}

.mobile-menu-btn {
  display: none;
  background: none;
  border: none;
  color: white;
  font-size: 1.5rem;
  cursor: pointer;
}

.mobile-menu {
  display: none;
  flex-direction: column;
  gap: 1rem;
  padding: 1.5rem 5%;
  background: rgba(10, 10, 10, 0.95);
  backdrop-filter: blur(20px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.mobile-menu a {
  color: rgba(255, 255, 255, 0.7);
  text-decoration: none;
  padding: 0.5rem 0;
}

.mobile-cta {
  width: 100%;
  margin-top: 1rem;
}

/* Buttons */
.btn-cta, .btn-small, .btn-link, .btn-pricing {
  padding: 0.75rem 1.8rem;
  border: none;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 0.95rem;
}

.btn-cta {
  background: white;
  color: #0a0a0a;
  padding: 1rem 2.5rem;
  font-size: 1.05rem;
}

.btn-cta:hover {
  transform: translateY(-2px);
  box-shadow: 0 15px 35px rgba(255, 255, 255, 0.3);
  background: #f0f0f0;
}

.btn-small {
  padding: 0.5rem 1rem;
  font-size: 0.85rem;
  background: rgba(99, 102, 241, 0.2);
  color: #6366f1;
}

.btn-link {
  background: none;
  color: rgba(255, 255, 255, 0.5);
  padding: 0;
}

.btn-pricing {
  width: 100%;
  background: rgba(255, 255, 255, 0.1);
  color: white;
}

.btn-pricing.primary {
  background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
}

.btn-pricing:hover {
  transform: translateY(-2px);
}

/* Hero Section */
.hero {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;
  padding: 3rem 5% 2rem;
  align-items: center;
}

.hero-content {
  max-width: 600px;
}

.hero-title {
  font-size: 4rem;
  font-weight: 800;
  line-height: 1.1;
  margin-bottom: 1.5rem;
}

.gradient-text {
  background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #a855f7 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-description {
  font-size: 1.15rem;
  color: rgba(255, 255, 255, 0.6);
  line-height: 1.7;
  margin-bottom: 2.5rem;
}

.hero-buttons {
  display: flex;
  justify-content: center;
  gap: 1.5rem;
}

/* Hero Visual */
.hero-visual {
  display: grid;
  gap: 1.5rem;
}

.stat-card {
  background: linear-gradient(135deg, rgba(30, 30, 30, 0.8) 0%, rgba(20, 20, 20, 0.6) 100%);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 16px;
  padding: 1.5rem;
  transition: transform 0.3s ease, border-color 0.3s ease;
}

.stat-card:hover {
  transform: translateY(-5px);
  border-color: rgba(99, 102, 241, 0.5);
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.card-label {
  font-weight: 600;
  font-size: 0.95rem;
  color: rgba(255, 255, 255, 0.8);
}

.card-amount {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
}

.card-change {
  font-size: 0.9rem;
  color: #10b981;
}

.card-change.positive {
  color: #10b981;
}

.accounts-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  margin-top: 1.5rem;
}

.account-item {
  display: flex;
  gap: 0.75rem;
}

.account-icon {
  width: 40px;
  height: 40px;
  border-radius: 8px;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.account-icon.income {
  background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
}

.account-icon.expends {
  background: linear-gradient(135deg, #3b82f6 0%, #06b6d4 100%);
}

.account-icon .icon {
  width: 20px;
  height: 20px;
  color: white;
}

.account-info {
  flex: 1;
}

.account-label {
  font-size: 0.85rem;
  color: rgba(255, 255, 255, 0.6);
  margin-bottom: 0.25rem;
}

.account-amount {
  font-size: 1.1rem;
  font-weight: 600;
  margin-bottom: 0.25rem;
}

.account-change {
  font-size: 0.8rem;
  color: #ef4444;
}

.account-change.positive {
  color: #10b981;
}

.legend {
  display: flex;
  gap: 1rem;
  font-size: 0.85rem;
}

.legend-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: rgba(255, 255, 255, 0.6);
}

.dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
}

.dot.income {
  background: #6366f1;
}

.dot.expends {
  background: #3b82f6;
}

.chart-area {
  margin-top: 1rem;
}

.line-chart {
  width: 100%;
  height: 80px;
}

.transactions-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.transaction-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.75rem 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}

.transaction-item:last-child {
  border-bottom: none;
}

.transaction-info {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.merchant {
  color: rgba(255, 255, 255, 0.9);
  font-weight: 500;
}

.category {
  font-size: 0.85rem;
  color: rgba(255, 255, 255, 0.5);
}

.amount {
  color: #ef4444;
  font-weight: 600;
}

/* Features Section */
.features {
  padding: 2rem 3;
}

.section-title {
  font-size: 3rem;
  font-weight: 700;
  text-align: center;
  margin-bottom: 1rem;
}

.section-subtitle {
  font-size: 1.1rem;
  color: rgba(255, 255, 255, 0.6);
  text-align: center;
  margin-bottom: 3rem;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  max-width: 1200px;
  margin: 0 auto 3rem;
}

.feature-card {
  background: linear-gradient(135deg, rgba(30, 30, 30, 0.6) 0%, rgba(20, 20, 20, 0.4) 100%);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 16px;
  padding: 2rem;
  transition: all 0.3s ease;
}

.feature-card:hover {
  transform: translateY(-5px);
  border-color: rgba(99, 102, 241, 0.5);
}

.feature-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.feature-card h3 {
  font-size: 1.3rem;
  margin-bottom: 0.75rem;
}

.feature-card p {
  color: rgba(255, 255, 255, 0.6);
  line-height: 1.6;
}

.feature-highlight {
  background: linear-gradient(135deg, rgba(99, 102, 241, 0.1) 0%, rgba(139, 92, 246, 0.1) 100%);
  border: 1px solid rgba(99, 102, 241, 0.3);
  border-radius: 16px;
  padding: 2.5rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1200px;
  margin: 0 auto;
}

.highlight-content h3 {
  font-size: 1.8rem;
  margin-bottom: 0.75rem;
}

.highlight-content p {
  color: rgba(255, 255, 255, 0.6);
  font-size: 1.05rem;
}

.highlight-icon {
  font-size: 4rem;
}

/* Pricing Section */
.pricing {
  padding: 2rem 5%;
  background: linear-gradient(180deg, transparent 0%, rgba(15, 15, 15, 0.5) 100%);
}

.pricing-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

.pricing-card {
  background: linear-gradient(135deg, rgba(30, 30, 30, 0.6) 0%, rgba(20, 20, 20, 0.4) 100%);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 16px;
  padding: 2.5rem;
  transition: all 0.3s ease;
}

.pricing-card.highlighted {
  background: linear-gradient(135deg, rgba(99, 102, 241, 0.2) 0%, rgba(139, 92, 246, 0.2) 100%);
  border: 2px solid rgba(99, 102, 241, 0.5);
  transform: scale(1.05);
}

.pricing-card:hover {
  transform: translateY(-5px);
}

.pricing-card.highlighted:hover {
  transform: scale(1.05) translateY(-5px);
}

.pricing-header {
  text-align: center;
  margin-bottom: 2rem;
  padding-bottom: 2rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.pricing-header h3 {
  font-size: 1.8rem;
  margin-bottom: 0.5rem;
}

.pricing-subtitle {
  color: rgba(255, 255, 255, 0.6);
  margin-bottom: 1.5rem;
}

.price {
  margin-top: 1rem;
}

.price-amount {
  font-size: 3rem;
  font-weight: 700;
}

.price-period {
  color: rgba(255, 255, 255, 0.5);
  font-size: 0.95rem;
}

.features-list {
  list-style: none;
  padding: 0;
  margin-bottom: 2rem;
}

.features-list li {
  padding: 0.75rem 0;
  color: rgba(255, 255, 255, 0.8);
  display: flex;
  align-items: start;
  gap: 0.75rem;
}

.checkmark {
  color: #10b981;
  font-weight: bold;
  flex-shrink: 0;
}

/* CTA Section */
.cta {
  padding: 3rem 5%;
  text-align: center;
  max-width: 800px;
  margin: 0 auto;
}

.cta h2 {
  font-size: 3rem;
  font-weight: 700;
  margin-bottom: 1.5rem;
}

.cta p {
  font-size: 1.15rem;
  color: rgba(255, 255, 255, 0.6);
  margin-bottom: 1rem;
}

/* Footer */
.footer {
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  padding: 0.5rem;
}

.footer-content {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 3rem;
  margin-bottom: 3rem;
  max-width: 1200px;
  margin: 0 auto 3rem;
}

.footer-section h4 {
  margin-bottom: 1rem;
  font-size: 1.1rem;
}

.footer-section a {
  display: block;
  color: rgba(255, 255, 255, 0.6);
  text-decoration: none;
  margin-bottom: 0.75rem;
  transition: color 0.3s;
}

.footer-section a:hover {
  color: #ffffff;
}

.footer-description {
  color: rgba(255, 255, 255, 0.6);
  margin-top: 1rem;
  line-height: 1.6;
}

.footer-bottom {
  text-align: center;
  padding-top: 2rem;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  color: rgba(255, 255, 255, 0.5);
}

/* Responsive */
@media (max-width: 968px) {
  .hero {
    grid-template-columns: 1fr;
    text-align: center;
  }
  
  .hero-content {
    margin: 0 auto;
  }
  
  .hero-buttons {
    justify-content: center;
  }
  
  .hero-title {
    font-size: 2.5rem;
  }
  
  .nav {
    display: none;
  }

  .mobile-menu-btn {
    display: block;
  }

  .mobile-menu {
    display: flex;
  }

  .feature-highlight {
    flex-direction: column;
    text-align: center;
    gap: 2rem;
  }

  .pricing-card.highlighted {
    transform: scale(1);
  }

  .section-title {
    font-size: 2rem;
  }
}

@media (max-width: 640px) {
  .hero-buttons {
    flex-direction: column;
    width: 100%;
  }
  
  .btn-cta {
    width: 100%;
  }
  
  .header-buttons {
    display: none;
  }

  .hero-title {
    font-size: 2rem;
  }

  .accounts-row {
    grid-template-columns: 1fr;
  }

  .pricing-grid {
    grid-template-columns: 1fr;
  }

  .cta h2 {
    font-size: 2rem;
  }

  .footer-content {
    grid-template-columns: 1fr;
    text-align: center;
  }

  .logo {
    font-size: 1.1rem;
  }

  .logo-icon {
    width: 28px;
    height: 28px;
  }
}
</style>