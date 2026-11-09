from django.contrib import admin
from .models import Answer


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'author',
        'request',
        'short_text',
        'created_at'
    )

    list_filter = (
        'author',
    )

    search_fields = (
        'text',
        'author__username',
        'request__description',
    )

    date_hierarchy = 'created_at'

    ordering = (
        '-id',
    )

    list_per_page = 20

    list_select_related = (
        'author',
        'request',
    )

    readonly_fields = (
        'created_at',
    )

    fields = (
        'request',
        'author',
        'text',
        'created_at',
    )

    @admin.display(description='Текст ответа')
    def short_text(self, obj):
        if len(obj.text) > 70:
            return obj.text[:70] + '...'
        return obj.text
