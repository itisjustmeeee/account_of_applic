from .models import UserRequest
from statuses.models import RequestStatus
from .utils import filter_requests, paginate_queryset
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from .forms import (
    RequestFilterForm,
    UserRequestCreateForm,
    UserRequestUpdateForm,
    RequestStatusForm
)
from django.views.decorators.http import require_POST

User = get_user_model()


def user_request(request):

    filter_form = RequestFilterForm(request.GET)

    requests = UserRequest.objects.select_related(
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
            unanswered_only=filter_form.cleaned_data['unanswered_only'],
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
        'user_requests/user_request.html',
        {
            'requests': page_obj.object_list,
            'page_obj': page_obj,
            'pagination_query': pagination_query,
            'filter_form': filter_form
        },
    )


def page_not_found(request, exception):
    return render(
        request,
        '404.html',
        status=404
    )


def create_request(request):

    form = UserRequestCreateForm(
        request.POST if request.method == 'POST' else None,
        request.FILES if request.method == 'POST' else None,
    )

    if request.method == 'POST' and form.is_valid():
        status = RequestStatus.objects.filter(
            name='Новая'
        ).first()

        if status is None:
            form.add_error(
                None,
                'Отсутствует статус "Новая"',
            )
        else:
            new_request = form.save(commit=False)

            new_request.status = status

            new_request.save()

            return redirect('user_requests:list')

    return render(
        request,
        'user_requests/create_request.html',
        {
            'form': form
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

    status_form = RequestStatusForm(
        instance=current_request
    )

    return render(
        request,
        'user_requests/request_detail.html',
        {
            'request': current_request,
            'status_form': status_form,
        },
    )


def editRequest(request, request_id):
    current_request = get_object_or_404(
        UserRequest,
        pk=request_id
    )

    form = UserRequestUpdateForm(
        request.POST if request.method == 'POST' else None,
        request.FILES if request.method == 'POST' else None,
        instance=current_request
    )

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect(
            'user_requests:detail',
            request_id=request_id
        )

    return render(
        request,
        'user_requests/edit_request.html',
        {
            'form': form,
            'request': current_request,
        }
    )


@require_POST
def changeRequestStatus(request, request_id):
    current_request = get_object_or_404(
        UserRequest,
        pk=request_id
    )

    form = RequestStatusForm(
        request.POST,
        instance=current_request
    )

    if form.is_valid():
        form.save()
        return redirect(
            'user_requests:detail',
            request_id=request_id
        )

    return render(
        request,
        'user_requests/request_detail.html',
        {
            'request': current_request,
            'status_form': form,
        },
        status=400
    )


def deleteRequest(request, request_id):
    current_request = get_object_or_404(
        UserRequest,
        pk=request_id
    )

    if request.method == 'POST':
        current_request.delete()
        return redirect('user_requests:list')

    return render(
        request,
        'user_requests/confirm_delete.html',
        {
            'request': current_request
        }
    )
