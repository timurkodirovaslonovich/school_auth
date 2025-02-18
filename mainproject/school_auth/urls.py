from django.urls import path
from .views import *


urlpatterns = [
    path('students/', student_list),
    path('teachers/', teacher_list),
    path('login/', login),
    path('register/', register_user),
    path('token/', CustomTokenObtainPairView.as_view())
]