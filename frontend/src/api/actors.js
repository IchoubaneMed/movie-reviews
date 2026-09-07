import { apiClient } from "./client"

export const updateActor = (id, data) => {
  return apiClient.patch(`/actors/${id}/`, data)
}