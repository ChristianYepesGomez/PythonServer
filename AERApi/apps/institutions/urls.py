from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'base', views.InstitutionViewSet, basename="institutions")

urlpatterns = [
    path('', include(router.urls)),
]
