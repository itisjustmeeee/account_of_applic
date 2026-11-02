from django.urls import path
from . import views

appp_name = 'users'

urlpatterns = [
    path('', views.index, name='list'),
    path(
        '<int:user_id>/',
        views.user_detail,
        name='detail'
    ),
]
