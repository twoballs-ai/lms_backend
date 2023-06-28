from django.shortcuts import render
from . import models
from django.db.models import Q
# Create your views here.
from rest_framework import generics
from django.http import JsonResponse, HttpResponse
from .serializers import QuizSerializer


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
