from django.db import models

import lms.models


class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    teacher_image = models.ImageField(upload_to='teacher_profile_images/', null=True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100, blank=True)
    qualification = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    skills = models.TextField()

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'учитель'
        verbose_name_plural = 'учителя'

    def skill_list(self):
        skill_list=self.skills.split(',')
        return skill_list        

    def total_teacher_courses(self):
        total_courses= lms.models.Course.objects.filter(teacher = self).count()
        return total_courses
    
    def total_teacher_chapters(self):
        total_chapters= lms.models.Chapter.objects.filter(course__teacher= self).count()
        return total_chapters

    def total_teacher_students(self):
        total_students= lms.models.CourseEnroll.objects.filter(course__teacher = self).count()
        return total_students
    

class Student(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    interested_categories = models.TextField()

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'ученик'
        verbose_name_plural = 'ученики'