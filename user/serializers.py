from rest_framework import serializers
from . import models


class TeacherSeializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = ['id','full_name', 'detail','email', 'password', 'qualification', 'phone', 'skills','teacher_courses']
        depth=1
