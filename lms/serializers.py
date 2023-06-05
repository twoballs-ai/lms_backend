from rest_framework import serializers
from . import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseCategory
        fields = ['id','title', 'description']

class CourseSeializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ['id','category','teacher','title','description','course_image','technologicals','course_chapters','related_courses','technological_list']
        depth = 1

class ChapterSeializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chapter
        fields = ['id','course', 'title','description','video','comment']