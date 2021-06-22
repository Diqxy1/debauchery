from django.urls import path

from .views import CoachsAPIView, CoachAPIView, EvaluationsAPIView, EvaluationAPIView

urlpatterns = [
    # coachs routes
    path('coachs/', CoachsAPIView.as_view(), name='coachs'),
    path('coachs/<int:pk>/', CoachAPIView.as_view(), name='coach'),
    path('coachs/<int:coach_pk>/avaliacoes/', EvaluationsAPIView.as_view(), name='coach_avaliacoes'),
    path('coachs/<int:coach_pk>/avaliacoes/<int:evaluation_pk>/', EvaluationsAPIView.as_view(),
         name='coach_avaliacoes'),
    # evaluation rotes
    path('avaliacoes/', EvaluationsAPIView.as_view(), name='avaliacoes'),
    path('avaliacoes/<int:evaluation_pk>/', EvaluationAPIView.as_view(), name='avaliacoes')
]
