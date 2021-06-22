from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import CoachViewSet, ReviewViewSet


router = SimpleRouter()
router.register('coachs', CoachViewSet)
router.register('avaliacoes', ReviewViewSet)
