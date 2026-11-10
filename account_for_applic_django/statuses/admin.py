from django.contrib import admin
from .models import RequestStatus
from user_requests.models import UserRequest


class UserRequestInline(admin.TabularInline):
    model = UserRequest

    extra = 0
    can_delete = False
    show_change_link = True

    fields = (
        'id',
        'user',
        'category',
        'priority',
        'created_at',
    )

    readonly_fields = (
        'id',
        'user',
        'category',
        'priority',
        'created_at',
    )

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(RequestStatus)
class RequestStatusAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name'
    )

    search_fields = (
        'name',
    )

    ordering = (
        '-id',
    )

    list_per_page = 20

    fields = (
        'name',
    )

    inlines = [
        UserRequestInline,
    ]
