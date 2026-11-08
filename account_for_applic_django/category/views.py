from django.shortcuts import render, redirect
from .models import Category
from .forms import CategoryForm


def category_list(request):
    categories = Category.objects.all()

    return render(
        request,
        'category/category_list.html',
        {'categories': categories},
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
