from django.urls import path
from . import views

app_name = 'user_requests'

urlpatterns = [
    path('', views.user_request, name='list'),
    path('create/', views.create_request, name='create'),
    path(
        '<int:request_id>/',
        views.request_detail,
        name='detail',
    )
]
