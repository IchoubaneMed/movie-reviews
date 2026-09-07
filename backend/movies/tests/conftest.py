import pytest
from rest_framework.test import APIClient

from movies.models import Movie

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def movies():
    return [
        Movie.objects.create(
            title=f"Movie {index}",
            description=f"Description {index}",
        )
        for index in range(12)
    ]