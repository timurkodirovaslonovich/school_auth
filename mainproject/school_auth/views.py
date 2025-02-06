from django.shortcuts import render
from rest_framework import views, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer


# Create your views here.

@api_view(["GET"])
def student_list(request):

    #get all the students
    students = Student.objects.all()
    #serialize them
    serializer = StudentSerializer(students, many=True)
    #return json
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(["POST"])
def student_create(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data, status=status.HTTP_201_CREATED)