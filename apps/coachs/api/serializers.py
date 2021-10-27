from rest_framework import serializers

from apps.coachs.models import Coach, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Review
        fields = (
            'id',
            'coach',
            'name',
            'email',
            'comment',
            'valuation',
            'created_at',
            'updated_at'
        )


class CoachSerializer(serializers.ModelSerializer):
    reviews = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='review-detail')

    class Meta:
        model = Coach
        fields = (
            'id',
            'title',
            'description',
            'url',
            'created_at',
            'updated_at',
            'is_active',
            'reviews'
        )
