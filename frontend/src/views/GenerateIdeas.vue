<template>
  <div class="h-full w-full">
    <ChatWindow title="Generate Ideas" apiEndpoint="/generate" />
  </div>
</template>

<script>
import ChatWindow from '../components/ChatWindow.vue'

export default {
  name: 'GenerateIdeas',
  components: {
    ChatWindow
  }
}
</script>

<style scoped>
/* Add any additional styling here if needed */
</style>
