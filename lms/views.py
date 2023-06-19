from django.shortcuts import render
from . import models
from django.db.models import Q
# Create your views here.
from rest_framework import generics
from django.http import JsonResponse, HttpResponse
from .serializers import CategorySerializer, CourseEnrollSerializer, \
    CourseSerializer, ChapterSerializer, CourseRatingSerializer, NotificationSerializer, StudentFavoriteCourseSerializer, TaskForStudentsSerializer


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
        # разобратьсЯ в работе этой функции
        elif 'student_id' in self.kwargs:
            student_id = self.kwargs['student_id']
            student = models.Student.objects.get(pk=student_id)
            queries=[Q(technologicals__iendswiith=value) for value in student.interested_categories]
            query = queries.pop()
            for item in queries:
                query |= item
            return models.Course.objects.filter(query)
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
        if 'course_id' in self.kwargs:
            course_id = self.kwargs['course_id']
            course = models.Course.objects.get(pk=course_id)
            return models.CourseEnroll.objects.filter(course=course)
        elif 'teacher_id' in self.kwargs:
            teacher_id = self.kwargs['teacher_id']
            teacher = models.Teacher.objects.get(pk=teacher_id)
            return models.CourseEnroll.objects.filter(course__teacher= teacher).distinct()
        elif 'student_id' in self.kwargs:
            student_id = self.kwargs['student_id']
            student = models.Student.objects.get(pk=student_id)
            return models.CourseEnroll.objects.filter(student= student).distinct()
        # return models.CourseEnroll.objects.filter(course__teacher= teacher).distinct('id') проверить на посгрес


class CourseRatingList(generics.ListCreateAPIView):
    queryset = models.CourseRating.objects.all()
    serializer_class = CourseRatingSerializer

    # def get_queryset(self):
    #     course_id = self.kwargs['course_id']
    #     course = models.Course.objects.get(pk=course_id)
    #     return models.CourseRating.objects.filter(course=course)

def rating_course_status(request, student_id, course_id):
    student = models.Student.objects.filter(id = student_id).first()
    course = models.Course.objects.filter(id = course_id).first()
    rating_status = models.CourseRating.objects.filter(course=course,student=student).count()
    if rating_status:
        return JsonResponse({'bool': True})
    else:
        return JsonResponse({'bool': False})
    
class StudentFavoriteCourse(generics.ListCreateAPIView):
    queryset = models.FavoriteCourse.objects.all()
    serializer_class = StudentFavoriteCourseSerializer

    def get_queryset(self):
        if 'student_id' in self.kwargs:
            student_id = self.kwargs['student_id']
            student = models.Student.objects.get(pk=student_id)
            return models.FavoriteCourse.objects.filter(student= student).distinct()  
 
 

def get_favorite_status(request, student_id, course_id):
    student = models.Student.objects.filter(id = student_id).first()
    course = models.Course.objects.filter(id = course_id).first()
    favorite_status = models.FavoriteCourse.objects.filter(course=course,student=student).first()
    if favorite_status:
        return JsonResponse({'bool': True})
    else:
        return JsonResponse({'bool': False})
    
def remove_favorite_status(request, student_id, course_id):
    student = models.Student.objects.filter(id = student_id).first()
    course = models.Course.objects.filter(id = course_id).first()
    favorite_status = models.FavoriteCourse.objects.filter(course=course,student=student).delete()
    if favorite_status:
        return JsonResponse({'bool': True})
    else:
        return JsonResponse({'bool': False})
    

class TaskForStudentList(generics.ListCreateAPIView):
    queryset = models.TaskForStudentsFromTeacher.objects.all()
    serializer_class = TaskForStudentsSerializer

    def get_queryset(self):
        teacher_id = self.kwargs['teacher_id']
        teacher = models.Teacher.objects.get(pk=teacher_id)
        return models.TaskForStudentsFromTeacher.objects.filter(teacher=teacher)
     

class StudentUpcomingTask(generics.ListCreateAPIView):
    queryset = models.TaskForStudentsFromTeacher.objects.all()
    serializer_class = TaskForStudentsSerializer

    def get_queryset(self):
        student_id = self.kwargs['student_id']
        student = models.Student.objects.get(pk=student_id)
        models.Notification.objects.filter(student=student, notification_for='student', notification_subject= 'task').update(notification_read_status=True)
        return models.TaskForStudentsFromTeacher.objects.filter(student=student)
    

class UpdateTask(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.TaskForStudentsFromTeacher.objects.all()
    serializer_class = TaskForStudentsSerializer


class NotificationList(generics.ListCreateAPIView):
    queryset = models.Notification.objects.all()
    serializer_class = NotificationSerializer

    def get_queryset(self):
        student_id = self.kwargs['student_id']
        student = models.Student.objects.get(pk=student_id)
        return models.Notification.objects.filter(student=student, notification_for='student', notification_subject= 'task', notification_read_status=False)
    