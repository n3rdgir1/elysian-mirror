<template>
  <div class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
    <div class="bg-white p-6 rounded shadow-lg w-1/3">
      <h2 class="text-2xl mb-4">Delete Confirmation</h2>
      <p>Are you sure you want to delete this knowledge item?</p>
      <p v-if="message" class="mt-4 text-red-500">{{ message }}</p>
      <div class="flex justify-end mt-4">
        <button @click="handleCancel" class="bg-gray-500 text-white p-2 rounded mr-2">Cancel</button>
        <button @click="handleConfirm" class="bg-red-500 text-white p-2 rounded">Confirm</button>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'

export default {
  name: 'DeleteConfirmationModal',
  props: {
    knowledgeItem: {
      type: Object,
      required: true
    }
  },
  setup(props, { emit }) {
    const isLoading = ref(false)
    const message = ref('')

    function handleCancel() {
      emit('close')
    }

    async function handleConfirm() {
      isLoading.value = true
      message.value = ''
      try {
        const response = await fetch('http://127.0.0.1:5000/delete_knowledge', {
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
        emit('confirm')
      } catch (error) {
        console.error('Error:', error)
        message.value = error.message
      } finally {
        isLoading.value = false
      }
    }

    return {
      handleCancel,
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
