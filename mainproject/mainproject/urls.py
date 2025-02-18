from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('school_auth.urls')),
    path('api/v1/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
