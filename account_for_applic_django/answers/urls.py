from django.urls import path
from . import views

app_name = 'answers'

urlpatterns = [
    path('', views.answer_list, name='list'),
    path(
        '<int:request_id>/',
        views.add_answer,
        name='add',
    ),
    path(
        'requests/<int:request_id>/edit/',
        views.editAnswer,
        name='edit'
    ),
    path(
        'requests/<int:request_id>/delete/',
        views.deleteAnswer,
        name='delete'
    ),
]
