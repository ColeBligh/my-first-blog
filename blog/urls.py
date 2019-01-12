from django.urls import path
from . import views

urkpatterns = [
    path('', views.post_list, name='post_list'),
]
