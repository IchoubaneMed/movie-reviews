from django.db.models import Avg
from rest_framework import mixins, viewsets
from .pagination import MoviePagination

# Create your views here.

from .models import Actor, Movie
from .serializers import (
    ActorSerializer,
    MovieDetailSerializer,
    MovieListSerializer,
    MovieUpdateSerializer,
)

class MovieViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = (
        Movie.objects
        .prefetch_related("actors", "reviews")
        .annotate(average_grade=Avg("reviews__grade"))
    )

    pagination_class = MoviePagination

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        if self.action in ("update", "partial_update"):
            return MovieUpdateSerializer
        return MovieDetailSerializer
    


class ActorViewSet(
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer