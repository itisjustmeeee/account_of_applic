from django.contrib import admin
from .models import Category
from user_requests.models import UserRequest


class UserRequestInline(admin.TabularInline):
    model = UserRequest

    extra = 0
    can_delete = False
    show_change_link = True

    fields = (
        'id',
        'user',
        'status',
        'priority',
        'created_at',
    )

    readonly_fields = (
        'id',
        'user',
        'status',
        'priority',
        'created_at',
    )

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'short_description',
    )

    search_fields = (
        'name',
        'description'
    )

    ordering = (
        '-id',
    )

    list_per_page = 20

    fields = (
        'name',
        'description',
    )

    inlines = [
        UserRequestInline,
    ]

    @admin.display(description='Описание категории')
    def short_description(self, obj):
        if len(obj.description) > 70:
            return obj.description[:70] + '...'
        return obj.description
