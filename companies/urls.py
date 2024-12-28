from django.urls import path, include
from rest_framework import routers

from companies import views

routes = routers.DefaultRouter()

routes.register('companies', views.CompaniesListView, basename='companies')

urlpatterns = [
    path("api/v1/", include(routes.urls)),
]
