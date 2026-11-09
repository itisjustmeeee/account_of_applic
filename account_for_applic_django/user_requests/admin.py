from django.contrib import admin
from .models import UserRequest


@admin.register(UserRequest)
class UserRequestAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'category',
        'status',
        'short_description',
        'priority',
        'created_at',
    )

    list_filter = (
        'user',
        'category',
        'status',
        'priority',
    )

    search_fields = (
        'user__username',
        'category__name',
        'status__name',
        'description',
    )

    date_hierarchy = 'created_at'

    ordering = (
        '-id',
    )

    list_per_page = 20

    list_select_related = (
        'user',
        'category',
        'status'
    )

    readonly_fields = (
        'created_at',
    )

    fields = (
        'user',
        'category',
        'status',
        'description',
        'priority',
        'created_at',
    )

    @admin.display(description='Описание заявки')
    def short_description(self, obj):
        if len(obj.description) > 70:
            return obj.description[:70] + '...'
        return obj.description
