import { createRouter, createWebHistory } from 'vue-router'
import GenerateIdeas from '../views/GenerateIdeas.vue'
import SearchKnowledge from '../views/SearchKnowledge.vue'
import SystemPrompt from '../views/SystemPrompt.vue'

const routes = [
  {
    path: '/',
    redirect: '/system-prompt'
  },
  {
    path: '/generate-ideas',
    name: 'GenerateIdeas',
    component: GenerateIdeas
  },
  {
    path: '/search-knowledge',
    name: 'SearchKnowledge',
    component: SearchKnowledge
  },
  {
    path: '/system-prompt',
    name: 'SystemPrompt',
    component: SystemPrompt
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
