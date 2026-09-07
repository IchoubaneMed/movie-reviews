import { beforeEach, describe, expect, it, vi } from "vitest"
import { mount } from "@vue/test-utils"

import { updateMovie } from "@/api/movies"
import MovieEditDialog from "../MovieEditDialog.vue"

vi.mock("@/api/movies", () => ({
  updateMovie: vi.fn(),
}))

describe("MovieEditDialog", () => {
  beforeEach(() => {
    vi.clearAllMocks()
  })

  it("updates the movie and emits updated", async () => {
    updateMovie.mockResolvedValue({
      data: {
        description: "Updated description",
      },
    })

    const movie = {
      id: 1,
      title: "Inception",
      description: "Original description",
      actors: [],
    }

    const wrapper = mount(MovieEditDialog, {
      props: {
        movie,
      },
      global: {
        stubs: {
          VBtn: {
            template:
              "<button @click=\"$emit('click')\"><slot /></button>",
          },
          VDialog: {
            template: "<div><slot /></div>",
          },
          VCard: {
            template: "<div><slot /></div>",
          },
          VCardTitle: {
            template: "<div><slot /></div>",
          },
          VCardText: {
            template: "<div><slot /></div>",
          },
          VCardActions: {
            template: "<div><slot /></div>",
          },
          VSpacer: {
            template: "<div />",
          },
          VAlert: {
            template: "<div><slot /></div>",
          },
          VTextarea: {
            props: ["modelValue"],
            emits: ["update:modelValue"],
            template: `
              <textarea
                data-test="description"
                :value="modelValue"
                @input="$emit('update:modelValue', $event.target.value)"
              />
            `,
          },
        },
      },
    })

    const buttons = wrapper.findAll("button")

    await buttons[0].trigger("click")

    const textarea = wrapper.find("[data-test='description']")

    await textarea.setValue("Updated description")

    const saveButton = wrapper
      .findAll("button")
      .find((button) => button.text() === "Save")

    await saveButton.trigger("click")

    expect(updateMovie).toHaveBeenCalledWith(1, {
      description: "Updated description",
    })

    expect(wrapper.emitted("updated")).toHaveLength(1)
  })
})