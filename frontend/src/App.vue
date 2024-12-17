<template>
  <div class="min-h-screen flex">
    <aside :class="['bg-gray-800 text-white p-4 fixed h-full', { 'w-16': isCollapsed, 'w-45': !isCollapsed }]">
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
            <router-link to="/generate-ideas" class="flex flex-col items-center">
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
        </ul>
      </nav>
    </aside>
    <main class="flex-1 ml-16">
      <router-view />
    </main>
  </div>
</template>

<script>
import { ref } from 'vue'

export default {
  name: 'App',
  setup() {
    const isCollapsed = ref(true) // Set to true to collapse by default

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

aside.fixed {
  top: 0;
  left: 0;
}

main {
  margin-left: 16rem; /* Adjust based on the width of the sidebar */
}
</style>
