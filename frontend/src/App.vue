<template>
  <div class="min-h-screen flex">
    <aside :class="['bg-gray-800 text-white p-4', { 'w-16': isCollapsed, 'w-45': !isCollapsed }]">
      <button @click="toggleMenu" class="mb-4">
        <span v-if="isCollapsed">☰</span>
        <span v-else>✖</span>
      </button>
      <nav>
        <ul>
          <li class="mb-4">
            <router-link to="/generate-ideas" class="flex flex-col items-center">
              <i :class="['fas fa-lightbulb', { 'text-2xl': isCollapsed, 'text-4xl': !isCollapsed }]"></i>
              <span v-if="!isCollapsed" class="mt-2 text-center">Generate<br>Ideas</span>
            </router-link>
          </li>
          <li class="mb-4">
            <router-link to="/search-knowledge" class="flex flex-col items-center">
              <i :class="['fas fa-search', { 'text-2xl': isCollapsed, 'text-4xl': !isCollapsed }]"></i>
              <span v-if="!isCollapsed" class="mt-2 text-center">Search<br>Knowledge</span>
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
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css');

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
