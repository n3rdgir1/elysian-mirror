<template>
  <div class="h-full w-full">
    <ChatWindow
      title="Generate Ideas"
      apiEndpoint="/generate"
      @add-to-knowledge="openAddKnowledgeModal"
      :showAddToKnowledgeButton="true"
      @server-message="handleServerMessage"
      />
    <AddKnowledgeModal
      v-if="isAddKnowledgeModalOpen"
      @close="closeAddKnowledgeModal"
      :initialTitle="knowledgeTitle"
      :initialDescription="knowledgeDescription"
      @server-message="handleServerMessage"
    />
  </div>
</template>

<script>
import ChatWindow from '../components/ChatWindow.vue'
import AddKnowledgeModal from '../components/AddKnowledgeModal.vue'
import { ref } from 'vue'

export default {
  name: 'GenerateIdeas',
  components: {
    ChatWindow,
    AddKnowledgeModal
  },
  setup(props, {emit}) {
    const isAddKnowledgeModalOpen = ref(false)
    const knowledgeTitle = ref('')
    const knowledgeDescription = ref('')

    function openAddKnowledgeModal({ botMessage, userMessage }) {
      knowledgeTitle.value = userMessage.text
      knowledgeDescription.value = botMessage.text
      isAddKnowledgeModalOpen.value = true
    }

    function closeAddKnowledgeModal() {
      isAddKnowledgeModalOpen.value = false
    }

    function handleServerMessage({ message, type }) {
      emit('server-message', { message, type })
    }

    return {
      isAddKnowledgeModalOpen,
      knowledgeTitle,
      knowledgeDescription,
      openAddKnowledgeModal,
      closeAddKnowledgeModal,
      handleServerMessage
    }
  }
}
</script>

<style scoped>
/* Add any additional styling here if needed */
</style>
