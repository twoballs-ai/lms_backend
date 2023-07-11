from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.CourseCategory)
admin.site.register(models.Course)
admin.site.register(models.Chapter)
admin.site.register(models.CourseEnroll)
admin.site.register(models.CourseRating)
admin.site.register(models.FavoriteCourse)
admin.site.register(models.TaskForStudentsFromTeacher)

class NotificationAdmin(admin.ModelAdmin):
    list_display=['id','notification_subject', 'notification_for', 'notification_read_status']
    
admin.site.register(models.Notification, NotificationAdmin)
admin.site.register(models.StudyMaterial)