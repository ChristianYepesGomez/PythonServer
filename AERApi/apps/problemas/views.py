from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets
from .serializers import ProblemSerializer
from .models import Problems


# Create your views here


class ProblemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Problems.objects.all().order_by('id_problem')
    serializer_class = ProblemSerializer
