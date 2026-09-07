<script setup>
import { ref } from "vue"

import { createReview } from "@/api/movies"

const props = defineProps({
  movieId: {
    type: Number,
    required: true,
  },
})

const emit = defineEmits(["created"])

const grade = ref(0)
const submitting = ref(false)
const error = ref(null)

async function submitReview() {
  if (grade.value < 1 || grade.value > 5) {
    error.value = "Please select a rating between 1 and 5."
    return
  }

  submitting.value = true
  error.value = null

  try {
    await createReview(props.movieId, {
      grade: grade.value,
    })

    grade.value = 0
    emit("created")
  } catch (err) {
    console.error(err)
    error.value = "Unable to add review."
  } finally {
    submitting.value = false
  }
}
</script>

<template>
  <v-card
    variant="outlined"
    class="mt-8"
  >
    <v-card-title>
      Add a review
    </v-card-title>

    <v-card-text>
      <v-alert
        v-if="error"
        type="error"
        class="mb-4"
      >
        {{ error }}
      </v-alert>

      <v-rating
        v-model="grade"
        :length="5"
        hover
      />
    </v-card-text>

    <v-card-actions>
      <v-btn
        color="primary"
        :loading="submitting"
        :disabled="grade === 0"
        @click="submitReview"
      >
        Submit review
      </v-btn>
    </v-card-actions>
  </v-card>
</template>