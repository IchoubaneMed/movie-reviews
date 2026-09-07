import { beforeEach, describe, expect, it, vi } from "vitest"
import { mount } from "@vue/test-utils"

import { updateActor } from "@/api/actors"
import ActorEditDialog from "../ActorEditDialog.vue"

vi.mock("@/api/actors", () => ({
  updateActor: vi.fn(),
}))

describe("ActorEditDialog", () => {
  beforeEach(() => {
    vi.clearAllMocks()
  })

  it("updates an actor and emits updated", async () => {
    updateActor.mockResolvedValue({
      data: {
        id: 1,
        first_name: "Leo",
        last_name: "DiCaprio",
      },
    })

    const actor = {
      id: 1,
      first_name: "Leonardo",
      last_name: "DiCaprio",
    }

    const wrapper = mount(ActorEditDialog, {
      props: {
        actor,
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
          VTextField: {
            props: ["modelValue", "label"],
            emits: ["update:modelValue"],
            template: `
              <input
                :data-test="label"
                :value="modelValue"
                @input="$emit('update:modelValue', $event.target.value)"
              />
            `,
          },
        },
      },
    })

    await wrapper.findAll("button")[0].trigger("click")

    await wrapper
      .find("[data-test='First name']")
      .setValue("Leo")

    const saveButton = wrapper
      .findAll("button")
      .find((button) => button.text() === "Save")

    await saveButton.trigger("click")

    expect(updateActor).toHaveBeenCalledWith(1, {
      first_name: "Leo",
      last_name: "DiCaprio",
    })

    expect(wrapper.emitted("updated")).toHaveLength(1)
  })
})