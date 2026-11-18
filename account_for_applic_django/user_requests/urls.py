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
    ),
    path(
        '<int:request_id>/edit/',
        views.editRequest,
        name='edit'
    ),
    path(
        '<int:request_id>/change-status/',
        views.changeRequestStatus,
        name='change_status'
    ),
    path(
        '<int:request_id>/delete/',
        views.deleteRequest,
        name='delete'
    ),
]
