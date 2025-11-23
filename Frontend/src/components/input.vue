<script setup lang="ts">
import { ref, computed } from 'vue'
import {
    AtSymbolIcon,
    EyeIcon,
    EyeSlashIcon,
    LockClosedIcon,
    UserIcon,
    PhoneIcon,
    IdentificationIcon
} from '@heroicons/vue/24/outline'

interface Props {
    type: string,
    modelValue: string,
    placeholder: string,
    required?: boolean,
    passwordToggle?: boolean,
    id?: string
}

const props = defineProps<Props>()

const emit = defineEmits<{
    'update:modelValue': [value: string]
}>()

// State for password visibility toggle
const isPasswordVisible = ref(false)

// Computed property to determine the actual input type
const actualInputType = computed(() => {
    if (props.type === 'password' && props.passwordToggle) {
        return isPasswordVisible.value ? 'text' : 'password'
    }
    return props.type
})

// Method to toggle password visibility
const togglePasswordVisibility = () => {
    isPasswordVisible.value = !isPasswordVisible.value
}

// Computed property to determine the appropriate icon component
const InputIcon = computed(() => {
    switch (props.type) {
        case 'email':
            return AtSymbolIcon
        case 'password':
            return LockClosedIcon
        case 'text':
            return UserIcon
        case 'tel':
            return PhoneIcon
        case 'id':
            return IdentificationIcon
        default:
            return UserIcon
    }
})
</script>

<template>
    <div class="input-wrapper">
        <!-- Dynamic icon based on input type -->
        <component :is="InputIcon" class="input-icon" width="18" height="18" />
        
        <input
            :id="id || type"
            :type="actualInputType"
            :placeholder="placeholder"
            :required="required"
            :value="modelValue"
            :class="{ 'password-toggle': passwordToggle && type === 'password' }"
            @input="emit('update:modelValue', ($event.target as HTMLInputElement).value)"
        />
        <button
            v-if="passwordToggle && type === 'password'"
            class="toggle-password"
            type="button"
            @click="togglePasswordVisibility"
            :aria-label="isPasswordVisible ? 'Hide password' : 'Show password'"
        >
            <!-- Eye icon (when password is hidden) -->
            <EyeIcon v-if="!isPasswordVisible" width="18" height="18" />
            <!-- Eye-off icon (when password is visible) -->
            <EyeSlashIcon v-else width="18" height="18" />
        </button>
    </div>
</template>

<style scoped>
    .input-wrapper {
        position: relative;
        display: flex;
        align-items: center;
    }

    .input-icon {
        position: absolute;
        left: 16px;
        color: #64748b;
        pointer-events: none;
        z-index: 1;
        width: 18px;
        height: 18px;
        flex-shrink: 0;
    }

    input {
        width: 100%;
        padding: 14px 48px 14px 48px;
        background: rgba(15, 23, 42, 0.6);
        border: 2px solid rgba(216, 196, 255, 0.2);
        border-radius: 12px;
        color: #ffffff;
        font-size: 15px;
        transition: all 0.3s ease;
        outline: none;
    }

    input:not(.password-toggle) {
        padding-right: 16px;
    }

    input::placeholder {
        color: #64748b;
    }

    input:focus {
        border: 2px solid rgba(216, 196, 255, 0.6);
        background: rgba(15, 23, 42, 0.8);
        box-shadow: 0 0 0 3x rgba(216, 196, 255, 0.1);
        padding: 14px 48px 14px 48px;
    }

    .toggle-password {
        position: absolute;
        right: 12px;
        background: none;
        border: none;
        color: #64748b;
        cursor: pointer;
        padding: 6px;
        display: flex;
        align-items: center;
        justify-content: center;
        transition: color 0.2s ease;
        width: auto;
        height: auto;
        border-radius: 6px;
    }

    .toggle-password svg {
        width: 18px;
        height: 18px;
        flex-shrink: 0;
    }

    .toggle-password:hover {
        color: #3b82f6;
        background: rgba(59, 130, 246, 0.1);
    }

    .toggle-password:focus {
        outline: 2px solid #3b82f6;
        outline-offset: 2px;
    }
</style>