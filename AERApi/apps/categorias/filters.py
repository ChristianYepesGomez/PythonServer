import django_filters
from .models import Categories
from django_property_filter import *


class CategoriesFilter(django_filters.FilterSet):
    class Meta:
        model = Categories
        fields = {
            'name': ['contains']
        }
