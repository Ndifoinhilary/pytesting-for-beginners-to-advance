import pytest
from django.urls import reverse

from companies.models import Company

companies_url = reverse("companies-list")


@pytest.mark.django_db
def test_zero_company_should_return_empty_list(client):
    response = client.get(companies_url)
    assert response.status_code == 200
    assert response.json() == []


@pytest.mark.django_db
def test_company_should_return_company_list(client):
    company = Company.objects.create(name="test")
    response = client.get(companies_url)
    response_content = response.json()
    assert response.status_code == 200
    assert response.json() != []
    assert len(response_content) == 1
    assert response_content[0]["name"] == company.name