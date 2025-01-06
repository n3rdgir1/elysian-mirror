<template>
  <div class="h-full w-full">
    <ChatWindow title="Search Knowledge" apiEndpoint="/rag" @server-message="handleServerMessage"/>
  </div>
</template>

<script>
import ChatWindow from '../components/ChatWindow.vue'

export default {
  name: 'SearchKnowledge',
  components: {
    ChatWindow
  },
  setup(props, {emit}) {
    function handleServerMessage({ message, type }) {
      emit('server-message', { message, type })
    }

    return {
      handleServerMessage
    }
  }
}
</script>

<style scoped>
/* Add any additional styling here if needed */
</style>
