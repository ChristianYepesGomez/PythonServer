import django_filters
from .models import Problems
from django_property_filter import *


class ProblemFilter(PropertyFilterSet):
    # percentage_users_completed = PropertyDateFilter(field_name='percentage_users_completed', lookup_expr='gte')

    class Meta:
        model = Problems
        fields = {
            'id_problem': ['exact'],
            'title': ['contains']
        }
        property_fields = [
            ('percentage_users_completed', PropertyNumberFilter, ['lte', 'gte'])
        ]
