from rest_framework import generics
from rest_framework.generics import get_object_or_404

from .models import Coach, Evaluation
from .serializers import CoachSerializer, EvaluationSerializer


class CoachsAPIView(generics.ListCreateAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer


class CoachAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer


class EvaluationsAPIView(generics.ListCreateAPIView):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer

    def get_queryset(self):
        if self.kwargs.get('coach_pk'):
            return self.queryset.filter(coach_id=self.kwargs.get('coach_pk'))
        return self.queryset.all()


class EvaluationAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer

    def get_object(self):
        if self.kwargs.get('coach_pk'):
            return get_object_or_404(self.get_queryset(),
                                     curso_id=self.kwargs.get('coach_pk'),
                                     pk=self.kwargs.get('evaluation_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('evaluation_pk'))
