from .models import UserRequest
from category.models import Category
from statuses.models import RequestStatus
from .utils import filter_requests, paginate_queryset
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import get_user_model

User = get_user_model()


def user_request(request):
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
    )

    page_obj, pagination_query = paginate_queryset(
        request,
        requests,
        per_page=10,
    )

    return render(
        request,
        'user_requests/user_request.html',
        {
            'requests': page_obj.object_list,
            'page_obj': page_obj,
            'pagination_query': pagination_query,
            'search': search,
            'status': status,
        },
    )


def page_not_found(request, exception):
    return HttpResponse(
        '<h2>страница не найдена. '
        'ID должно быть положительным целым числом</h2>',
        status=404,
    )


def create_request(request):
    categories = Category.objects.all()
    users = User.objects.filter(is_active=True)

    error = ''
    selected_priority = ''

    if request.method == 'POST':
        description = request.POST.get(
            'description',
            '',
        ).strip()

        category_id = request.POST.get('category')
        user_id = request.POST.get('user')
        priority = request.POST.get('priority', '')

        selected_priority = priority

        if not description:
            error = 'Введите описание заявки'

        elif priority not in UserRequest.Priority.values:
            error = 'Выберите корректный приоритет'

        else:
            user = get_object_or_404(
                User,
                pk=user_id,
                is_active=True,
            )

            category = get_object_or_404(
                Category,
                pk=category_id,
            )

            status = get_object_or_404(
                RequestStatus,
                name='Новая',
            )

            UserRequest.objects.create(
                user=user,
                category=category,
                status=status,
                description=description,
                priority=priority,
            )

            return redirect('user_requests:list')

    return render(
        request,
        'user_requests/create_request.html',
        {
            'categories': categories,
            'users': users,
            'error': error,
            'priority_choices': UserRequest.Priority.choices,
            'selected_priority': selected_priority,
        },
    )


def request_detail(request, request_id):
    current_request = get_object_or_404(
        UserRequest.objects.select_related(
            'user',
            'category',
            'status',
        ),
        pk=request_id,
    )

    return render(
        request,
        'user_requests/request_detail.html',
        {
            'request': current_request,
        },
    )
