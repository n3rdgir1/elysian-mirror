<template>
  <div class="flex flex-col h-full w-full">
    <div class="bg-gray-700 text-white p-4 fixed w-full">
      <h2 class="text-xl text-left">{{ title }}</h2>
    </div>
    <div class="flex-1 overflow-y-auto p-4 mt-16">
      <div v-for="(message, index) in messages" :key="index" class="mb-2">
        <div :class="{'text-right': message.isUser}">
          <span :class="{'bg-blue-500 text-white': message.isUser, 'bg-gray-300': !message.isUser}" class="inline-block p-2 rounded">
            <i v-if="message.isUser" class="fas fa-user"></i>
            <i v-else class="fas fa-robot"></i>
            {{ message.text }}
          </span>
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
    apiEndpoint: String
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
        const response = await fetch('http://127.0.0.1:5000' + this.apiEndpoint, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ prompt: userMessage.text })
        });

        if (!response.ok) {
          throw new Error('Network response was not ok');
        }

        const data = await response.json();
        const botMessage = {
          text: data.response || data.answer,
          isUser: false
        };
        this.messages.push(botMessage);
      } catch (error) {
        const errorMessage = {
          text: 'Error: ' + error.message,
          isUser: false
        };
        this.messages.push(errorMessage);
      }
    }
  }
}
</script>

<style scoped>
/* Add any additional styling here if needed */
</style>
