from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets
from .serializers import UserSerializer, UserSerializerWithoutProblems
from .models import Users
from django.http import HttpResponse
from .filters import UsersFilter


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all().order_by('id_user')
    serializer_class = UserSerializer
    filterset_fields = ['country', 'institution', 'name', 'nick']

    model = Users
    queryset = model.objects.all()
    serializer_class = UserSerializer
    filterset_class = UsersFilter
    ordering_fields = ['accepteds', 'intents', ]
    ordering = ['id_user']
    http_method_names = ['get']


class UserViewSetWithoutProblems(viewsets.ModelViewSet):
    queryset = Users.objects.all().order_by('id_user')
    serializer_class = UserSerializerWithoutProblems
    filterset_fields = ['country', 'institution', 'name', 'nick']

    model = Users
    queryset = model.objects.all()
    serializer_class = UserSerializerWithoutProblems
    filterset_class = UsersFilter
    ordering_fields = ['accepteds', 'intents', ]
    ordering = ['id_user']
    http_method_names = ['get']
