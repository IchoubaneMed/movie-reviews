import { apiClient } from "./client"

export const getMovies = (page = 1) => {
  return apiClient.get("/movies/", {
    params: { page },
  })
}

export const getMovie = (id) => {
  return apiClient.get(`/movies/${id}/`)
}

export const updateMovie = (id, data) => {
  return apiClient.patch(`/movies/${id}/`, data)
}

export const createReview = (movieId, data) => {
  return apiClient.post(
    `/movies/${movieId}/reviews/`,
    data,
  )
}