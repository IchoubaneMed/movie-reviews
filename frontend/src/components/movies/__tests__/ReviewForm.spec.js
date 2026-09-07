import { beforeEach, describe, expect, it, vi } from "vitest"
import { mount } from "@vue/test-utils"

import { createReview } from "@/api/movies"
import ReviewForm from "../ReviewForm.vue"

vi.mock("@/api/movies", () => ({
  createReview: vi.fn(),
}))

function mountReviewForm() {
  return mount(ReviewForm, {
    props: {
      movieId: 1,
    },
    global: {
      stubs: {
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
        VAlert: {
          template: "<div><slot /></div>",
        },
        VRating: {
          props: ["modelValue"],
          emits: ["update:modelValue"],
          template: `
            <input
              data-test="rating"
              type="number"
              :value="modelValue"
              @input="$emit(
                'update:modelValue',
                Number($event.target.value)
              )"
            />
          `,
        },
        VBtn: {
          template:
            "<button @click=\"$emit('click')\"><slot /></button>",
        },
      },
    },
  })
}

describe("ReviewForm", () => {
  beforeEach(() => {
    vi.clearAllMocks()
  })

  it("creates a review and emits created", async () => {
    createReview.mockResolvedValue({
      data: {
        id: 100,
        grade: 5,
      },
    })

    const wrapper = mountReviewForm()

    await wrapper
      .find("[data-test='rating']")
      .setValue(5)

    const submitButton = wrapper
      .findAll("button")
      .find((button) => button.text() === "Submit review")

    await submitButton.trigger("click")

    expect(createReview).toHaveBeenCalledWith(1, {
      grade: 5,
    })

    expect(wrapper.emitted("created")).toHaveLength(1)
  })

  it("does not submit an invalid rating", async () => {
    const wrapper = mountReviewForm()

    await wrapper
      .find("[data-test='rating']")
      .setValue(6)

    const submitButton = wrapper
      .findAll("button")
      .find((button) => button.text() === "Submit review")

    await submitButton.trigger("click")

    expect(createReview).not.toHaveBeenCalled()

    expect(wrapper.text()).toContain(
      "Please select a rating between 1 and 5.",
    )
  })

  it("shows an error when review creation fails", async () => {
    createReview.mockRejectedValue(
      new Error("Server error"),
    )

    const wrapper = mountReviewForm()

    await wrapper
      .find("[data-test='rating']")
      .setValue(4)

    const submitButton = wrapper
      .findAll("button")
      .find((button) => button.text() === "Submit review")

    await submitButton.trigger("click")

    expect(wrapper.text()).toContain(
      "Unable to add review.",
    )

    expect(wrapper.emitted("created")).toBeUndefined()
  })
})