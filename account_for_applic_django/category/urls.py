from django.urls import path
from . import views


app_name = 'category'

urlpatterns = [
    path('', views.category_list, name='list'),
    path('create/', views.create_category, name='create'),
    path(
        '<int:category_id>/edit/',
        views.editCategory,
        name='edit',
    ),
    path(
        '<int:category_id>/delete/',
        views.deleteCategory,
        name='delete',
    ),
]
