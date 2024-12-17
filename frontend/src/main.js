import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './assets/tailwind.css'
import AddKnowledgeModal from './components/AddKnowledgeModal.vue'

createApp(App).use(router).component('AddKnowledgeModal', AddKnowledgeModal).mount('#app')
