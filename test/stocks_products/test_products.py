import pytest


from rest_framework.test import APIClient

@pytest.mark.django_db
def test_api():
    client = APIClient()
    response = client.get('/api/v1/products/')
    assert response.status_code == 200
