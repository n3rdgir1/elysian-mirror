<template>
  <div class="h-full w-full">
    <ChatWindow title="Search Knowledge" apiEndpoint="/rag" />
  </div>
</template>

<script>
import ChatWindow from '../components/ChatWindow.vue'

export default {
  name: 'SearchKnowledge',
  components: {
    ChatWindow
  }
}
</script>

<style scoped>
/* Add any additional styling here if needed */
</style>
