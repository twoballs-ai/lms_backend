from django.db import models

# Create your models here.
from user.models import Teacher


class CourseCategory(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=1000)

    class Meta:
        verbose_name = 'категория курса'
        verbose_name_plural = 'категории курсов'

    def __str__(self):
        return self.title


class Course(models.Model):
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField(null=True)
    course_image = models.ImageField(upload_to='course_images/', null=True)
    technologicals = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Chapter(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_chapters')
    title = models.CharField(max_length=150)
    description = models.TextField()
    video = models.FileField(upload_to='chapter_videos/', null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Глава'
        verbose_name_plural = 'Главы'

