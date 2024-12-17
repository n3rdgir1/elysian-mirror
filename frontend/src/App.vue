<template>
  <div class="min-h-screen flex flex-col">
    <header class="bg-gray-800 text-white p-4">
      <h1 class="text-2xl text-left">Elysian Mirror</h1>
    </header>
    <main class="flex flex-1">
      <ChatWindow title="Generate Ideas" api-endpoint="/generate" />
      <ChatWindow title="Search Knowledgebase" api-endpoint="/rag" />
    </main>
  </div>
</template>

<script>
import ChatWindow from './components/ChatWindow.vue'

export default {
  name: 'App',
  components: {
    ChatWindow
  }
}
</script>

<style>
@import './assets/tailwind.css';

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
