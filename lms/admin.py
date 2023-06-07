from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.CourseCategory)
admin.site.register(models.Course)
admin.site.register(models.Chapter)
admin.site.register(models.CourseEnroll)
admin.site.register(models.CourseRating)