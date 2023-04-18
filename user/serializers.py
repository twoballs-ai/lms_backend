from rest_framework import serializers
from . import models


class TeacherSeializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = ['id','full_name', 'email', 'password', 'qualification', 'phone', 'address']
