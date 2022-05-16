from .models import Categories
from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    related_category = RecursiveField()

    class Meta:
        model = Categories
        fields = ['name', 'related_category']

# CategorySerializer._declared_fields['related_category'] = CategorySerializer()
