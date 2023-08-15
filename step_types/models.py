from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

from user.models import Teacher

import lms.models


    
class LessonType(models.Model):
    stage = models.ForeignKey(lms.models.Stage, on_delete=models.CASCADE, related_name='type_lesson')
    


class ClassicLesson(models.Model):
    lesson_type = models.ForeignKey(LessonType, on_delete=models.CASCADE, related_name='classic_lesson_type')
    image = models.FileField(upload_to='images',null=True,blank=True)
    content = models.TextField(null=True,blank=True)
    file = models.FileField(upload_to='files',null=True,blank=True)
    video_link = models.URLField(null=True,blank=True)
    url_link = models.URLField(null=True,blank=True)


class Quiz(models.Model):
    lesson_type = models.ForeignKey(LessonType, on_delete=models.CASCADE, related_name='quiz_lesson_type')

    questions= models.CharField(max_length=150)
    answer1= models.CharField(max_length=150)
    true_answer=models.CharField(max_length=150)




