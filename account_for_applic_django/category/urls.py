from django.urls import path
from . import views


app_name = 'category'

urlpatterns = [
    path('', views.category_list, name='list'),
    path('create/', views.create_category, name='create')
]
