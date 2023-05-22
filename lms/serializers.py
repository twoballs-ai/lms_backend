from rest_framework import serializers
from . import models


class CategorySeializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseCategory
        fields = ['id','title', 'description']

class CourseSeializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ['category','teacher','title','description','course_image','technologicals']