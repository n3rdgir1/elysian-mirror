<template>
  <div class="flex flex-col h-full w-full">
    <div class="bg-gray-700 text-white p-4 fixed w-full">
      <h2 class="text-xl text-left">{{ title }}</h2>
    </div>
    <div class="flex-1 overflow-y-auto p-4 mt-16">
      <div v-for="(message, index) in messages" :key="index" class="mb-2">
        <div :class="{'text-right': message.isUser, 'text-left': !message.isUser}">
          <span :class="{'bg-blue-500 text-white': message.isUser, 'bg-gray-300': !message.isUser}" class="inline-block p-2 rounded">
            <i v-if="message.isUser" class="fas fa-user"></i>
            <i v-else class="fas fa-robot"></i>
            <span v-html="formatMessage(message.text)"></span>
            <div v-if="message.sources && message.sources.length > 0" class="mt-2">
              <h3 class="text-lg font-bold">Sources:</h3>
              <ul>
                <li v-for="(source, sourceIndex) in message.sources" :key="sourceIndex" class="cursor-pointer" @click="toggleDescription(source)">
                  <span class="text-blue-500">{{ source.title }}</span>
                  <p v-if="source.showDescription" class="mt-1">{{ source.description }}</p>
                </li>
              </ul>
            </div>
          </span>
          <button v-if="!message.isUser && showAddToKnowledgeButton" @click="addToKnowledge(message, messages[index - 1])" class="ml-2 p-1 bg-green-500 text-white rounded float-right" title="Add to Knowledge">
            <i class="fas fa-plus"></i>
          </button>
        </div>
      </div>
    </div>
    <div class="p-4 bg-gray-100 flex">
      <input v-model="newMessage" @keyup.enter="sendMessage" class="flex-1 p-2 border rounded" type="text" placeholder="Type a message...">
      <button @click="sendMessage" class="ml-2 p-2 bg-blue-500 text-white rounded">
        <i class="fas fa-paper-plane"></i> Send
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ChatWindow',
  props: {
    title: String,
    apiEndpoint: String,
    showAddToKnowledgeButton: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      messages: [],
      newMessage: ''
    }
  },
  methods: {
    async sendMessage() {
      if (this.newMessage.trim() === '') return;

      const userMessage = {
        text: this.newMessage,
        isUser: true
      };
      this.messages.push(userMessage);
      this.newMessage = '';

      try {
        const response = await fetch('http://127.0.0.1:5012' + this.apiEndpoint, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ prompt: userMessage.text })
        });

        const data = await response.json();
        const botMessage = {
          text: data.response || data.answer,
          isUser: false,
          sources: data.sources || []
        };
        this.messages.push(botMessage);
      } catch (error) {
        this.$emit('server-message', { message: 'Failed to send message', type: 'error' });
      }
    },
    addToKnowledge(botMessage, userMessage) {
      this.$emit('add-to-knowledge', { botMessage, userMessage });
    },
    formatMessage(message) {
      return message.replace(/\n/g, '<br>')
    },
    toggleDescription(source) {
      source.showDescription = !source.showDescription;
    }
  }
}
</script>

<style scoped>
/* Add any additional styling here if needed */
</style>
