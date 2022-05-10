from .models import Categories

from rest_framework import serializers


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categories
        fields = ['name', 'related_category']


CategorySerializer._declared_fields['related_category'] = CategorySerializer()
