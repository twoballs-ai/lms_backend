from django.shortcuts import render
from . import models
# Create your views here.
from rest_framework import generics

from .serializers import CategorySeializer, CourseSeializer


class CategoryList(generics.ListCreateAPIView):
    queryset = models.CourseCategory.objects.all()
    serializer_class = CategorySeializer


class CourseList(generics.ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = CourseSeializer