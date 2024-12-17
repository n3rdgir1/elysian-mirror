<template>
  <div class="p-4">
    <h1 class="text-2xl mb-4">Knowledge Base</h1>
    <ul>
      <li v-for="item in knowledgeItems" :key="item.title" class="mb-4">
        <div @click="toggleDescription(item)" class="cursor-pointer">
          <h2 class="text-xl font-bold">{{ item.title }}</h2>
          <p v-if="item.showDescription" class="mt-2">{{ item.description }}</p>
        </div>
      </li>
    </ul>
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

    onMounted(fetchKnowledgeItems)

    return {
      knowledgeItems,
      toggleDescription
    }
  }
}
</script>

<style scoped>
/* Add any additional styling here if needed */
</style>
