from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import ProblemSerializer
from .models import Problems
from django.shortcuts import get_object_or_404
import django_filters
from .filters import ProblemFilter


# Create your views here


class ProblemViewSet(viewsets.ModelViewSet):
    """
    Standar view for Problems


    Return all problem without the field 'categories'
    """
    model = Problems
    queryset = model.objects.all()
    serializer_class = ProblemSerializer
    filterset_class = ProblemFilter
    ordering_fields = ['accepteds', 'percentage_users_completed', 'id_problem']
    ordering = ['id_problem']
    http_method_names = ['get']
