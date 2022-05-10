from AERApi.applications.usuarios.models import Users, BlacklistUsers
from AERApi.applications.categorias.models import Categories
from AERApi.applications.problemas.models import Problems, ProblemsCategories

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ['id_user', 'nick', 'name', 'country', 'institution', 'logo_src', 'shipments', 'total_accepteds',
                  'intents', 'accepteds']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categories
        fields = ['id_category', 'name', 'related_category']


class ProblemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Problems
        fields = ['id_problem', 'title', 'no_repeated_accepteds', 'wrong_answer', 'accepteds', 'shipments',
                  'time_limit', 'memory_limit', 'presentation_error', 'attempts', 'other', 'restricted_function',
                  'compilation_error', 'c_shipments', 'cpp_shipments', 'java_shipments']


class BlackListUsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Problems
        fields = ['url', 'name']
