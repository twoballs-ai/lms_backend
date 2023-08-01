from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

from lms.models import Stage
from user.models import Teacher
from lms.models import Stage


class LessonType(models.Model):
    # stage = models.OneToOneField(Stage, on_delete=models.CASCADE)
    pass
    
    


class ClassicLesson(LessonType):
    place_ptr = models.ForeignKey(
    LessonType, on_delete=models.CASCADE, related_name='plas'
)
    # stage = models.OneToOneField(Stage, on_delete=models.CASCADE)
    image = models.FileField(upload_to='images',null=True,blank=True)
    content = models.TextField(null=True,blank=True)
    file = models.FileField(upload_to='files',null=True,blank=True)
    video_link = models.URLField(null=True,blank=True)
    url_link = models.URLField(null=True,blank=True)


class Quiz(LessonType):
    # stage = models.OneToOneField(Stage, on_delete = models.CASCADE)
    questions= models.CharField(max_length=150)
    answer1= models.CharField(max_length=150)
    true_answer=models.CharField(max_length=150)




