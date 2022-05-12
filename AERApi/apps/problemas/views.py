from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import ProblemSerializer, ProblemSerializerWithCategories
from .models import Problems
from django.shortcuts import get_object_or_404


# Create your views here


class ProblemViewSet(viewsets.GenericViewSet):
    """
    Standar view for Problems


    Return all problem without the field 'categories'
    """
    model = Problems
    serializer_class = ProblemSerializer
    queryset = None

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self):
        return self.model.objects.all()

    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        return Response(data.data)

    def retrieve(self, request, pk=None):
        problem = self.get_object(pk)
        problem_serializer = self.serializer_class(problem)
        return Response(problem_serializer.data)

    # @action(methods=['get'], detail=False)
    # def get_problems_by_accepteds(self, request):
    #     print(request.query_params)
    #     problems_by_accepteds = self.get_queryset().order_by('accepteds')
    #     serializer = self.get_serializer_class()(problems_by_accepteds)
    #     return Response(serializer.data)


class ProblemViewSetWithCategories(viewsets.GenericViewSet):
    """
    Comentarios
    """
    model = Problems
    serializer_class = ProblemSerializerWithCategories
    queryset = None

    def get_queryset(self):
        return self.model.objects.all()

    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        return Response(data.data)


class ProblemViewByAccepteds(viewsets.GenericViewSet):
    """
    Comentarios
    """
    model = Problems
    serializer_class = ProblemSerializerWithCategories
    queryset = None

    def get_queryset(self):
        return self.model.objects.all().order_by('-accepteds')

    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        return Response(data.data)


class ProblemViewByCompletedPercentage(viewsets.GenericViewSet):
    """
    Comentarios
    """
    model = Problems
    serializer_class = ProblemSerializerWithCategories
    queryset = None

    def get_queryset(self):
        return self.model.objects.all().order_by('-percentage_users_completed')

    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        return Response(data.data)
