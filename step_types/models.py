from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

from user.models import Teacher

import lms.models


    
class LessonType(models.Model):
    stage = models.OneToOneField(lms.models.Stage, on_delete=models.CASCADE, related_name='type_lesson')
    


class ClassicLesson(LessonType):
    is_classic = models.BooleanField(default=True)
    content = models.JSONField(null=True, blank=True, default=dict)



class Quiz(LessonType):
    is_quiz = models.BooleanField(default=True)
    questions= models.CharField(max_length=150)
    answer1= models.CharField(max_length=150)
    answer2= models.CharField(max_length=150)
    answer3= models.CharField(max_length=150)
    answer4= models.CharField(max_length=150)
    true_answer=models.CharField(max_length=150)


class Video(LessonType):
    is_video = models.BooleanField(default=True)
    video_lesson= models.URLField()
    description= models.CharField(max_length=150)


