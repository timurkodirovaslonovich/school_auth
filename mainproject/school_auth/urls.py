from django.urls import path
from .views import *

urlpatterns = [
    path('students/', student_list),
    path('studentadd/', student_create),
    path('teachers/', teacher_list),
    path('teacheradd/', teacher_create),
]