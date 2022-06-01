from apps.usuarios.serializers import UserSerializer
from .models import Institutions
from rest_framework import serializers


class InstitutionsSerializer(serializers.HyperlinkedModelSerializer):
    users = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Institutions
        fields = ['id', 'name', 'problems_solved', 'shipments', 'logo_src', 'users', ]
