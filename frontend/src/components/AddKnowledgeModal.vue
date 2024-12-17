<template>
  <div class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
    <div class="bg-white p-6 rounded shadow-lg w-1/3">
      <h2 class="text-2xl mb-4">Add Knowledge</h2>
      <form @submit.prevent="handleSubmit">
        <div class="mb-4">
          <label for="title" class="block text-gray-700">Title</label>
          <input v-model="title" id="title" type="text" class="mt-1 block w-full p-2 border rounded" />
          <span v-if="errors.title" class="text-red-500">{{ errors.title }}</span>
        </div>
        <div class="mb-4">
          <label for="description" class="block text-gray-700">Description</label>
          <textarea v-model="description" id="description" class="mt-1 block w-full p-2 border rounded" rows="5"></textarea>
          <span v-if="errors.description" class="text-red-500">{{ errors.description }}</span>
        </div>
        <div class="flex justify-end">
          <button type="button" @click="$emit('close')" class="bg-gray-500 text-white p-2 rounded mr-2">Cancel</button>
          <button type="submit" :disabled="isLoading" class="bg-blue-500 text-white p-2 rounded">
            <span v-if="isLoading">Loading...</span>
            <span v-else>Submit</span>
          </button>
        </div>
      </form>
      <div v-if="apiResponse" class="mt-4">
        <p>{{ apiResponse.message }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'

export default {
  name: 'AddKnowledgeModal',
  setup() {
    const title = ref('')
    const description = ref('')
    const errors = ref({})
    const isLoading = ref(false)
    const apiResponse = ref(null)

    function validateForm() {
      errors.value = {}
      if (!title.value) {
        errors.value.title = 'Title is required'
      }
      if (!description.value) {
        errors.value.description = 'Description is required'
      }
      return Object.keys(errors.value).length === 0
    }

    async function handleSubmit() {
      if (!validateForm()) {
        return
      }

      isLoading.value = true
      try {
        const response = await fetch('http://127.0.0.1:5000/embed', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ title: title.value, description: description.value })
        })

        if (!response.ok) {
          throw new Error('Network response was not ok')
        }

        const data = await response.json()
        apiResponse.value = data
        title.value = ''
        description.value = ''
      } catch (error) {
        apiResponse.value = { message: 'Error: ' + error.message }
      } finally {
        isLoading.value = false
      }
    }

    return {
      title,
      description,
      errors,
      isLoading,
      apiResponse,
      handleSubmit
    }
  }
}
</script>

<style scoped>
/* Add any additional styling here if needed */
</style>
