from django.db import models


class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    teacher_image = models.ImageField(upload_to='teacher_profile_images/', null=True)
    detail = models.TextField(null=True,blank=True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
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