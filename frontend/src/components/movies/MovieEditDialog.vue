<script setup>
import { ref } from "vue"

import { updateMovie } from "@/api/movies"

const props = defineProps({
  movie: {
    type: Object,
    required: true,
  },
})

const emit = defineEmits(["updated"])

const dialog = ref(false)
const description = ref("")
const saving = ref(false)
const error = ref(null)

function openDialog() {
  description.value = props.movie.description
  error.value = null
  dialog.value = true
}

function closeDialog() {
  dialog.value = false
}

async function saveMovie() {
  saving.value = true
  error.value = null

  try {
    await updateMovie(props.movie.id, {
      description: description.value,
    })

    dialog.value = false
    emit("updated")
  } catch (err) {
    console.error(err)
    error.value = "Unable to update movie."
  } finally {
    saving.value = false
  }
}
</script>

<template>
  <v-btn
    color="primary"
    @click="openDialog"
  >
    Edit movie
  </v-btn>

  <v-dialog
    v-model="dialog"
    max-width="700"
  >
    <v-card>
      <v-card-title>
        Edit {{ movie.title }}
      </v-card-title>

      <v-card-text>
        <v-alert
          v-if="error"
          type="error"
          class="mb-4"
        >
          {{ error }}
        </v-alert>

        <v-textarea
          v-model="description"
          label="Description"
          rows="5"
          auto-grow
        />
      </v-card-text>

      <v-card-actions>
        <v-spacer />

        <v-btn
          :disabled="saving"
          @click="closeDialog"
        >
          Cancel
        </v-btn>

        <v-btn
          color="primary"
          :loading="saving"
          @click="saveMovie"
        >
          Save
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>