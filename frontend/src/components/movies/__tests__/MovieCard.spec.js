import { describe, expect, it } from "vitest"
import { mount } from "@vue/test-utils"

import MovieCard from "../MovieCard.vue"

describe("MovieCard", () => {
  it("renders movie information", () => {
    const movie = {
      id: 1,
      title: "Inception",
      description: "A thief enters people's dreams.",
      average_grade: 4.5,
    }

    const wrapper = mount(MovieCard, {
      props: {
        movie,
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
          VRating: {
            template: "<div data-test='rating' />",
          },
          VBtn: {
            template: "<button><slot /></button>",
          },
        },
      },
    })

    expect(wrapper.text()).toContain("Inception")
    expect(wrapper.text()).toContain("A thief enters people's dreams.")
    expect(wrapper.find("[data-test='rating']").exists()).toBe(true)
    expect(wrapper.text()).toContain("View details")
  })

  it("shows a message when the movie has no reviews", () => {
    const movie = {
      id: 12,
      title: "Mad Max: Fury Road",
      description: "A post-apocalyptic action movie.",
      average_grade: null,
    }

    const wrapper = mount(MovieCard, {
      props: {
        movie,
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
          VRating: {
            template: "<div data-test='rating' />",
          },
          VBtn: {
            template: "<button><slot /></button>",
          },
        },
      },
    })

    expect(wrapper.text()).toContain("No reviews yet")
    expect(wrapper.find("[data-test='rating']").exists()).toBe(false)
  })
})