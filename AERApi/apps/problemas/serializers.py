from .models import Problems
from apps.categorias.models import Categories

from rest_framework import serializers


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categories
        fields = ('name',)


class ProblemSerializer(serializers.HyperlinkedModelSerializer):
    categories = CategorySerializer(read_only=True, many=True)

    class Meta:
        model = Problems
        fields = ['id_problem', 'title', 'no_repeated_accepteds', 'wrong_answer', 'accepteds', 'shipments',
                  'time_limit', 'memory_limit', 'presentation_error', 'attempts', 'other', 'restricted_function',
                  'compilation_error', 'c_shipments', 'cpp_shipments', 'java_shipments', 'categories']
