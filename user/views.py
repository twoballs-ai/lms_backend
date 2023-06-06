from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import TeacherSerializer, StudentSerializer
from . import models
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt


class TeacherList(generics.ListCreateAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializer
    # permission_classes = [permissions.IsAuthenticated]


class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializer
    # permission_classes = [permissions.IsAuthenticated]

@csrf_exempt
def teacher_login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    try:
        teacher_data = models.Teacher.objects.get(email=email,password=password)
    except models.Teacher.DoesNotExist:
        teacher_data= None
    if teacher_data:
        return JsonResponse({'bool': True, 'teacher_id': teacher_data.id})
    else:
        return JsonResponse({'bool': False})


# students
class StudentList(generics.ListCreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer
    # permission_classes = [permissions.IsAuthenticated]


@csrf_exempt
def student_login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    try:
        student_data = models.Student.objects.get(email=email,password=password)
    except models.Student.DoesNotExist:
        student_data= None
    if student_data:
        return JsonResponse({'bool': True, 'student_id': student_data.id})
    else:
        return JsonResponse({'bool': False})