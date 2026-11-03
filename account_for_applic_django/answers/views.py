from user_requests.models import UserRequest
from statuses.models import RequestStatus
from users.models import UserProfile
from .models import Answer
from user_requests.utils import filter_requests, paginate_queryset
from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction


def answer_list(request):
    search = request.GET.get('search', '')
    status = request.GET.get('status', '')

    requests = filter_requests(
        UserRequest.objects.select_related(
            'user',
            'category',
            'status',
        ),
        search=search,
        status=status,
        unanswered_only=True,
    )

    page_obj, pagination_query = paginate_queryset(
        request,
        requests,
        per_page=10,
    )

    return render(
        request,
        'answers/answer_list.html',
        {
            'requests': page_obj.object_list,
            'page_obj': page_obj,
            'pagination_query': paginate_queryset,
            'search': search,
            'status': status,
        },
    )


def add_answer(request, request_id):
    current_request = get_object_or_404(
        UserRequest,
        pk=request_id,
    )

    admin_profiles = UserProfile.objects.filter(
        role='admin',
        user__is_active=True,
    ).select_related(
        'user'
    ).order_by(
        'user__username'
    )

    if Answer.objects.filter(
        request=current_request,
    ).exists():
        return redirect('answers:list')

    error = ''
    selected_author_id = ''

    if request.method == 'POST':
        answer_text = request.POST.get(
            'answer',
            '',
        ).strip()

        author_id = request.POST.get(
            'author',
            '',
        )

        author_profile = admin_profiles.filter(
            user_id=author_id,
        ).first()

        if not answer_text:
            error = 'Введите текст ответа'

        elif author_profile is None:
            error = 'Выберите администратора из списка'

        else:
            completed_status = get_object_or_404(
                RequestStatus,
                name='Завершена',
            )

            with transaction.atomic():
                Answer.objects.create(
                    request=current_request,
                    author=author_profile.user,
                    text=answer_text,
                )

                current_request.status = completed_status

                current_request.save(
                    update_fields=['status'],
                )
            return redirect('answers:list')

        if author_id.isdigit():
            selected_author_id = int(author_id)

    return render(
        request,
        'answers/add_answer.html',
        {
            'request_item': current_request,
            'admin_profiles': admin_profiles,
            'selected_author_id': selected_author_id,
            'error': error,
        },
    )
