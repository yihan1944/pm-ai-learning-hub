import { ref } from 'vue'
import searchIndex from '../data/search-index.json'
import type { SearchItem } from '../types'

export function useSearch() {
  const results = ref<SearchItem[]>([])
  const loading = ref(false)

  function search(query: string) {
    const q = query.trim().toLowerCase()
    if (!q) {
      results.value = []
      return
    }

    loading.value = true
    results.value = searchIndex.filter(item =>
      item.title.toLowerCase().includes(q) ||
      item.text.toLowerCase().includes(q)
    ) as SearchItem[]
    loading.value = false
  }

  return { results, loading, search }
}
