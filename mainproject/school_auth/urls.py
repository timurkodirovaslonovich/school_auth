from django.urls import path
from .views import *
from rest_framework_simplejwt import views
urlpatterns = [
    path('students/', student_list),
    path('studentadd/', student_create),
    path('teachers/', teacher_list),
    path('teacheradd/', teacher_create),
    path('login/', login),
    #Authentication
    path('toke/', views.TokenObtainPairView.as_view()),
    path('token/refresh/', views.TokenRefreshView.as_view()),
]