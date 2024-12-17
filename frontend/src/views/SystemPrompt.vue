<template>
  <div class="flex flex-col h-full w-full">
    <div class="bg-gray-700 text-white p-4 fixed w-full">
      <h1 class="text-2xl">System Prompt</h1>
    </div>
    <div class="flex-1 overflow-y-auto p-4 mt-16">
      <form @submit.prevent="saveSystemPrompt">
        <div class="mb-4">
          <label for="systemPrompt" class="block text-gray-700">System Prompt</label>
          <textarea id="systemPrompt" v-model="systemPrompt" class="mt-1 block w-full p-2 border rounded" rows="5"></textarea>
        </div>
        <button type="submit" class="bg-blue-500 text-white p-2 rounded">Save</button>
      </form>
      <div v-if="errorMessage" class="mt-4 text-red-500">{{ errorMessage }}</div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'

export default {
  name: 'SystemPrompt',
  setup() {
    const systemPrompt = ref('')
    const errorMessage = ref('')

    async function fetchSystemPrompt() {
      try {
        const response = await fetch('http://127.0.0.1:5000/system_prompt')
        if (!response.ok) {
          throw new Error('Failed to fetch system prompt')
        }
        const data = await response.json()
        systemPrompt.value = data.system_prompt
      } catch (error) {
        errorMessage.value = 'Error: ' + error.message
      }
    }

    async function saveSystemPrompt() {
      try {
        const response = await fetch('http://127.0.0.1:5000/system_prompt', {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ description: systemPrompt.value })
        })
        if (!response.ok) {
          throw new Error('Failed to save system prompt')
        }
        errorMessage.value = ''
      } catch (error) {
        errorMessage.value = 'Error: ' + error.message
      }
    }

    onMounted(fetchSystemPrompt)

    return {
      systemPrompt,
      errorMessage,
      saveSystemPrompt
    }
  }
}
</script>

<style scoped>
/* Add any additional styling here if needed */
</style>
