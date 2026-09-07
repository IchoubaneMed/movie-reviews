<script setup>
import { ref } from "vue"

import { updateActor } from "@/api/actors"

const props = defineProps({
  actor: {
    type: Object,
    required: true,
  },
})

const emit = defineEmits(["updated"])

const dialog = ref(false)
const firstName = ref("")
const lastName = ref("")
const saving = ref(false)
const error = ref(null)

function openDialog() {
  firstName.value = props.actor.first_name
  lastName.value = props.actor.last_name
  error.value = null
  dialog.value = true
}

function closeDialog() {
  dialog.value = false
}

async function saveActor() {
  saving.value = true
  error.value = null

  try {
    await updateActor(props.actor.id, {
      first_name: firstName.value,
      last_name: lastName.value,
    })

    dialog.value = false
    emit("updated")
  } catch (err) {
    console.error(err)
    error.value = "Unable to update actor."
  } finally {
    saving.value = false
  }
}
</script>

<template>
  <v-btn
    size="small"
    variant="text"
    @click="openDialog"
  >
    Edit
  </v-btn>

  <v-dialog
    v-model="dialog"
    max-width="500"
  >
    <v-card>
      <v-card-title>
        Edit actor
      </v-card-title>

      <v-card-text>
        <v-alert
          v-if="error"
          type="error"
          class="mb-4"
        >
          {{ error }}
        </v-alert>

        <v-text-field
          v-model="firstName"
          label="First name"
        />

        <v-text-field
          v-model="lastName"
          label="Last name"
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
          @click="saveActor"
        >
          Save
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>