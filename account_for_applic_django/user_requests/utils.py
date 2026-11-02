
from django.db.models import Q
from django.db.models.functions import Trim


def filter_requests(queryset, search='', status='',
                    unanswered_only=False):
    if unanswered_only:
        queryset = (
            queryset
            .annotate(answer_trimmed=Trim('answer'))
            .filter(answer_trimmed='')
        )

    if status:
        queryset = queryset.filter(status=status)

    search = search.strip()

    if search:
        condition = (
            Q(title_icontains=search)
            | Q(user_icontains=search)
            | Q(category_icontains=search)
            | Q(description_icontains=search)
            | Q(status_icontains=search)
            | Q(priority_icontains=search)
        )

        if search.isdigit():
            condition |= Q(pk=int(search))

        queryset = queryset.filter(condition)

    return queryset
