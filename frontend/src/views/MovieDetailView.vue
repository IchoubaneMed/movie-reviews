<script setup>
import { onMounted, ref } from "vue"

import { getMovie } from "@/api/movies"
import MovieEditDialog from "@/components/movies/MovieEditDialog.vue"
const props = defineProps({
  id: {
    type: String,
    required: true,
  },
})


const movie = ref(null)
const loading = ref(false)
const error = ref(null)

async function fetchMovie() {
  loading.value = true
  error.value = null

  try {
    const response = await getMovie(props.id)
    movie.value = response.data
  } catch (error) {
    error.value = "Unable to load movie."
  } finally {
    loading.value = false
  }
}

onMounted(fetchMovie)
</script>

<template>
  <v-container>
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

    <template v-else-if="movie">
      <v-btn
        :to="{ name: 'movies' }"
        variant="text"
        class="mb-4"
      >
        Back to movies
      </v-btn>

      <div class="d-flex align-center justify-space-between mb-4">
        <h1>{{ movie.title }}</h1>

        <MovieEditDialog
          :movie="movie"
          @updated="fetchMovie"
        />
      </div>

      <p class="my-4">
        {{ movie.description }}
      </p>

      <h2>Rating</h2>

      <v-rating
        v-if="movie.average_grade !== null"
        :model-value="movie.average_grade"
        readonly
        half-increments
      />

      <p v-else>
        No reviews yet.
      </p>

      <h2 class="mt-6">Actors</h2>

      <v-list>
        <v-list-item
          v-for="actor in movie.actors"
          :key="actor.id"
        >
          {{ actor.first_name }}
          {{ actor.last_name }}
        </v-list-item>
      </v-list>

      <h2 class="mt-6">Reviews</h2>

      <v-list v-if="movie.reviews.length">
        <v-list-item
          v-for="review in movie.reviews"
          :key="review.id"
        >
          {{ review.grade }} / 5
        </v-list-item>
      </v-list>

      <p v-else>
        No reviews yet.
      </p>
    </template>
  </v-container>
</template>