from django.shortcuts import render
from . import models
# Create your views here.
from rest_framework import generics
from django.http import JsonResponse, HttpResponse
from .serializers import CategorySerializer, CourseEnrollSerializer, CourseSerializer, ChapterSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = models.CourseCategory.objects.all()
    serializer_class = CategorySerializer


class CourseList(generics.ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        qs=super().get_queryset()
        if 'result' in self.request.GET:
            limit= int(self.request.GET['result'])
            qs = models.Course.objects.all().order_by('-id')[:limit]
        if 'category' in self.request.GET:
            category = self.request.GET['category']
            qs = models.Course.objects.filter(technologicals__icontains=category)
        if 'skill_slug' in self.request.GET and 'teacher' in self.request.GET:
           skill_slug = self.request.GET['skill_slug']
           teacher = self.request.GET['teacher']
           teacher = models.Teacher.objects.filter(id=teacher).first()
           qs = models.Course.objects.filter(technologicals__icontains=skill_slug,teacher=teacher)
        return qs
    

class CourseDetailView(generics.RetrieveAPIView):
    queryset = models.Course.objects.all()
    serializer_class = CourseSerializer


class TeacherCourseList(generics.ListCreateAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        teacher_id = self.kwargs['teacher_id']
        teacher = models.Teacher.objects.get(pk=teacher_id)
        return models.Course.objects.filter(teacher=teacher)


class TeacherCourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Course.objects.all()
    serializer_class = CourseSerializer


class CourseChapterList(generics.ListCreateAPIView):
    serializer_class = ChapterSerializer

    def get_queryset(self):
        course_id = self.kwargs['course_id']
        course = models.Course.objects.get(pk=course_id)
        return models.Chapter.objects.filter(course=course)


class ChapterDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Chapter.objects.all()
    serializer_class = ChapterSerializer


# список всех подписок на курсы.
class StudenEnrollList(generics.ListCreateAPIView):
    queryset = models.CourseEnroll.objects.all()
    serializer_class = CourseEnrollSerializer    


def enroll_course_status(request, student_id, course_id):
    student = models.Student.objects.filter(id = student_id).first()
    course = models.Course.objects.filter(id = course_id).first()
    enroll_status = models.CourseEnroll.objects.filter(course=course,student=student).count()
    if enroll_status:
        return JsonResponse({'bool': True})
    else:
        return JsonResponse({'bool': False})
    

# список подписанных людей на нужные курсы.
class EnrolledUsersByCourse(generics.ListAPIView):
    queryset = models.CourseEnroll.objects.all()
    serializer_class = CourseEnrollSerializer    
    
    def get_queryset(self):
        course_id = self.kwargs['course_id']
        course = models.Course.objects.get(pk=course_id)
        return models.CourseEnroll.objects.filter(course=course)