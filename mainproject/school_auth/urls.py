from django.urls import path
from .views import *

urlpatterns = [
    path('students/', student_list),
    path('add/', student_create)
]