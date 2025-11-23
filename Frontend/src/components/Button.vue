<script setup lang="ts">
import { computed } from 'vue'
import Colors from '../Constant/Colors'

interface Props {
  variant?: 'primary' | 'secondary' | 'cta' | 'small' | 'link' | 'pricing'
  disabled?: boolean
  primary?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  variant: 'primary',
  disabled: false,
  primary: false
})

const buttonClass = computed(() => {
  return `btn-${props.variant}${props.primary ? ' primary' : ''}`
})
</script>

<template>
  <button :class="buttonClass" @click="$emit('click')" :disabled="disabled">
    <slot></slot>
  </button>
</template>

<style scoped>
.btn-primary, .btn-cta, .btn-small, .btn-link, .btn-pricing, .btn-secondary {
  padding: 0.75rem 1.8rem;
  border: none;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 0.95rem;
}

.btn-primary {
  background: linear-gradient(90deg, rgba(172, 172, 172, 0.7)0%, rgba(87, 87, 87, 0.5) 100%);
  backdrop-filter: blur(20px);
  color: --var(--primary-0);
  box-shadow: 0 4px 10px rgba(174, 174, 174, 0.6);
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 25px rgba(174, 174, 174, 0.7);
}

.btn-secondary {
  margin-top: 10px;
  width: 100%;
  background: #6366f1;
  color: #ffffff;
}

.btn-secondary:hover {
  background: #6366f1;
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(99, 102, 241, 0.6);
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
  backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: white;
}

.btn-pricing.primary {
  background: linear-gradient(135deg, var(--primary-500) 0%, var(--primary-600) 100%);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.btn-pricing:hover {
  transform: translateY(-2px);
}
</style>