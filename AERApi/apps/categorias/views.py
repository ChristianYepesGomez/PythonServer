from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets
from .serializers import CategorySerializer
from .models import Categories


# Create your views here


class CategoriesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Categories.objects.all().order_by('id_category')
    serializer_class = CategorySerializer
