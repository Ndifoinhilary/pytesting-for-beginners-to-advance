from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from companies.models import Company
from companies.serializers import CompanySerializer


# Create your views here.



class CompaniesListView(ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all().order_by('last_update')