from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.accounts.api.viewsets import UserViewSet
from apps.coachs.api.viewsets import CoachViewSet, ReviewViewSet

router = DefaultRouter()

router.register('users', UserViewSet)
router.register('coachs', CoachViewSet)
router.register('avaliacoes', ReviewViewSet)

routes = router.urls