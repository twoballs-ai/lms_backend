from django.db import models

# Create your models here.
from user.models import Teacher


class CourseCategory(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=1000)

    class Meta:
        verbose_name = 'категория курса'
        verbose_name_plural = 'категории курсов'


class Course(models.Model):
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'
