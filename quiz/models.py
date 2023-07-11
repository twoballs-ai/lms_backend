from django.db import models
from django.core import serializers
from user.models import Student, Teacher
import lms.models
from lms.models import Course
# Create your models here.
class Quiz(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    title= models.CharField(max_length=150)
    detail=  models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)

    # def assign_status(self):

    #     return CourseQuiz.objects.filter(quiz = self).count()

    class Meta:
        verbose_name = 'Квиз'
        verbose_name_plural = 'Квизы'


class QuizQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True)
    questions= models.CharField(max_length=150)
    answer1= models.CharField(max_length=150)
    answer2= models.CharField(max_length=150)
    answer3= models.CharField(max_length=150)
    answer4= models.CharField(max_length=150)
    true_answer=models.CharField(max_length=150)
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Вопрос для квиза'
        verbose_name_plural = 'Вопросы для квиза'


class CourseQuiz(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(lms.models.Course, on_delete=models.CASCADE, null=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True)
    # notification_text= models.TextField(verbose_name='Notification Text')
    add_time = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        verbose_name = 'Квиз для курса'
        verbose_name_plural = 'Квизы  для курса'