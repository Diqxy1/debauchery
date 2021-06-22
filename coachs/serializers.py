from rest_framework import serializers

from .models import Coach, Assessment


class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Assessment
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
    class Meta:
        model = Coach
        fields = (
            'id',
            'title',
            'description',
            'url',
            'created_at',
            'updated_at',
            'is_active'
        )
