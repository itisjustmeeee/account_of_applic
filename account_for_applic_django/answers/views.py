from user_requests.models import UserRequest
from user_requests.utils import filter_requests
from django.shortcuts import render, redirect, get_object_or_404


def answer_list(request):
    search = request.GET.get('search', '')
    status = request.GET.get('status', '')

    requests = filter_requests(
        UserRequest.objects.all(),
        search=search,
        status=status,
        unanswered_only=True
    )

    return render(
        request,
        'answers/answer_list.html',
        {
            'requests': requests,
            'search': search,
            'status': status,
        },
    )


def add_answer(request, request_id):
    current_request = get_object_or_404(
        UserRequest,
        pk=request_id,
    )

    if current_request.answer.strip():
        return redirect('answers:list')

    error = ''

    if request.method == 'POST':
        answer = request.POST.get('answer', '').strip()

        if answer:
            current_request.answer = answer
            current_request.status = 'Решена'

            current_request.save(
                update_fields=['answer', 'status']
            )

            return redirect('answers:list')
        error = 'Введите текст ответа'

    return render(
        request,
        'answers/add_answer.html',
        {
            'request_item': current_request,
            'error': error,
        },
    )
