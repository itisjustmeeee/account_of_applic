from django.shortcuts import render, redirect, get_object_or_404
from .models import Category
from .forms import CategoryForm
from django.db.models.deletion import ProtectedError
from django.db.models import Count


def category_list(request):
    categories = Category.objects.annotate(
        requests_count=Count('requests')
    ).order_by('name')

    return render(
        request,
        'category/category_list.html',
        {
            'categories': categories
        },
    )


def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('category:list')

    else:
        form = CategoryForm()

    return render(
        request,
        'category/create_category.html',
        {'form': form},
    )


def editCategory(request, category_id):
    current_category = get_object_or_404(
        Category,
        pk=category_id
    )

    form = CategoryForm(
        request.POST if request.method == 'POST' else None,
        instance=current_category,
    )

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect(
            'category:list'
        )

    return render(
        request,
        'category/edit_category.html',
        {
            'form': form,
            'category': current_category
        }
    )


def deleteCategory(request, category_id):
    current_category = get_object_or_404(
        Category,
        pk=category_id
    )

    requests_count = current_category.requests.count()

    if request.method == 'POST':

        if requests_count > 0:
            return render(
                request,
                'category/confirm_delete.html',
                {
                    'category': current_category,
                    'requests_count': requests_count,
                    'error': 'Нельзя удалить категорию, которая есть в заявках'
                },
                status=409,
            )

        try:
            current_category.delete()

        except ProtectedError:
            return render(
                request,
                'category/confirm_delete.html',
                {
                    'category': current_category,
                    'requests_count': current_category.requests.count(),
                    'error': 'Категория используется и не может быть удалена',
                },
                status=409,
            )

        return redirect(
            'category:list'
        )

    return render(
        request,
        'category/confirm_delete.html',
        {
            'category': current_category,
            'requests_count': requests_count,
        }
    )
