from .models import UserRequest
from .utils import filter_requests
from django.shortcuts import render, redirect
from django.http import HttpResponse


def user_request(request):
    search = request.GET.get('search', '').strip()
    status = request.GET.get('status', '')

    requests = filter_requests(
        UserRequest.objects.all(),
        search=search,
        status=status,
    )

    return render(
        request,
        'user_requests/user_request.html',
        {
            'requests': requests,
            'search': search,
            'status': status,
        }
    )


def page_not_found(request, exception):
    return HttpResponse(
        '<h2>страница не найдена. '
        'ID должно быть положительным целым числом</h2>',
        status=404,
    )


def create_request(request):
    

    return render(
        request,
        'user_requests/create_request.html',
        {
            'categories': categories,
            'users': users,
        },
    )


def request_detail(request, request_id):
    requests = load_json(DATA_FILE)

    for item in requests:
        if item['id'] == request_id:
            return render(
                request,
                'user_requests/request_detail.html',
                {
                    'request': item,
                },
            )

    return page_not_found(request, None)
