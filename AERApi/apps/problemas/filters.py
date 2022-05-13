import django_filters
from .models import Problems


class ProblemFilter(django_filters.FilterSet):
    class Meta:
        model = Problems
        fields = {
            'percentage_users_completed': ['lt', 'gt'],
            'id_problem': ['exact'],
            'title': ['contains']
        }
