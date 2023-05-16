from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import TeacherSeializer
from . import models
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions


class TeacherList(generics.ListCreateAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSeializer
    # permission_classes = [permissions.IsAuthenticated]


class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSeializer
    permission_classes = [permissions.IsAuthenticated]
