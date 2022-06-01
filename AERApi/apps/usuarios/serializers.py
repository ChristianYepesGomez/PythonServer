from .models import Users, BlacklistUsers
from apps.problemas.serializers import ProblemSerializerShort

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # problems_attempted = ProblemSerializerShort(read_only=True, many=True)

    class Meta:
        model = Users
        fields = ['id_user', 'nick', 'name', 'country', 'institution', 'logo_src', 'shipments', 'total_accepteds',
                  'intents', 'accepteds', ]


class BlackListUsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BlacklistUsers
        fields = ['id_blacklist', 'number_user']
