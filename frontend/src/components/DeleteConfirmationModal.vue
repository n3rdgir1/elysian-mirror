<template>
  <BaseModal
    confirm_text="Confirm"
    cancel_text="Cancel"
    :serverMessage="message"
    @close="$emit('close')"
    @confirm="handleConfirm"
    @server-message="$emit('server-message', $event)"
  >
  <p>Are you sure you want to delete this knowledge item?</p>
  </BaseModal>
</template>

<script>
import { ref } from 'vue'
import BaseModal from './BaseModal.vue'

export default {
  name: 'DeleteConfirmationModal',
  components: {
    BaseModal
  },
  props: {
    knowledgeItem: {
      type: Object,
      required: true
    }
  },
  setup(props, { emit }) {
    const isLoading = ref(false)
    const message = ref('')

    async function handleConfirm() {
      isLoading.value = true
      message.value = ''
      try {
        const response = await fetch('http://127.0.0.1:5012/delete_knowledge', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ id: props.knowledgeItem.id })
        })

        const data = await response.json()

        if (!response.ok) {
          throw new Error(data.message || 'Failed to delete knowledge item')
        }

        message.value = data.message || 'Knowledge item deleted successfully'
        emit('server-message', { message: data.message || 'Knowledge item deleted successfully', type: 'success' })

        emit('confirm', props.knowledgeItem.id)
        emit('close')

      } catch (error) {
        console.error('Error:', error)
        message.value = error.message
        emit('server-message', { message: error.message, type: 'error' })
      } finally {
        isLoading.value = false
      }
    }

    return {
      handleConfirm,
      isLoading,
      message
    }
  }
}
</script>

<style scoped>
/* Add any additional styling here if needed */
</style>
