from django.contrib.auth.models import User
from django.db.models import (
    Avg,
    Count,
    F,
    Max,
    Min,
    Q,
    Value,
    Case,
    When,
    FloatField,
    ExpressionWrapper
)
from django.shortcuts import render
from user_requests.models import UserRequest
from user_requests.utils import paginate_queryset


def statictics(request):
    requests_queryset = UserRequest.objects.annotate(
        priority_number=Case(
            When(priority='Низкий', then=Value(1.0)),
            When(priority='Средний', then=Value(2.0)),
            When(priority='Высокий', then=Value(3.0)),
            default=Value(None, output_field=FloatField()),
            output_field=FloatField(),
        )
    )

    total_stats = requests_queryset.aggregate(
        total_requests=Count('id'),
        average_priority=Avg('priority_number'),
        max_priority=Max('priority_number'),
        min_priority=Min('priority_number'),
        answered_requests=Count(
            'id',
            filter=Q(answer_record__isnull=False),
        ),
        unanswered_requests=Count(
            'id',
            filter=Q(answer_record__isnull=True)
        ),
    )

    categories_stats = (
        UserRequest.objects
        .values(
            'category__name',
        )
        .annotate(
            request_count=Count('id'),
        )
        .order_by('-request_count', 'category__name')
    )

    statuses_stats = (
        UserRequest.objects
        .values(
            'status__name',
        )
        .annotate(
            request_count=Count('id'),
        )
        .order_by('-request_count', 'status__name')
    )

    users_stats = (
        User.objects
        .annotate(
            requests_count=Count(
                'requests',
            ),
        )
        .filter(
            requests_count__gt=0,
        )
        .order_by(
            '-requests_count',
            'username',
        )
    )

    average_priority = total_stats['average_priority'] or 0.0

    requests_with_difference = (
        requests_queryset
        .annotate(
            priority_difference=ExpressionWrapper(
                F('priority_number')
                - Value(
                    average_priority,
                    output_field=FloatField(),
                ),
                output_field=FloatField(),
            )
        )
        .select_related(
            'user',
            'category',
            'status'
        )
        .order_by(
            '-priority_difference'
        )
    )

    page_obj, pagination_query = paginate_queryset(
        request,
        requests_with_difference,
        per_page=5,
    )

    context = {
        'total_stats': total_stats,
        'categories_stats': categories_stats,
        'statuses_stats': statuses_stats,
        'users_stats': users_stats,
        'page_obj': page_obj,
        'pagination_query': pagination_query,
    }

    return render(
        request,
        'statictics/statictics.html',
        context,
    )
