from django.shortcuts import render
from . import models
from django.db.models import Q
# Create your views here.
from rest_framework import generics
from django.http import JsonResponse, HttpResponse
from .serializers import CourseQuizSerializer, QuizQuestionSerializer, QuizSerializer


# Create your views here.
class QuizList(generics.ListCreateAPIView):
    queryset = models.Quiz.objects.all()
    serializer_class = QuizSerializer


class TeacherQuizList(generics.ListCreateAPIView):
    serializer_class = QuizSerializer

    def get_queryset(self):
        teacher_id = self.kwargs['teacher_id']
        teacher = models.Teacher.objects.get(pk=teacher_id)
        return models.Quiz.objects.filter(teacher=teacher)
    

class TeacherQuizDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Quiz.objects.all()
    serializer_class = QuizSerializer


class QuizDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Quiz.objects.all()
    serializer_class = QuizSerializer


class QuizQuestionList(generics.ListCreateAPIView):
    serializer_class = QuizQuestionSerializer

    def get_queryset(self):
        quiz_id = self.kwargs['quiz_id']
        quiz = models.Quiz.objects.get(pk=quiz_id)
        return models.QuizQuestion.objects.filter(quiz=quiz)
    

class CourseQuizList(generics.ListCreateAPIView):
    queryset = models.CourseQuiz.objects.all()
    serializer_class = CourseQuizSerializer    


def get_quiz_assign_status(request, quiz_id, course_id):
    quiz = models.Quiz.objects.filter(id = quiz_id).first()
    course = models.Course.objects.filter(id = course_id).first()
    assign_status = models.CourseQuiz.objects.filter(course=course,quiz=quiz).count()
    if assign_status:
        return JsonResponse({'bool': True})
    else:
        return JsonResponse({'bool': False})