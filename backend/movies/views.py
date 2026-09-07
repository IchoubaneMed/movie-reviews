from django.db.models import Avg
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .pagination import MoviePagination

# Create your views here.

from .models import Actor, Movie
from .serializers import (
    ActorSerializer,
    MovieDetailSerializer,
    MovieListSerializer,
    MovieUpdateSerializer,
    ReviewSerializer,
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
    
    @action(
        detail=True,
        methods=["post"],
        url_path="reviews",
    )
    def reviews(self, request, pk=None):
        movie = self.get_object()

        serializer = ReviewSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(movie=movie)

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )

class ActorViewSet(
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer