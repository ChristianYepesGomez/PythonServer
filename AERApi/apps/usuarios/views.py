from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import Users

from django.http import HttpResponse


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all().order_by('id_user')
    serializer_class = UserSerializer
    filterset_fields = ['country', 'institution', 'name', 'nick']


class UserViewSetByAccepteds(viewsets.ModelViewSet):
    queryset = Users.objects.all().order_by('accepteds')
    serializer_class = UserSerializer
    filterset_fields = ['country', 'institution', 'name', 'nick']
