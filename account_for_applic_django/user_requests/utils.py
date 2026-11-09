from .models import UserRequest
from django.db.models import Q
from django.core.paginator import Paginator


def filter_requests(
    queryset,
    search='',
    status='',
    unanswered_only=False,
):
    if unanswered_only:
        queryset = queryset.filter(
            answer_record__isnull=True
        )

    if status:
        queryset = queryset.filter(
            status__name=status
        )

    search = (search or '').strip()

    if search:
        condition = Q()

        priority_values = [
            value
            for value, label in UserRequest.Priority.choices
            if search.casefold() in label.casefold()
        ]

        condition |= (
            Q(description__unicode_icontains=search)
            | Q(user__username__unicode_icontains=search)
            | Q(category__name__unicode_icontains=search)
            | Q(status__name__unicode_icontains=search)
            | Q(priority__unicode_icontains=search)
            | Q(priority__in=priority_values)
            | Q(answer_record__text__unicode_icontains=search)
        )

        if search.isdigit():
            condition |= Q(pk=int(search))

        queryset = queryset.filter(condition)

    return queryset


def paginate_queryset(request, queryset, per_page=10):
    paginator = Paginator(queryset, per_page)

    page_obj = paginator.get_page(
        request.GET.get('page')
    )

    query_params = request.GET.copy()
    query_params.pop('page', None)

    pagination_query = query_params.urlencode()

    return page_obj, pagination_query
