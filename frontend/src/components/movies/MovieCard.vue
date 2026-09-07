<script setup>
defineProps({
  movie: {
    type: Object,
    required: true,
  },
})
</script>

<template>
  <v-card>
    <v-card-title>
      {{ movie.title }}
    </v-card-title>

    <v-card-text>
      <p>{{ movie.description }}</p>

      <div class="mt-4">
        <div
          v-if="movie.average_grade !== null"
          class="d-flex align-center ga-2 mt-4"
        >
          <v-rating
            :model-value="movie.average_grade"
            readonly
            half-increments
            density="compact"
          />

          <span>
            {{ Number(movie.average_grade).toFixed(1) }} / 5
          </span>
      </div>

        <span v-else>
          No reviews yet
        </span>
      </div>
    </v-card-text>

    <v-card-actions>
      <v-btn
        :to="{
          name: 'movie-detail',
          params: { id: movie.id },
        }"
      >
        View details
      </v-btn>
    </v-card-actions>
  </v-card>
</template>