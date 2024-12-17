import { createRouter, createWebHistory } from 'vue-router'
import GenerateIdeas from '../views/GenerateIdeas.vue'
import SearchKnowledge from '../views/SearchKnowledge.vue'
import SystemPrompt from '../views/SystemPrompt.vue'
import KnowledgeBase from '../views/KnowledgeBase.vue'

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
  },
  {
    path: '/knowledge-base',
    name: 'KnowledgeBase',
    component: KnowledgeBase
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
