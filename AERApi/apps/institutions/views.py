from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import InstitutionsSerializer
from .models import Institutions


# Create your views here.


class InstitutionViewSet(viewsets.ModelViewSet):
    """
    Standar view for Institutions
    """
    model = Institutions
    queryset = model.objects.all()
    serializer_class = InstitutionsSerializer

    http_method_names = ['get']
