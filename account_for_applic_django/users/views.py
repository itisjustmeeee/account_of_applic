from django.shortcuts import render, get_object_or_404
from .models import UserProfile


def index(request):
    profiles = UserProfile.objects.select_related(
        'user'
    ).filter(
        user__is_active=True
    ).order_by('user__username')

    return render(
        request,
        'users/user_list.html',
        {
            'profiles': profiles,
        },
    )


def user_detail(request, user_id):
    profile = get_object_or_404(
        UserProfile.objects.select_related('user'),
        user_id=user_id,
        user__is_active=True
    )

    return render(
        request,
        'users/user_detail.html',
        {
            'profile': profile
        }
    )
