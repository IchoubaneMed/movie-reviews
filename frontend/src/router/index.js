import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "movies",
      component: () =>
        import("../views/MovieListView.vue"),
    },
    {
      path: "/movies/:id",
      name: "movie-detail",
      component: () =>
        import("../views/MovieDetailView.vue"),
      props: true,
    },
  ],
})

export default router
