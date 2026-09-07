from rest_framework.routers import DefaultRouter

from .views import ActorViewSet, MovieViewSet

router = DefaultRouter()

router.register(
    "movies",
    MovieViewSet,
    basename="movie",
)

router.register(
    "actors",
    ActorViewSet,
    basename="actor",
)

urlpatterns = router.urls