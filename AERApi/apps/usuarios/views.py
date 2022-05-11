from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import Users
from django.http import HttpResponse


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Users.objects.all().order_by('id_user')
    serializer_class = UserSerializer
    filterset_fields = ['country', 'institution', 'name', 'nick']

    # @link()
    # def by_accepteds(self, request, *args, **kwargs):
    #     users = self.get_object()
    #     data = users.all()
    #     serializer = UserSerializer(data)
    #     return Response(serializer.data)
