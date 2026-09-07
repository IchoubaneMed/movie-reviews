import { ref } from "vue"
import { defineStore } from "pinia"

import { getMovies } from "@/api/movies"

export const useMoviesStore = defineStore("movies", () => {
  const movies = ref([])
  const total = ref(0)
  const currentPage = ref(1)
  const loading = ref(false)
  const error = ref(null)

  async function fetchMovies(page = 1) {
    loading.value = true
    error.value = null

    try {
      const response = await getMovies(page)

      movies.value = response.data.results
      total.value = response.data.count
      currentPage.value = page
    } catch (err) {
      error.value = "Unable to load movies."
    } finally {
      loading.value = false
    }
  }

  return {
    movies,
    total,
    currentPage,
    loading,
    error,
    fetchMovies,
  }
})