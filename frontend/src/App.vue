<template>
  <div class="min-h-screen flex flex-col">
    <header class="bg-gray-800 text-white p-4 flex justify-between items-center fixed w-full z-20">
      <h1 class="text-2xl">Elysian Mirror</h1>
      <button @click="openAddKnowledgeModal" class="bg-blue-500 text-white p-2 rounded flex items-center">
        <i class="fas fa-plus"></i>
        <span class="ml-2">Knowledge</span>
      </button>
    </header>
    <div class="flex flex-1">
      <aside :class="['bg-gray-800 text-white p-4 fixed mt-16', { 'w-16': isCollapsed, 'w-45': !isCollapsed }]">
        <button @click="toggleMenu" class="mb-4">
          <span v-if="isCollapsed">☰</span>
          <span v-else>✖</span>
        </button>
        <nav>
          <ul>
            <li class="mb-4">
              <router-link to="/search-knowledge" class="flex flex-col items-center">
                <i :class="['fas fa-search', { 'text-2xl': isCollapsed, 'text-4xl': !isCollapsed }]"></i>
                <span v-if="!isCollapsed" class="mt-2 text-center">Search<br>Knowledge</span>
              </router-link>
            </li>
            <li class="mb-4">
              <router-link to="/generate-ideas" @click="handleServerMessage" class="flex flex-col items-center">
                <i :class="['fas fa-lightbulb', { 'text-2xl': isCollapsed, 'text-4xl': !isCollapsed }]"></i>
                <span v-if="!isCollapsed" class="mt-2 text-center">Generate<br>Ideas</span>
              </router-link>
            </li>
            <li class="mb-4">
              <router-link to="/system-prompt" class="flex flex-col items-center">
                <i :class="['fas fa-terminal', { 'text-2xl': isCollapsed, 'text-4xl': !isCollapsed }]"></i>
                <span v-if="!isCollapsed" class="mt-2 text-center">System<br>Prompt</span>
              </router-link>
            </li>
            <li class="mb-4">
              <router-link to="/knowledge-base" class="flex flex-col items-center">
                <i :class="['fas fa-book', { 'text-2xl': isCollapsed, 'text-4xl': !isCollapsed }]"></i>
                <span v-if="!isCollapsed" class="mt-2 text-center">Knowledge<br>Base</span>
              </router-link>
            </li>
          </ul>
        </nav>
      </aside>
      <main class="flex-1 ml-16">
        <router-view @server-message="handleServerMessage" />
      </main>
    </div>
    <AddKnowledgeModal v-if="isAddKnowledgeModalOpen" @close="closeAddKnowledgeModal" @server-message="handleServerMessage" />
    <div class="fixed top-0 right-0 m-4 z-20">
      <AppNotification
        v-for="notification in notifications"
        :key="notification.id"
        :message="notification.message"
        :type="notification.type"
        :id="notification.id"
        @close="removeNotification"
      />
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'
import AddKnowledgeModal from './components/AddKnowledgeModal.vue'
import AppNotification from './components/Notification.vue' // Updated import

export default {
  name: 'App',
  components: {
    AddKnowledgeModal,
    AppNotification // Updated component name
  },
  setup() {
    const isCollapsed = ref(true) // Set to true to collapse by default
    const isAddKnowledgeModalOpen = ref(false)
    const notifications = ref([])

    function toggleMenu() {
      isCollapsed.value = !isCollapsed.value
    }

    function openAddKnowledgeModal() {
      isAddKnowledgeModalOpen.value = true
    }

    function closeAddKnowledgeModal() {
      isAddKnowledgeModalOpen.value = false
    }

    function addNotification(message, type) {
      const id = Date.now()
      notifications.value.push({ id, message, type })
    }

    function removeNotification(id) {
      notifications.value = notifications.value.filter(notification => notification.id !== id)
    }

    function handleServerMessage({ message, type }) {
      addNotification(message, type)
    }

    return {
      isCollapsed,
      toggleMenu,
      isAddKnowledgeModalOpen,
      openAddKnowledgeModal,
      closeAddKnowledgeModal,
      notifications,
      addNotification,
      removeNotification,
      handleServerMessage
    }
  }
}
</script>

<style>
@import './assets/tailwind.css';
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css');

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

aside.fixed {
  top: 0;
  left: 0;
  margin-top: 4rem; /* Adjust the top margin to start lower down */
  height: calc(100vh - 4rem); /* Adjust the height to make the menu shorter */
  z-index: 10; /* Ensure the sidebar displays above other elements */
}

main {
  margin-left: 16rem; /* Adjust based on the width of the sidebar */
  margin-top: 4rem; /* Adjust to account for the fixed header */
}
</style>
