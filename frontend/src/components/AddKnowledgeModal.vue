<template>
  <BaseModal
    :confirm_text="isEditing ? 'Save' : 'Add'"
    cancel_text="Cancel"
    :content="modalContent"
    @close="$emit('close')"
    @confirm="handleSubmit"
  />
</template>

<script>
import { ref, watch, computed } from 'vue'
import BaseModal from './BaseModal.vue'

export default {
  name: 'AddKnowledgeModal',
  components: {
    BaseModal
  },
  props: {
    initialTitle: {
      type: String,
      default: ''
    },
    initialDescription: {
      type: String,
      default: ''
    },
    isEditing: {
      type: Boolean,
      default: false
    },
    knowledgeId: {
      type: String,
      default: null
    }
  },
  setup(props, { emit }) {
    const title = ref(props.initialTitle)
    const description = ref(props.initialDescription)
    const errors = ref({})
    const isLoading = ref(false)
    const apiResponse = ref(null)

    watch(() => props.initialTitle, (newTitle) => {
      title.value = newTitle
    })

    watch(() => props.initialDescription, (newDescription) => {
      description.value = newDescription
    })

    function validateForm() {
      errors.value = {}
      if (!title.value) {
        errors.value.title = 'Title is required'
      }
      if (!description.value) {
        errors.value.description = 'Description is required'
      }
      return Object.keys(errors.value).length === 0
    }

    async function handleSubmit() {
      if (!validateForm()) {
        return
      }

      isLoading.value = true
      try {
        const endpoint = props.isEditing ? 'http://127.0.0.1:5000/update_knowledge' : 'http://127.0.0.1:5000/embed'
        const payload = props.isEditing ? { id: props.knowledgeId, title: title.value, description: description.value } : { title: title.value, description: description.value }

        const response = await fetch(endpoint, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(payload)
        })

        if (!response.ok) {
          throw new Error('Network response was not ok')
        }

        const data = await response.json()
        apiResponse.value = data
        title.value = ''
        description.value = ''
        if (!props.isEditing) {
          emit('refresh')
        }
      } catch (error) {
        apiResponse.value = { message: 'Error: ' + error.message }
      } finally {
        isLoading.value = false
      }
    }

    const modalContent = computed(() => `
      <div>
        <h2 class="text-2xl mb-4">${props.isEditing ? 'Edit Knowledge' : 'Add Knowledge'}</h2>
        <form @submit.prevent="handleSubmit">
          <div class="mb-4">
            <label for="title" class="block text-gray-700">Title</label>
            <input v-model="title" id="title" type="text" class="mt-1 block w-full p-2 border rounded" />
            <span v-if="errors.title" class="text-red-500">{{ errors.title }}</span>
          </div>
          <div class="mb-4">
            <label for="description" class="block text-gray-700">Description</label>
            <textarea v-model="description" id="description" class="mt-1 block w-full p-2 border rounded" rows="5"></textarea>
            <span v-if="errors.description" class="text-red-500">{{ errors.description }}</span>
          </div>
        </form>
        <div v-if="apiResponse" class="mt-4">
          <p>{{ apiResponse.message }}</p>
        </div>
      </div>
    `)

    return {
      title,
      description,
      errors,
      isLoading,
      apiResponse,
      handleSubmit,
      modalContent
    }
  }
}
</script>

<style scoped>
/* Add any additional styling here if needed */
</style>
