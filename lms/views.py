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

    def get_queryset(self):
        qs=super().get_queryset()
        if 'result' in self.request.GET:
            limit= int(self.request.GET['result'])
            qs = models.Course.objects.all().order_by('-id')[:limit]
        if 'category' in self.request.GET:
            category = self.request.GET['category']
            qs = models.Course.objects.filter(technologicals__icontains=category)
        if 'skill_name' in self.request.GET and 'teacher' in self.request.GET:
           'skill_name' in self.request.GET['skill_name']
           'teacher' in self.request.GET['teacher']
           teacher = models.Teacher.objects.filter(id=skill_name).first
           qs = models.Course.objects.filter(technologicals__icontains=skill_name, teacher=teacher)
        return qs
    

class CourseDetailView(generics.RetrieveAPIView):
    queryset = models.Course.objects.all()
    serializer_class = CourseSeializer


class TeacherCourseList(generics.ListCreateAPIView):
    serializer_class = CourseSeializer

    def get_queryset(self):
        teacher_id = self.kwargs['teacher_id']
        teacher = models.Teacher.objects.get(pk=teacher_id)
        return models.Course.objects.filter(teacher=teacher)


class TeacherCourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Course.objects.all()
    serializer_class = CourseSeializer


class CourseChapterList(generics.ListCreateAPIView):
    serializer_class = ChapterSeializer

    def get_queryset(self):
        course_id = self.kwargs['course_id']
        course = models.Course.objects.get(pk=course_id)
        return models.Chapter.objects.filter(course=course)


class ChapterDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Chapter.objects.all()
    serializer_class = ChapterSeializer