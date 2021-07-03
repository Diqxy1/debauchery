from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import mixins

from accounts.permissions import IsOwner
from .models import Coach, Review
from .serializers import CoachSerializer, ReviewSerializer


class CoachViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsOwner)
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer

    @action(detail=True, methods=['get'])
    def reviews(self, request, pk=None):
        self.pagination_class.page_size = 1
        reviews = Review.objects.filter(coach_id=pk)
        page = self.paginate_queryset(reviews)

        if page is not None:
            serializer = ReviewSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = ReviewSerializer(reviews, many=True)

        return Response(serializer.data)


class ReviewViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
