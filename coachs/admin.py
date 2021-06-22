from django.contrib import admin

from .models import Coach, Evaluation


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'url', 'created_at', 'updated_at', 'is_active')


@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('coach', 'name', 'email', 'evaluation', 'created_at', 'updated_at', 'is_active')