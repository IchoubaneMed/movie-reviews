import pytest

from movies.models import Actor, Movie, Review

@pytest.mark.django_db
def test_movie_can_have_actors():
    actor = Actor.objects.create(
        first_name="Leonardo",
        last_name="DiCaprio",
    )

    movie = Movie.objects.create(
        title="Inception",
        description="A science fiction movie.",
    )

    movie.actors.add(actor)

    assert movie.actors.count() == 1
    assert movie.actors.first() == actor

@pytest.mark.django_db
def test_movie_can_have_reviews():
    movie = Movie.objects.create(
        title="Inception",
        description="A science fiction movie.",
    )

    review = Review.objects.create(
        movie=movie,
        grade=5,
    )

    assert movie.reviews.count() == 1
    assert movie.reviews.first() == review