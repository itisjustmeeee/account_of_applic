from user_requests.models import UserRequest
from statuses.models import RequestStatus
from .models import Answer
from user_requests.utils import filter_requests, paginate_queryset
from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from user_requests.forms import AnswerRequestFilterForm
from .forms import AnswerCreateForm


def answer_list(request):

    filter_form = AnswerRequestFilterForm(request.GET)

    requests = UserRequest.objects.filter(
        answer_record__isnull=True
    ).select_related(
            'user',
            'category',
            'status',
    )

    if filter_form.is_valid():
        requests = filter_requests(
            requests,
            search=filter_form.cleaned_data['search'],
            status=filter_form.cleaned_data['status'],
            category=filter_form.cleaned_data['category'],
            priority=filter_form.cleaned_data['priority'],
        )
    else:
        requests = requests.none()

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
            'pagination_query': pagination_query,
            'filter_form': filter_form
        },
    )


def add_answer(request, request_id):

    current_request = get_object_or_404(
        UserRequest.objects.select_related(
            'user',
            'category',
            'status',
        ),
        pk=request_id,
    )

    if Answer.objects.filter(
        request=current_request
    ).exists():
        return redirect('answers:list')

    form = AnswerCreateForm(
        request.POST if request.method == 'POST' else None,
        request.FILES if request.method == 'POST' else None,
    )

    if request.method == 'POST' and form.is_valid():

        completed_status = RequestStatus.objects.filter(
            name='Завершена'
        ).first()

        if completed_status is None:
            form.add_error(
                None,
                'Отсутствует статус "Завершена"',
            )
        else:
            with transaction.atomic():

                answer = form.save(commit=False)

                answer.request = current_request

                answer.save()

                current_request.status = completed_status

                current_request.save(
                    update_fields=['status']
                )

            return redirect('answers:list')

    return render(
        request,
        'answers/add_answer.html',
        {
            'request_item': current_request,
            'form': form,
        },
    )


def editAnswer(request, request_id):
    current_request = get_object_or_404(
        UserRequest,
        pk=request_id
    )

    answer = get_object_or_404(
        Answer,
        request=current_request
    )

    form = AnswerCreateForm(
        request.POST if request.method == 'POST' else None,
        request.FILES if request.method == 'POST' else None,
        instance=answer
    )

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect(
            'user_requests:detail',
            request_id=request_id
        )

    return render(
        request,
        'answers/edit_answer.html',
        {
            'form': form,
            'answer': answer,
            'request': current_request,
        }
    )


def deleteAnswer(request, request_id):
    current_request = get_object_or_404(
        UserRequest,
        pk=request_id
    )

    answer = get_object_or_404(
        Answer,
        request=current_request
    )

    if request.method == 'POST':
        answer.delete()
        return redirect(
            'user_requests:detail',
            request_id=request_id
        )

    return render(
        request,
        'answers/confirm_delete.html',
        {
            'answer': answer,
            'request': current_request,
        }
    )
