# import json
# import os
# from unittest import TestCase
#
# import pytest
# from django.test import Client
# from django.urls import reverse
#
# from companies.models import Company
#
#
# @pytest.mark.django_db
# class BasicCompanyAPITestCase(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.companies_url = reverse("companies-list")
#
#
#     def tearDown(self):
#         pass
#
#
#
# class TestGetCompanies(BasicCompanyAPITestCase):
#
#
#     def test_zero_company_should_return_empty_list(self):
#         client = self.client
#         response = client.get(self.companies_url)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(json.loads(response.content), [])
#
#
#
#     def test_company_should_return_company_list(self):
#         client = self.client
#         company = Company.objects.create(
#             name="Test Company",
#         )
#         response = client.get(self.companies_url)
#         response_content = json.loads(response.content)[0]
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response_content["name"], company.name)
#         self.assertEqual(response_content["description"], "")
#
#
#
#
#
# class TestPostCompanies(BasicCompanyAPITestCase):
#     def test_create_company_without_argument(self):
#         response = self.client.post(path=self.companies_url)
#         self.assertEqual(response.status_code, 400)
#
#
#     def test_create_company_with_argument(self):
#         response = self.client.post(path=self.companies_url, data={"name": "Test Company"})
#         self.assertEqual(response.status_code, 201)
