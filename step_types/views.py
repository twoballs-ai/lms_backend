from django.shortcuts import render

from step_types.serializers import ClassicLessonSerializer
from . import models
from django.db.models import Q
# Create your views here.
from rest_framework import generics
from django.http import JsonResponse, HttpResponse

from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination



class ClassicLessonList(generics.ListCreateAPIView):
    queryset = models.ClassicLesson.objects.all()
    serializer_class = ClassicLessonSerializer
