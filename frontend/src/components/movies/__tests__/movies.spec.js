import { beforeEach, describe, expect, it, vi } from "vitest"
import { createPinia, setActivePinia } from "pinia"

import { getMovies } from "@/api/movies"
import { useMoviesStore } from "../movies"

vi.mock("@/api/movies", () => ({
  getMovies: vi.fn(),
}))

describe("movies store", () => {
  beforeEach(() => {
    setActivePinia(createPinia())
    vi.clearAllMocks()
  })

  it("loads movies and pagination information", async () => {
    getMovies.mockResolvedValue({
      data: {
        count: 12,
        next: "http://localhost:8000/api/movies/?page=2",
        previous: null,
        results: [
          {
            id: 1,
            title: "Inception",
            description: "Description",
            average_grade: 4.5,
          },
        ],
      },
    })

    const store = useMoviesStore()

    await store.fetchMovies(1)

    expect(getMovies).toHaveBeenCalledWith(1)

    expect(store.movies).toHaveLength(1)
    expect(store.movies[0].title).toBe("Inception")

    expect(store.total).toBe(12)
    expect(store.currentPage).toBe(1)
    expect(store.loading).toBe(false)
    expect(store.error).toBeNull()
  })

  it("loads the requested page", async () => {
    getMovies.mockResolvedValue({
      data: {
        count: 12,
        results: [],
      },
    })

    const store = useMoviesStore()

    await store.fetchMovies(2)

    expect(getMovies).toHaveBeenCalledWith(2)
    expect(store.currentPage).toBe(2)
  })

  it("sets an error when movies cannot be loaded", async () => {
    getMovies.mockRejectedValue(new Error("Network error"))

    const store = useMoviesStore()

    await store.fetchMovies()

    expect(store.error).toBe("Unable to load movies.")
    expect(store.loading).toBe(false)
  })
})