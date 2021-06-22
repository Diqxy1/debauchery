from django.urls import path

from .views import CoachsAPIView, CoachAPIView, AssessmentsAPIView, AssessmentAPIView

urlpatterns = [
    # coachs routes
    path('coachs/', CoachsAPIView.as_view(), name='coachs'),
    path('coachs/<int:pk>/', CoachAPIView.as_view(), name='coach'),
    path('coachs/<int:coach_pk>/avaliacoes/', AssessmentsAPIView.as_view(), name='coach_avaliacoes'),
    path('coachs/<int:coach_pk>/avaliacoes/<int:assessment_pk>/', AssessmentsAPIView.as_view(),
         name='coach_avaliacoes'),
    # evaluation rotes
    path('avaliacoes/', AssessmentAPIView.as_view(), name='avaliacoes'),
    path('avaliacoes/<int:assessment_pk>/', AssessmentAPIView.as_view(), name='avaliacoes')
]
