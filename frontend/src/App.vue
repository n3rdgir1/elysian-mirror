<template>
  <div class="min-h-screen flex">
    <aside :class="['bg-gray-800 text-white p-4', { 'w-16': isCollapsed, 'w-64': !isCollapsed }]">
      <button @click="toggleMenu" class="mb-4">
        <span v-if="isCollapsed">☰</span>
        <span v-else>✖</span>
      </button>
      <nav>
        <ul>
          <li>
            <router-link to="/generate-ideas" class="flex items-center">
              <span class="material-icons">lightbulb</span>
              <span v-if="!isCollapsed" class="ml-2">Generate Ideas</span>
            </router-link>
          </li>
          <li>
            <router-link to="/search-knowledge" class="flex items-center">
              <span class="material-icons">search</span>
              <span v-if="!isCollapsed" class="ml-2">Search Knowledge</span>
            </router-link>
          </li>
        </ul>
      </nav>
    </aside>
    <main class="flex-1">
      <router-view />
    </main>
  </div>
</template>

<script>
import { ref } from 'vue'

export default {
  name: 'App',
  setup() {
    const isCollapsed = ref(false)

    function toggleMenu() {
      isCollapsed.value = !isCollapsed.value
    }

    return {
      isCollapsed,
      toggleMenu
    }
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
