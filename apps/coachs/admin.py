from django.contrib import admin

from .models import Coach, Review


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'url', 'created_at', 'updated_at', 'is_active')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('coach', 'name', 'email', 'valuation', 'created_at', 'updated_at', 'is_active')
