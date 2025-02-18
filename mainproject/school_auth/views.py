from django.shortcuts import render, redirect
from rest_framework import views, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from .permissions import *
from .models import CustomUser
from .serializers import CustomUserSerializer, CustomTokenObtainPairSerializer


# Create your views here.

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_data = CustomTokenObtainPairSerializer


@api_view(['POST'])
def register_user(request):
    username = request.data['username']
    password = request.data['password']
    email = request.data['email']
    role = request.data['role']

    if not username or not password or not email or not role:
        return Response({'message': 'Missing username or password.'}, status=status.HTTP_400_BAD_REQUEST)

    if CustomUser.objects.filter(username=username).exists():
        return Response({'message': 'Username already exists.'}, status=status.HTTP_400_BAD_REQUEST)

    user = CustomUser.objects.create_user(username, email, password)
    user.role = role
    user.save()
    refresh = RefreshToken.for_user(user)

    return Response({'token': str(refresh.access_token)})




@api_view(["POST"])
def login(request):
    username = request.data['username']
    password = request.data["password"]

    user = CustomUser.objects.filter(username=username)[0]
    if user and user.check_password(password):
        if user.role == 'teacher':
            return redirect('http://127.0.0.1:8000/api/v1/teachers/')
        elif user.role == 'student':
            return redirect('http://127.0.0.1:8000/api/v1/students/')




@api_view(["GET"])
@permission_classes([IsAuthenticated, IsTeacherOrSuperUser])
def student_list(request):
    students = CustomUser.objects.filter(role = 'student').all()

    serializer = CustomUserSerializer(students, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated, IsTeacherOrSuperUser])
def teacher_list(request):
    teachers = CustomUser.objects.filter(role = 'teacher').all()
    serializer = CustomUserSerializer(teachers, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)















