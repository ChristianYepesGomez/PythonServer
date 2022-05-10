from .models import Problems, ProblemsCategories

from rest_framework import serializers

class ProblemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Problems
        fields = ['id_problem', 'title', 'no_repeated_accepteds', 'wrong_answer', 'accepteds', 'shipments',
                  'time_limit', 'memory_limit', 'presentation_error', 'attempts', 'other', 'restricted_function',
                  'compilation_error', 'c_shipments', 'cpp_shipments', 'java_shipments']
