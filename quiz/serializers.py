from rest_framework import serializers
from . import models


class QuizSerializer(serializers.ModelSerializer):
    # category_name = serializers.RelatedField(source='category', read_only=True)
    # category = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # category = serializers.StringRelatedField(many=True)
    class Meta:
        model = models.Quiz
        fields = ['id','teacher','title','detail', 'assign_status', 'add_time']
        # depth = 1

    def __init__(self, *args, **kwargs):
        super(QuizSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 2


class QuizQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QuizQuestion
        fields = ['id','quiz', 'questions','answer1','answer2','answer3','answer4','true_answer','add_time']

    def __init__(self, *args, **kwargs):
        super(QuizQuestionSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 2