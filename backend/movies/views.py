from django.db.models import Avg
from rest_framework import viewsets
from .pagination import MoviePagination

# Create your views here.

from .models import Movie
from .serializers import (
    MovieDetailSerializer,
    MovieListSerializer,
)

class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = (
        Movie.objects
        .prefetch_related("actors", "reviews")
        .annotate(average_grade=Avg("reviews__grade"))
    )

    pagination_class = MoviePagination

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        return MovieDetailSerializer