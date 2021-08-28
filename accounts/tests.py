from django.test import TestCase
from django.test import Client
import pytest
from django.urls import reverse

# Create your tests here.

@pytest.mark.django_db
def test_client():
    Client()


@pytest.mark.django_db
def test_signup_view():
    c = Client()
    url = reverse('signup')
    response = c.get(url)
    assert response.status_code == 200
    assert len(response.context['form'].fields) == 3