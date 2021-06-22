from rest_framework import generics
from rest_framework.generics import get_object_or_404
# import from api-v2
from rest_framework import viewsets

from .models import Coach, Assessment
from .serializers import CoachSerializer, AssessmentSerializer

"""
API V1
"""


class CoachsAPIView(generics.ListCreateAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer


class CoachAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer


class AssessmentsAPIView(generics.ListCreateAPIView):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer

    def get_queryset(self):
        if self.kwargs.get('coach_pk'):
            return self.queryset.filter(coach_id=self.kwargs.get('coach_pk'))
        return self.queryset.all()


class AssessmentAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer

    def get_object(self):
        if self.kwargs.get('coach_pk'):
            return get_object_or_404(self.get_queryset(),
                                     curso_id=self.kwargs.get('coach_pk'),
                                     pk=self.kwargs.get('assessment_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('assessment_pk'))
