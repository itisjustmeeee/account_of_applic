from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'role',
    )

    list_filter = (
        'role',
    )

    search_fields = (
        'user__username',
    )

    ordering = (
        '-id',
    )

    list_per_page = 20

    list_select_related = (
        'user',
    )

    fields = (
        'user',
        'role',
    )
