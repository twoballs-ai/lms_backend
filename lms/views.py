from django.shortcuts import render
from . import models
# Create your views here.
from rest_framework import generics

from .serializers import CategorySeializer, CourseSeializer, ChapterSeializer


class CategoryList(generics.ListCreateAPIView):
    queryset = models.CourseCategory.objects.all()
    serializer_class = CategorySeializer


class CourseList(generics.ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = CourseSeializer


class TeacherCourseList(generics.ListAPIView):
    serializer_class = CourseSeializer

    def get_queryset(self):
        teacher_id = self.kwargs['teacher_id']
        teacher = models.Teacher.objects.get(pk=teacher_id)
        return models.Course.objects.filter(teacher=teacher)


class ChapterList(generics.ListCreateAPIView):
    queryset = models.Chapter.objects.all()
    serializer_class = ChapterSeializer
