from rest_framework import serializers
from . import models


class ClassicLessonSerializer(serializers.ModelSerializer):
    # categories = serializers.StringRelatedField(many=True)
    # category_course = serializers.StringRelatedField(many=True)

    class Meta:
        model = models.ClassicLesson
        fields = ['id','stage', 'image','content','file','video_link','url_link']