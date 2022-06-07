from apps.usuarios.serializers import UserSerializerWithoutProblems
from .models import Institutions
from rest_framework import serializers


class InstitutionsSerializer(serializers.HyperlinkedModelSerializer):
    users = UserSerializerWithoutProblems(read_only=True, many=True)

    class Meta:
        model = Institutions
        fields = ['id', 'name', 'problems_solved', 'shipments', 'logo_src', 'users', ]
