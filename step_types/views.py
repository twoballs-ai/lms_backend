from django.shortcuts import render

from step_types.serializers import ClassicLessonSerializer, QuizLessonSerializer
from . import models
from django.db.models import Q
# Create your views here.
from rest_framework import generics
from django.http import JsonResponse, HttpResponse

from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
import lms.models


class ClassicLessonList(generics.ListCreateAPIView):
    serializer_class = ClassicLessonSerializer

    def get_queryset(self):
        stage_id = self.kwargs['stage_id']
        stage = lms.models.Stage.objects.get(pk=stage_id)
        return models.ClassicLesson.objects.filter(stage=stage)
    

class QuizLessonList(generics.ListCreateAPIView):
    serializer_class = QuizLessonSerializer

    def get_queryset(self):
        stage_id = self.kwargs['stage_id']
        stage = lms.models.Stage.objects.get(pk=stage_id)
        return models.Quiz.objects.filter(stage=stage)