from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets
from ...api.serializers import UserSerializer
from .models import Users


# Create your views here


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Users.objects.all().order_by('id_user')
    serializer_class = UserSerializer
