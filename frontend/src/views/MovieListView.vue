<script setup>
import { computed, onMounted } from "vue"
import { storeToRefs } from "pinia"

import MovieCard from "@/components/movies/MovieCard.vue"
import { useMoviesStore } from "@/stores/movies"

const store = useMoviesStore()

const {
  movies,
  total,
  currentPage,
  loading,
  error,
} = storeToRefs(store)

const pageCount = computed(() =>
  Math.ceil(total.value / 5),
)

const changePage = (page) => {
  store.fetchMovies(page)
}

onMounted(() => {
  store.fetchMovies()
})
</script>

<template>
  <v-container>
    <h1 class="mb-6">Movies</h1>

    <v-progress-circular
      v-if="loading"
      indeterminate
    />

    <v-alert
      v-else-if="error"
      type="error"
    >
      {{ error }}
    </v-alert>

    <template v-else>
      <v-row>
        <v-col
          v-for="movie in movies"
          :key="movie.id"
          cols="12"
        >
          <MovieCard :movie="movie" />
        </v-col>
      </v-row>

      <v-pagination
        v-if="pageCount > 1"
        :model-value="currentPage"
        :length="pageCount"
        class="mt-6"
        @update:model-value="changePage"
      />
    </template>
  </v-container>
</template>