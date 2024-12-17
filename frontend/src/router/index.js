import { createRouter, createWebHistory } from 'vue-router'
import GenerateIdeas from '../views/GenerateIdeas.vue'
import SearchKnowledge from '../views/SearchKnowledge.vue'

const routes = [
  {
    path: '/',
    name: 'SearchKnowledge',
    component: SearchKnowledge
  },
  {
    path: '/generate-ideas',
    name: 'GenerateIdeas',
    component: GenerateIdeas
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
