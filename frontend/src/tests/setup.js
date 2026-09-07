import { config } from "@vue/test-utils"

config.global.stubs = {
  VBtn: {
    template: "<button><slot /></button>",
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
  VAlert: {
    template: "<div><slot /></div>",
  },
  VSpacer: {
    template: "<div />",
  },
  VDialog: {
    template: "<div><slot /></div>",
  },
}