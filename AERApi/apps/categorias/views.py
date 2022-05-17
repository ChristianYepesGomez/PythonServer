from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets
from .serializers import CategorySerializer
from .models import Categories
from .filters import CategoriesFilter


# Create your views here


class CategoriesViewSet(viewsets.ModelViewSet):
    """
    Standar view for Problems


    Return all problem without the field 'categories'
    """
    model = Categories
    queryset = model.objects.all()
    serializer_class = CategorySerializer
    filterset_class = CategoriesFilter
    ordering_fields = ['id_category', 'name']
    ordering = ['id_category']
    http_method_names = ['get']
