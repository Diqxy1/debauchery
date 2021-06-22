from django.contrib import admin

from .models import Coach, Assessment


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'url', 'created_at', 'updated_at', 'is_active')


@admin.register(Assessment)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('coach', 'name', 'email', 'valuation', 'created_at', 'updated_at', 'is_active')