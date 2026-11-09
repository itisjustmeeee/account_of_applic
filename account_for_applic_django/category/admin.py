from django.contrib import admin
from .models import Category


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

    @admin.display(description='Описание категории')
    def short_description(self, obj):
        if len(obj.description) > 70:
            return obj.description[:70] + '...'
        return obj.description
