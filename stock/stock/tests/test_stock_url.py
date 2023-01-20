import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_admin_url(client):
    url = reverse('admin:index')
    response = client.get(url)
    assert response.status_code == 302
