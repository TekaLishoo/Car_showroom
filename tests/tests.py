import pytest
from django.urls import reverse


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()


@pytest.mark.django_db
def test_unauthorized_request(api_client):
    """
    Check unauthorized API request
    """
    url = reverse('carshowroom-list')
    response = api_client.get(url)
    assert response.status_code == 401




