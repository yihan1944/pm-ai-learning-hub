import { ref, watch } from 'vue'

const STORAGE_KEY = 'learning-progress'

const completedItems = ref<Set<string>>(new Set())

// Load from localStorage
try {
  const saved = localStorage.getItem(STORAGE_KEY)
  if (saved) {
    const arr = JSON.parse(saved) as string[]
    completedItems.value = new Set(arr)
  }
} catch {}

// Save on change
watch(completedItems, (val) => {
  localStorage.setItem(STORAGE_KEY, JSON.stringify([...val]))
}, { deep: true })

export function useProgress() {
  function toggle(itemId: string) {
    const next = new Set(completedItems.value)
    if (next.has(itemId)) {
      next.delete(itemId)
    } else {
      next.add(itemId)
    }
    completedItems.value = next
  }

  function isCompleted(itemId: string) {
    return completedItems.value.has(itemId)
  }

  return { completedItems, toggle, isCompleted }
}
