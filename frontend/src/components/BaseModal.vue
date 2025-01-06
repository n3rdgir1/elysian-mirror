<template>
  <div class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50" @click.self="closeModal" @keydown.esc="closeModal" tabindex="0">
    <div class="bg-white p-6 rounded shadow-lg w-1/3 relative">
      <button @click="closeModal" class="absolute top-2 right-2 text-gray-500 hover:text-gray-700">
        <i class="fas fa-times"></i>
      </button>
      <slot></slot>
      <div class="mt-4 flex justify-start button-container">
        <button v-if="confirm_text" @click="confirmAction" class="bg-blue-500 text-white p-2 rounded mr-2" ref="confirmButton">{{ confirm_text }}</button>
        <button v-if="cancel_text" @click="closeModal" class="bg-gray-500 text-white p-2 rounded mr-2" ref="cancelButton">{{ cancel_text }}</button>
      </div>
      <div v-if="serverMessage" class="mt-4 text-blue-500">{{ serverMessage }}</div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'

export default {
  name: 'BaseModal',
  props: {
    confirm_text: {
      type: String,
      default: ''
    },
    cancel_text: {
      type: String,
      default: ''
    },
    serverMessage: {
      type: String,
      default: ''
    }
  },
  setup(props, { emit }) {
    const confirmButton = ref(null)
    const cancelButton = ref(null)
    const closeButton = ref(null)

    function closeModal() {
      emit('close')
    }

    function confirmAction() {
      emit('confirm')
    }

    onMounted(() => {
      if (confirmButton.value) {
        confirmButton.value.focus()
      } else if (cancelButton.value) {
        cancelButton.value.focus()
      } else if (closeButton.value) {
        closeButton.value.focus()
      }
    })

    return {
      closeModal,
      confirmAction,
      confirmButton,
      cancelButton,
      closeButton
    }
  }
}
</script>

<style scoped>
.button-container {
  display: flex;
  flex-direction: row-reverse;
}
/* Add any additional styling here if needed */
</style>
