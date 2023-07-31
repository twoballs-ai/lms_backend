from django.contrib import admin
from . import models
# Register your models here.
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "description",)

admin.site.register(models.CourseCategory, CourseCategoryAdmin)
admin.site.register(models.Course)
admin.site.register(models.Chapter)
admin.site.register(models.Module)
admin.site.register(models.Stage)
admin.site.register(models.Content)
admin.site.register(models.CourseEnroll)
admin.site.register(models.CourseRating)
admin.site.register(models.FavoriteCourse)
admin.site.register(models.TaskForStudentsFromTeacher)

class NotificationAdmin(admin.ModelAdmin):
    list_display=['id','notification_subject', 'notification_for', 'notification_read_status']
    
admin.site.register(models.Notification, NotificationAdmin)
admin.site.register(models.StudyMaterial)