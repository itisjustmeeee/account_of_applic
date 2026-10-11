from django.shortcuts import render
from django.http import HttpResponse


def user_request(request):
    return render(
        request,
        'user_requests/user_request.html'
    )


def page_not_found(request, exception):
    return HttpResponse(
        '<h2>страница не найдена. ID должно быть положительным целым числом</h2>',
        status=404
    )
