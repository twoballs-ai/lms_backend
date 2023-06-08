from django.db import models
from django.core import serializers
# Create your models here.
from user.models import Student, Teacher


class CourseCategory(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=1000)

    class Meta:
        verbose_name = 'категория курса'
        verbose_name_plural = 'категории курсов'

    def __str__(self):
        return self.title


class Course(models.Model):
    category = models.ForeignKey(CourseCategory,on_delete=models.CASCADE , related_name='category_course')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher_course')
    title = models.CharField(max_length=150)
    description = models.TextField(null=True)
    course_image = models.ImageField(upload_to='course_images/', null=True)
    technologicals = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'

    def related_courses(self):
        related_courses = Course.objects.filter(technologicals__icontains=self.technologicals)
        return serializers.serialize('json',related_courses)
        
    def technological_list(self):
        technological_list=self.technologicals.split(',')
        return technological_list
    
    def total_enrolled_students(self):
        total_enrolled_students= CourseEnroll.objects.filter(course = self).count()
        return total_enrolled_students

    def __str__(self):
        return self.title



class Chapter(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_chapters')
    title = models.CharField(max_length=150)
    description = models.TextField()
    video = models.FileField(upload_to='chapter_videos/', null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Глава'
        verbose_name_plural = 'Главы'

    def __str__(self):
        return self.title
        

class CourseEnroll(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE,related_name='enrolled_courses')
    student = models.ForeignKey(Student, on_delete=models.CASCADE,related_name='enrolled_students')
    enrolled_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Студент подписанный на курс'
        verbose_name_plural = 'Студенты подписанные на курсы'

    def __str__(self):
        return f"{self.course}-{self.student}"   
    

class CourseRating(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='rating_courses')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='rating_students')
    rating = models.PositiveBigIntegerField(default=0)
    review = models.TextField(null=True)
    review_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.course}-{self.student}-{self.rating}"   