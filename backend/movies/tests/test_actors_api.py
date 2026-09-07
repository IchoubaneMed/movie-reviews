import pytest
from rest_framework import status

from movies.models import Actor


@pytest.mark.django_db
def test_actor_can_be_updated(api_client):
    actor = Actor.objects.create(
        first_name="Leo",
        last_name="DiCaprio",
    )

    response = api_client.patch(
        f"/api/actors/{actor.id}/",
        {
            "first_name": "Leonardo",
        },
        format="json",
    )

    assert response.status_code == status.HTTP_200_OK

    actor.refresh_from_db()

    assert actor.first_name == "Leonardo"
    assert actor.last_name == "DiCaprio"