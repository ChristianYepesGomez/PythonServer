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
        fields = ['url', 'name']


class ProblemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:

        model = Problems
        fields = ['url', 'name']

class BlacListUsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:

        model = Problems
        fields = ['url', 'name']