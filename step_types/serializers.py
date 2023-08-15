from rest_framework import serializers
from . import models



# class LessonTypeSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = models.LessonType
#         # fields = "__all__"
#         fields = ['stage']

#     def __init__(self, *args, **kwargs):
#         super(LessonTypeSerializer, self).__init__(*args, **kwargs)
#         request = self.context.get('request')
#         self.Meta.depth = 0
#         if request and request.method == 'GET':
#             self.Meta.depth = 1

    

class ClassicLessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ClassicLesson
        # fields = "__all__"
        fields = ['id','image','content','file','video_link','url_link','stage']


class QuizLessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Quiz
        # fields = "__all__"
        fields = ['id','questions','answer1','true_answer']