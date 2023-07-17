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
    verify_status = models.BooleanField(default=False)
    otp_digit = models.CharField(max_length=10, null=True)

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
    student_image = models.ImageField(upload_to='student_profile_images/', null=True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100,blank=True)
    username = models.CharField(max_length=100)
    interested_categories = models.TextField()
    verify_status = models.BooleanField(default=False)
    otp_digit = models.CharField(max_length=10, null=True)
    
    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'ученик'
        verbose_name_plural = 'ученики'

    def total_student_enroll_courses(self):
        enrolled_courses= lms.models.CourseEnroll.objects.filter(student = self).count()
        return enrolled_courses
    
    def total_favorite_courses(self):
        favorite_course= lms.models.FavoriteCourse.objects.filter(student= self).count()
        return favorite_course
    
    def total_completed_tasks(self):
        completed_task= lms.models.TaskForStudentsFromTeacher.objects.filter(student = self, complete_status=True).count()
        return completed_task    

    def total_pending_tasks(self):
        pending_task= lms.models.TaskForStudentsFromTeacher.objects.filter(student = self, complete_status=False).count()
        return pending_task    
    
    
    