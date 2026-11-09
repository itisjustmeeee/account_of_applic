from django.contrib import admin
from .models import RequestStatus


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
