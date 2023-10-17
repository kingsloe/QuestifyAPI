from django.urls import path
from . import views

urlpatterns = [
    path('questions_list/', views.questions_list, name='questions-list'),
]