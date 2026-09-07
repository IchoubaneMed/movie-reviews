import pytest
from rest_framework import status

from movies.models import Actor, Movie, Review

@pytest.mark.django_db
def test_movie_list_returns_movies(api_client):
    Movie.objects.create(
        title="Inception",
        description="Dreams within dreams.",
    )

    Movie.objects.create(
        title="Interstellar",
        description="Exploration through space.",
    )

    response = api_client.get("/api/movies/")

    assert response.status_code == status.HTTP_200_OK
    assert response.data["count"] == 2
    assert len(response.data["results"]) == 2

@pytest.mark.django_db
def test_movie_list_returns_five_movies_per_page(api_client, movies,):

    response = api_client.get("/api/movies/")

    assert response.status_code == status.HTTP_200_OK
    assert response.data["count"] == 12
    assert len(response.data["results"]) == 5

@pytest.mark.django_db
def test_movie_list_second_page_returns_five_movies(api_client, movies):

    response = api_client.get(
        "/api/movies/",
        {"page": 2},
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.data["count"] == 12
    assert len(response.data["results"]) == 5

@pytest.mark.django_db
def test_movie_list_last_page_returns_remaining_movies(api_client, movies):

    response = api_client.get(
        "/api/movies/",
        {"page": 3},
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.data["count"] == 12
    assert len(response.data["results"]) == 2

@pytest.mark.django_db
def test_movie_detail_contains_actors(api_client):
    actor = Actor.objects.create(
        first_name="Leonardo",
        last_name="DiCaprio",
    )

    movie = Movie.objects.create(
        title="Inception",
        description="Dreams within dreams.",
    )

    movie.actors.add(actor)

    response = api_client.get(
        f"/api/movies/{movie.id}/"
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.data["title"] == "Inception"

    assert len(response.data["actors"]) == 1

    assert (
        response.data["actors"][0]["first_name"]
        == "Leonardo"
    )

@pytest.mark.django_db
def test_movie_detail_returns_average_grade(api_client):
    movie = Movie.objects.create(
        title="Inception",
        description="Dreams within dreams.",
    )

    Review.objects.create(movie=movie, grade=5)
    Review.objects.create(movie=movie, grade=4)
    Review.objects.create(movie=movie, grade=3)

    response = api_client.get(
        f"/api/movies/{movie.id}/"
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.data["average_grade"] == 4.0
    
@pytest.mark.django_db
def test_movie_without_reviews_has_null_average_grade(
    api_client,
):
    movie = Movie.objects.create(
        title="Movie without reviews",
        description="No reviews yet.",
    )

    response = api_client.get(
        f"/api/movies/{movie.id}/"
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.data["average_grade"] is None

@pytest.mark.django_db
def test_movie_description_can_be_updated(api_client):
    movie = Movie.objects.create(
        title="Inception",
        description="Old description",
    )

    response = api_client.patch(
        f"/api/movies/{movie.id}/",
        {
            "description": "New description",
        },
        format="json",
    )

    assert response.status_code == status.HTTP_200_OK

    movie.refresh_from_db()

    assert movie.description == "New description"

@pytest.mark.django_db
def test_movie_actors_can_be_updated(api_client):
    actor_one = Actor.objects.create(
        first_name="Leonardo",
        last_name="DiCaprio",
    )

    actor_two = Actor.objects.create(
        first_name="Joseph",
        last_name="Gordon-Levitt",
    )

    movie = Movie.objects.create(
        title="Inception",
        description="Description",
    )

    response = api_client.patch(
        f"/api/movies/{movie.id}/",
        {
            "actors": [
                actor_one.id,
                actor_two.id,
            ]
        },
        format="json",
    )

    assert response.status_code == status.HTTP_200_OK

    assert movie.actors.count() == 2
    assert actor_one in movie.actors.all()
    assert actor_two in movie.actors.all()