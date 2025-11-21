<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import Input from '../components/input.vue'
import Button from '../components/Button.vue'
import { SignupUrl } from '../Constant/Url'
import { notification, Spin } from 'ant-design-vue'
import { usernamevalidator, emailvalidator, passwordvalidator } from '../utils/validators'
import { useMutation } from '@tanstack/vue-query'

const router = useRouter()
const username = ref<string>('')
const email = ref<string>('')
const password = ref<string>('')
const confirmPassword = ref<string>('')
const usernameError = ref<string>('')
const emailError = ref<string>('')
const passwordError = ref<string>('')
const confirmPasswordError = ref<string>('')
const loading = ref<boolean>(false)

const handleSignup = async () => {
  // Reset errors
  usernameError.value = '';
  emailError.value = '';
  passwordError.value = '';
  confirmPasswordError.value = '';

  // Validate inputs
  usernameError.value = usernamevalidator(username.value) ? '' : 'Invalid username';
  emailError.value = emailvalidator(email.value) ? '' : 'Invalid email';
  passwordError.value = passwordvalidator(password.value) ? '' : 'Invalid password';
  confirmPasswordError.value =
    password.value === confirmPassword.value ? '' : 'Passwords do not match';

  // If any errors, stop
  if (usernameError.value || emailError.value || passwordError.value || confirmPasswordError.value) {
    notification.error({
      message: 'Validation Error',
      description: 'Please fix the errors before submitting.',
      placement: 'topRight',
    });
    return;
  }

  loading.value = true;

  try {
    const response = await fetch(SignupUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        username: username.value,
        email: email.value,
        password: password.value,
      }),
    });

    if (response.ok) {
      notification.success({
        message: 'Signup Successful',
        description: 'Your account has been created. Please log in.',
        placement: 'topRight',
      });
      router.push('/login');
    } else {
      const data = await response.json();
      notification.error({
        message: 'Signup Failed',
        description: data.message || 'An error occurred during signup.',
        placement: 'topRight',
      });
    }
  } catch (error: any) {
    notification.error({
      message: 'Signup Failed',
      description: error.message || 'An unexpected error occurred.',
      placement: 'topRight',
    });
  } finally {
    loading.value = false;
  }
};

const handleSocialSignup = (provider: string) => {
  // TODO: Implement social signup logic
  console.log('Social signup with:', provider)
}

const goToLogin = () => {
  router.push('/login')
}

</script>

<template>
  <div class="signup-wrapper">
    <div class="signup-container">
      <h1 class="title">Create Account</h1>
      <p class="subtitle">
        Join us and take control of your financial future.
      </p>

      <form @submit.prevent="handleSignup">
        <div class="form-group">
          <Input
            v-model="username"
            type="string"
            placeholder="Enter a username"
            :required="true"
          />
          <span v-if="usernameError" class="error-message">
            {{ usernameError }}
          </span>
        </div>

        <div class="form-group">
          <Input
            v-model="email"
            type="email"
            placeholder="Enter your email address"
            :required="true"
          />
          <span v-if="emailError" class="error-message">
            {{ emailError }}
          </span>
        </div>

        <div class="form-group">
          <Input
            id="Password"
            v-model="password"
            type="password"
            placeholder="Enter your password"
            :required="true"
            :passwordToggle="true"
          />
          <span v-if="passwordError" class="error-message">
            {{ passwordError }}
          </span>
        </div>

        <div class="form-group">
          <Input
            id="confirmPassword"
            v-model="confirmPassword"
            type="password"
            placeholder="Confirm your password"
            :required="true"
            :passwordToggle="true"
          />
          <span v-if="confirmPasswordError" class="error-message">
            {{ confirmPasswordError }}
          </span>
        </div>
        <Button :disabled="loading" variant="secondary">
          <Spin v-if="loading" />
          <span v-else>Create Account</span>
        </Button>
      </form>

      <div class="divider">
        <div class="social-buttons">
          <button 
            type="button" 
            class="social-button"
            @click="handleSocialSignup('facebook')"
          >
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/>
            </svg>
            Facebook
          </button>
          <button 
            type="button" 
            class="social-button"
            @click="handleSocialSignup('google')"
          >
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4"/>
              <path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853"/>
              <path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" fill="#FBBC05"/>
              <path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#EA4335"/>
            </svg>
              Google
          </button>
          <button 
            type="button" 
            class="social-button"
            @click="handleSocialSignup('apple')"
          >
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M17.05 20.28c-.98.95-2.05.8-3.08.35-1.09-.46-2.09-.48-3.24 0-1.44.62-2.2.44-3.06-.35C2.79 15.25 3.51 7.59 9.05 7.31c1.35.07 2.29.74 3.08.8 1.18-.24 2.31-.93 3.57-.84 1.51.12 2.65.72 3.4 1.8-3.12 1.87-2.38 5.98.48 7.13-.57 1.5-1.31 2.99-2.54 4.09l.01-.01zM12.03 7.25c-.15-2.23 1.66-4.07 3.74-4.25.29 2.58-2.34 4.5-3.74 4.25z"/>
            </svg>
            Apple
          </button>
        </div>
      </div>

      <p class="login-text">
        Already have an account?
        <button @click="goToLogin" class="link-button">Log in</button>
      </p>
    </div>
  </div>
</template>

<style scoped>
* {
  box-sizing: border-box;
}

.signup-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 50%, #0f0f0f 100%);
  padding: 20px;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
}

.signup-container {
  width: 100%;
  max-width: 420px;
  padding: 40px 32px;
  background: linear-gradient(135deg, rgba(30, 30, 30, 0.8) 0%, rgba(20, 20, 20, 0.6) 100%);
  backdrop-filter: blur(20px);
  border: 2px solid rgba(216, 196, 255, 0.4);
  border-radius: 20px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
}

.title {
  font-size: 32px;
  font-weight: 600;
  color: #ffffff;
  margin: 0 0 6px 0;
  text-align: center;
}

.subtitle {
  font-size: 14px;
  color: #94a3b8;
  line-height: 1.6;
  text-align: center;
  margin: 0 0 20px 0;
}

.form-group {
  margin-bottom: 16px;
}

.divider {
  margin: 28px 0;
}

.social-buttons {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
}

.social-button {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 14px 8px;
  background: rgba(15, 23, 42, 0.6);
  border: 1px solid  rgba(216, 196, 255, 0.4);
  border-radius: 12px;
  color: #e2e8f0;
  font-size: 13px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
  width: 100%;
}

.social-button:hover {
  background: rgba(15, 23, 42, 0.8);
  border-color:  rgba(216, 196, 255, 0.6);
  transform: translateY(-2px);
}

.social-button svg {
  flex-shrink: 0;
}

.login-text {
  text-align: center;
  color: #94a3b8;
  font-size: 14px;
  margin: 10px 0 0 0;
}

.link-button {
  background: none;
  border: none;
  color: #6366f1;
  font-weight: 500;
  cursor: pointer;
  padding: 0;
  font-size: 14px;
  transition: color 0.2s;
  width: auto;
}

.link-button:hover {
  text-decoration: underline;
}

.error-message {
    display: block;
    color: #ef4444;
    font-size: 14px;
    margin-top: 6px;
    margin-left: 4px;
  }

@media (max-width: 480px) {
  .signup-container {
    padding: 32px 24px;
  }

  .title {
    font-size: 28px;
  }

  .subtitle {
    font-size: 13px;
  }

  .social-buttons {
    grid-template-columns: 1fr;
  }

  .social-button {
    flex-direction: row;
    justify-content: flex-start;
    padding: 12px 16px;
  }
}
</style>