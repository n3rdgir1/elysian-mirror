import { createRouter, createWebHistory } from 'vue-router'
import GenerateIdeas from '../views/GenerateIdeas.vue'
import SearchKnowledge from '../views/SearchKnowledge.vue'

const routes = [
  {
    path: '/',
    redirect: '/search-knowledge'
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
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
