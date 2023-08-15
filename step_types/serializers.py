from rest_framework import serializers
from . import models


class TypeLessonSerializer(serializers.Serializer):
    # Need to re-declare fields since this is not a ModelSerializer

    class Meta:
        fields = ['id','stage']


class ClassicLessonSerializer(TypeLessonSerializer,  serializers.ModelSerializer):


    class Meta:
        model = models.ClassicLesson
        # fields = "__all__"
        fields =TypeLessonSerializer.Meta.fields + ['id','image','content','file','video_link','url_link']

