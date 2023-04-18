from django.db import models


class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.TextField()

    class Meta:
        verbose_name = 'учитель'
        verbose_name_plural = 'учителя'


class Student(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.TextField()
    interested_categories = models.TextField()

    class Meta:
        verbose_name = 'ученик'
        verbose_name_plural = 'ученики'