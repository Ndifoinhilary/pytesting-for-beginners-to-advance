# in companies/urls.py
from django.urls import path, include
from rest_framework import routers
from companies import views

router = routers.DefaultRouter()
router.register('companies', views.CompaniesListView, basename='companies')  # Correct basename

urlpatterns = [
    path('', include(router.urls)),  # Include the router's URLs
]
