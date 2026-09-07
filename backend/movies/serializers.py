from rest_framework import serializers

from .models import Actor, Movie, Review

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name")

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("id", "grade")
        read_only_fields = ("id",)

class MovieListSerializer(serializers.ModelSerializer):
    average_grade = serializers.FloatField(read_only=True)

    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "description",
            "average_grade",
        )

class MovieDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    average_grade = serializers.FloatField(read_only=True)

    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "description",
            "actors",
            "reviews",
            "average_grade",
        )

class MovieUpdateSerializer(serializers.ModelSerializer):
    actors = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Actor.objects.all(),
        required=False,
    )

    class Meta:
        model = Movie
        fields = (
            "description",
            "actors",
        )