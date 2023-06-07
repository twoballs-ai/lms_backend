from rest_framework import serializers
from . import models


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = ['id','full_name', 'detail','email', 'password', 'qualification', 'phone', 'skills','teacher_course','skill_list']
        depth=1


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ['id','full_name','email', 'password', 'username', 'interested_categories']
        depth=1
