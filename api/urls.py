from django.urls import path
from .views import *

urlpatterns = [
    path('questions_list/', questions_list, name='questions-list'),
]