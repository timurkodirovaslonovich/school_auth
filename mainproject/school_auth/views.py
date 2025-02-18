from django.shortcuts import render, redirect
from rest_framework import views, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .permissions import *
from .models import CustomUser
from .serializers import CustomUserSerializer


# Create your views here.


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






@api_view(["POST"])
@permission_classes([IsAuthenticated, IsSuperUser])
def student_create(request):

    data = request.data
    data['role'] = 'student'
    serializer = CustomUserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
    return redirect('http://127.0.0.1:8000/api/v1/students/')



@api_view(["POST"])
@permission_classes([IsAuthenticated, IsSuperUser])
def teacher_create(request):
    data = request.data
    data['role'] = 'teacher'
    serializer = CustomUserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()

    return redirect('http://127.0.0.1:8000/api/v1/teachers/')




