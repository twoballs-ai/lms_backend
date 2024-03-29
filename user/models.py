from .managers import CustomUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
import lms.models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

# User = settings.AUTH_USER_MODEL

# class Role(models.Model):
#   STUDENT = 1
#   TEACHER = 2
#   MANAGER = 3
#   ROLE_CHOICES = (
#       (STUDENT, 'student'),
#       (TEACHER, 'teacher'),
#       (MANAGER, 'manager'),
#   )

#   id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

#   def __str__(self):
#       return self.get_id_display()



class CustomUser(AbstractUser):
    # roles = models.ManyToManyField(Role)

    username = None
    email = models.EmailField(_("email address"), unique=True)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    # is_company = models.BooleanField(default=False) #в будущем добавим возможность

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True, related_name='teachers')
    teacher_image = models.ImageField(upload_to='teacher_profile_images/', blank=True, null=True)
    qualification = models.CharField(max_length=100, blank=True, null=True)
    skills = models.TextField(blank=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'учитель'
        verbose_name_plural = 'учителя'
        permissions = (("sample_permission", "can change sth of sth"),)

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
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True, related_name='students')   
    student_image = models.ImageField(upload_to='student_profile_images/', blank=True, null=True)
    interested_categories = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'ученик'
        verbose_name_plural = 'ученики'
        permissions = (("sample_permission", "can change sth in sth"),)

    def total_student_score(self):
        student_score= lms.models.TotalStudentScore.objects.get_or_create(student=self)[0]
        student_score = student_score.total_student_score
        return student_score
    
    def total_student_energy(self):
        student_energy= lms.models.TotalStudentEnergy.objects.get_or_create(student=self)[0]
        print(student_energy)
        student_energy = student_energy.total_student_energy
        print(student_energy)
        return student_energy

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
    
    
    

class Manager(CustomUser):
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True, related_name='students')   
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True, related_name='managers')
    sample_field_name = models.CharField(max_length = 50, blank = True, null = True)

    class Meta:
        permissions = (("sample_permission", "can change sth in sth"),)