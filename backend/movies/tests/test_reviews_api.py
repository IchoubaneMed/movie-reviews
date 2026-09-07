import pytest
from rest_framework import status

from movies.models import Movie, Review


@pytest.mark.django_db
def test_review_can_be_created_for_movie(api_client):
    movie = Movie.objects.create(
        title="Inception",
        description="Description",
    )

    response = api_client.post(
        f"/api/movies/{movie.id}/reviews/",
        {
            "grade": 5,
        },
        format="json",
    )

    assert response.status_code == status.HTTP_201_CREATED

    assert Review.objects.count() == 1

    review = Review.objects.first()

    assert review.movie == movie
    assert review.grade == 5

@pytest.mark.django_db
def test_review_grade_above_five_is_rejected(api_client):
    movie = Movie.objects.create(
        title="Inception",
        description="Description",
    )

    response = api_client.post(
        f"/api/movies/{movie.id}/reviews/",
        {
            "grade": 6,
        },
        format="json",
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert Review.objects.count() == 0

@pytest.mark.django_db
def test_review_grade_below_one_is_rejected(api_client):
    movie = Movie.objects.create(
        title="Inception",
        description="Description",
    )

    response = api_client.post(
        f"/api/movies/{movie.id}/reviews/",
        {
            "grade": 0,
        },
        format="json",
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert Review.objects.count() == 0

@pytest.mark.django_db
def test_movie_detail_returns_404_when_movie_does_not_exist(
    api_client,
):
    response = api_client.get(
        "/api/movies/99999/"
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND

@pytest.mark.django_db
def test_review_cannot_be_created_for_nonexistent_movie(
    api_client,
):
    response = api_client.post(
        "/api/movies/99999/reviews/",
        {
            "grade": 5,
        },
        format="json",
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert Review.objects.count() == 0