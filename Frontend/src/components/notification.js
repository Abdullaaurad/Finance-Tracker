// customNotification.js
import { notification } from 'ant-design-vue';

// Inject custom styles matching your app's glassmorphism theme
const styleId = 'glass-notification-styles';
if (!document.getElementById(styleId)) {
  const style = document.createElement('style');
  style.id = styleId;
  style.textContent = `
    .glass-notification {
      background: linear-gradient(135deg, rgba(30, 30, 30, 0.53) 0%, rgba(20, 20, 20, 0.16) 100%) !important;
      backdrop-filter: blur(20px) saturate(180%) !important;
      -webkit-backdrop-filter: blur(20px) saturate(180%) !important;
      border: 2px solid rgba(216, 196, 255, 0.4) !important;
      border-radius: 16px !important;
      box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5), 0 0 0 1px rgba(255, 255, 255, 0.05) inset !important;
      padding: 20px 24px !important;
      overflow: hidden !important;
    }

    .glass-notification::before {
      content: '' !important;
      position: absolute !important;
      top: 0 !important;
      left: 0 !important;
      right: 0 !important;
      height: 3px !important;
      background: linear-gradient(90deg, rgba(216, 196, 255, 0.8), rgba(99, 102, 241, 0.8)) !important;
    }

    .glass-notification .ant-notification-notice-message {
      color: #ffffff !important;
      font-weight: 600 !important;
      font-size: 16px !important;
      margin-bottom: 8px !important;
      margin-top: 0 !important;
    }

    .glass-notification .ant-notification-notice-description {
      color: #94a3b8 !important;
      font-size: 14px !important;
      line-height: 1.6 !important;
    }

    .glass-notification .ant-notification-notice-icon {
      font-size: 24px !important;
      margin-top: 2px !important;
    }

    .glass-notification .ant-notification-notice-close {
      color: rgba(255, 255, 255, 0.5) !important;
      transition: all 0.3s ease !important;
      top: 20px !important;
      right: 20px !important;
    }

    .glass-notification .ant-notification-notice-close:hover {
      color: #ffffff !important;
      transform: scale(1.1) !important;
    }

    /* Icon colors for different types */
    .glass-notification-success .ant-notification-notice-icon {
      color: #10b981 !important;
    }

    .glass-notification-success::before {
      background: linear-gradient(90deg, rgba(16, 185, 129, 0.8), rgba(5, 150, 105, 0.8)) !important;
    }

    .glass-notification-info .ant-notification-notice-icon {
      color: #6366f1 !important;
    }

    .glass-notification-info::before {
      background: linear-gradient(90deg, rgba(99, 102, 241, 0.8), rgba(79, 70, 229, 0.8)) !important;
    }

    .glass-notification-warning .ant-notification-notice-icon {
      color: #f59e0b !important;
    }

    .glass-notification-warning::before {
      background: linear-gradient(90deg, rgba(245, 158, 11, 0.8), rgba(217, 119, 6, 0.8)) !important;
    }

    .glass-notification-error .ant-notification-notice-icon {
      color: #ef4444 !important;
    }

    .glass-notification-error::before {
      background: linear-gradient(90deg, rgba(239, 68, 68, 0.8), rgba(220, 38, 38, 0.8)) !important;
    }

    /* Smooth animations */
    .glass-notification {
      animation: slideInRight 0.5s cubic-bezier(0.16, 1, 0.3, 1) !important;
    }

    @keyframes slideInRight {
      from {
        opacity: 0;
        transform: translate3d(100%, 0, 0) scale(0.95);
      }
      to {
        opacity: 1;
        transform: translate3d(0, 0, 0) scale(1);
      }
    }

    /* Subtle hover effect */
    .glass-notification:hover {
      border-color: rgba(216, 196, 255, 0.6) !important;
      box-shadow: 0 25px 70px rgba(0, 0, 0, 0.6), 0 0 0 1px rgba(255, 255, 255, 0.08) inset !important;
    }
  `;
  document.head.appendChild(style);
}

// Custom notification functions with glassmorphism theme
export const glassNotification = {
  success(config) {
    notification.success({
      ...config,
      class: 'glass-notification glass-notification-success',
      placement: config.placement || 'topRight',
      duration: config.duration || 4.5,
    });
  },

  error(config) {
    notification.error({
      ...config,
      class: 'glass-notification glass-notification-error',
      placement: config.placement || 'topRight',
      duration: config.duration || 4.5,
    });
  },

  info(config) {
    notification.info({
      ...config,
      class: 'glass-notification glass-notification-info',
      placement: config.placement || 'topRight',
      duration: config.duration || 4.5,
    });
  },

  warning(config) {
    notification.warning({
      ...config,
      class: 'glass-notification glass-notification-warning',
      placement: config.placement || 'topRight',
      duration: config.duration || 4.5,
    });
  },

  open(config) {
    notification.open({
      ...config,
      class: `glass-notification ${config.class || ''}`,
      placement: config.placement || 'topRight',
      duration: config.duration || 4.5,
    });
  },
};

// Example usage in your components:
/*
import { glassNotification } from './customNotification';

// Success notification
glassNotification.success({
  message: 'Signup Successful',
  description: 'Your account has been created. Please log in.',
});

// Error notification
glassNotification.error({
  message: 'Validation Error',
  description: 'Please fix the errors before submitting.',
});

// Info notification
glassNotification.info({
  message: 'Information',
  description: 'This is an informational message.',
});

// Warning notification
glassNotification.warning({
  message: 'Warning',
  description: 'Please be careful with this action.',
});

// Custom notification with different placement and duration
glassNotification.success({
  message: 'Success',
  description: 'Operation completed successfully.',
  placement: 'bottomRight',
  duration: 3,
});
*/