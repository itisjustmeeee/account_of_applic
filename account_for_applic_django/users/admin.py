from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model


User = get_user_model()


class UserProfileInline(admin.StackedInline):
    model = UserProfile

    can_delete = False
    extra = 1
    max_num = 1

    fields = (
        'role',
    )


class UserAdmin(BaseUserAdmin):
    inlines = [
        UserProfileInline,
    ]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

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
