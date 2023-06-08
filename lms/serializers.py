from rest_framework import serializers
from . import models


class CategorySerializer(serializers.ModelSerializer):
    # categories = serializers.StringRelatedField(many=True)
    # category_course = serializers.StringRelatedField(many=True)

    class Meta:
        model = models.CourseCategory
        fields = ['id','title', 'description']

class CourseSerializer(serializers.ModelSerializer):
    # category_name = serializers.RelatedField(source='category', read_only=True)
    # category = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # category = serializers.StringRelatedField(many=True)
    class Meta:
        model = models.Course
        fields = ['id','category','teacher','title','description','course_image','technologicals','course_chapters','related_courses','technological_list','total_enrolled_students']
        # depth = 1

    def __init__(self, *args, **kwargs):
        super(CourseSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 1

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chapter
        fields = ['id','course', 'title','description','video','comment']


class CourseEnrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseEnroll
        fields = ['id','course', 'student', 'enrolled_time']   
        # depth = 1

    def __init__(self, *args, **kwargs):
        super(CourseEnrollSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 1


class CourseRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseRating
        fields = ['id','course', 'student', 'rating','review','review_time']

        def __init__(self, *args, **kwargs):
            super(CourseRatingSerializer, self).__init__(*args, **kwargs)
            request = self.context.get('request')
            self.Meta.depth = 0
            if request and request.method == 'GET':
                self.Meta.depth = 1