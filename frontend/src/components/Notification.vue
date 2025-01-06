<template>
  <div :class="['notification', type]" @click="closeNotification">
    <i :class="iconClass"></i>
    <span>{{ message }}</span>
    <button @click.stop="closeNotification">x</button>
  </div>
</template>

<script>
export default {
  name: 'Notification',
  props: {
    message: {
      type: String,
      required: true
    },
    type: {
      type: String,
      required: true
    },
    id: {
      type: Number,
      required: true
    }
  },
  computed: {
    iconClass() {
      return this.type === 'success' ? 'fas fa-check-circle text-green-500' : 'fas fa-times-circle text-red-500';
    }
  },
  mounted() {
    this.autoClose();
  },
  methods: {
    closeNotification() {
      this.$emit('close', this.id);
    },
    autoClose() {
      setTimeout(() => {
        this.closeNotification();
      }, 5000);
    }
  }
}
</script>

<style scoped>
.notification {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem;
  margin: 1rem 0;
  border-radius: 0.5rem;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  cursor: pointer;
}
.notification.success {
  background-color: #d4edda;
  color: #155724;
}
.notification.error {
  background-color: #f8d7da;
  color: #721c24;
}
.notification i {
  margin-right: 0.5rem;
}
.notification button {
  background: none;
  border: none;
  font-size: 1.2rem;
  cursor: pointer;
}
</style>
