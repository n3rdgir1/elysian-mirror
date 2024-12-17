<template>
  <div class="flex flex-col h-full w-full">
    <div class="bg-gray-700 text-white p-4 fixed w-full">
      <h1 class="text-2xl text-left">Knowledge Base</h1>
    </div>
    <div class="flex-1 overflow-y-auto p-4 mt-16">
      <ul>
        <li v-for="item in knowledgeItems" :key="item.title" class="mb-4 text-left">
          <div @click="toggleDescription(item)" class="cursor-pointer">
            <h2 class="text-xl font-bold">{{ item.title }}</h2>
            <p v-if="item.showDescription" class="mt-2" v-html="formatDescription(item.description)"></p>
          </div>
        </li>
      </ul>
      <div v-if="knowledgeItems.length === 0" class="flex justify-center mt-4">
        <button @click="openAddKnowledgeModal" class="bg-blue-500 text-white p-2 rounded flex items-center">
          <i class="fas fa-plus"></i>
          <span class="ml-2">Add Knowledge</span>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'

export default {
  name: 'KnowledgeBase',
  setup() {
    const knowledgeItems = ref([])

    async function fetchKnowledgeItems() {
      try {
        const response = await fetch('http://127.0.0.1:5000/knowledge')
        if (!response.ok) {
          throw new Error('Failed to fetch knowledge items')
        }
        const data = await response.json()
        knowledgeItems.value = data.knowledge.map(item => ({
          ...item,
          showDescription: false
        }))
      } catch (error) {
        console.error('Error:', error)
      }
    }

    function toggleDescription(item) {
      item.showDescription = !item.showDescription
    }

    function formatDescription(description) {
      return description.replace(/\n/g, '<br>')
    }

    function openAddKnowledgeModal() {
      // Emit an event to open the Add Knowledge modal
      const event = new CustomEvent('open-add-knowledge-modal')
      window.dispatchEvent(event)
    }

    onMounted(fetchKnowledgeItems)

    return {
      knowledgeItems,
      toggleDescription,
      formatDescription,
      openAddKnowledgeModal
    }
  }
}
</script>

<style scoped>
/* Add any additional styling here if needed */
</style>
