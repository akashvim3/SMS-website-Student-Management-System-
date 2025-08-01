from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """Admin configuration for UserProfile model"""
    list_display = ('user', 'user_type', 'phone_number')
    list_filter = ('user_type',)
    search_fields = ('user__username', 'user__email', 'user__first_name', 'user__last_name')
    fieldsets = (
        ('User Information', {
            'fields': ('user', 'user_type')
        }),
        ('Personal Information', {
            'fields': ('date_of_birth', 'address', 'phone_number', 'profile_picture')
        }),
        ('Student Information', {
            'fields': ('student_id', 'admission_date'),
            'classes': ('collapse',),
        }),
        ('Teacher Information', {
            'fields': ('teacher_id', 'qualification', 'joining_date'),
            'classes': ('collapse',),
        }),
    )
