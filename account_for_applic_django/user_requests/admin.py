from django.contrib import admin
from .models import UserRequest
from answers.models import Answer
from django.contrib.auth import get_user_model


User = get_user_model()


class AnswerInline(admin.StackedInline):
    model = Answer

    extra = 1
    max_num = 1

    fields = (
        'author',
        'text',
        'created_at',
    )

    readonly_fields = (
        'created_at',
    )

    def formfield_for_foreignkey(
            self,
            db_field,
            request,
            **kwargs
    ):
        if db_field.name == 'author':
            kwargs['queryset'] = User.objects.filter(
                is_active=True,
                profile__role='admin',
            ).order_by('username')

        return super().formfield_for_foreignkey(
            db_field,
            request,
            **kwargs,
        )


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

    inlines = [
        AnswerInline,
    ]

    @admin.display(description='Описание заявки')
    def short_description(self, obj):
        if len(obj.description) > 70:
            return obj.description[:70] + '...'
        return obj.description
