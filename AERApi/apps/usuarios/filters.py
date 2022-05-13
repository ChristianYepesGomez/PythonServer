import django_filters
from .models import Users


class UsersFilter(django_filters.FilterSet):
    class Meta:
        model = Users
        fields = {
            'nick': ['exact'],
            'name': ['exact'],
            'country': ['exact'],
            'institution': ['contains'],
            'accepteds': ['lt', 'gt'],
        }
