from rest_framework import serializers
from . import models


class CategorySerializer(serializers.ModelSerializer):
    # categories = serializers.StringRelatedField(many=True)
    # category_course = serializers.StringRelatedField(many=True)

    class Meta:
        model = models.CourseCategory
        fields = ['id','title', 'description','total_courses']

class CourseSerializer(serializers.ModelSerializer):
    # category_name = serializers.RelatedField(source='category', read_only=True)
    # category = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # category = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = models.Course
        fields = ['id','category','teacher','title','description','course_image','technologicals','course_chapters','related_courses','technological_list','total_enrolled_students', 'course_rating','course_views']
        # depth = 1

    def __init__(self, *args, **kwargs):
        super(CourseSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 2

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chapter
        fields = ['id','course', 'title','description', 'chapter_modules']

    def __init__(self, *args, **kwargs):
        super(ChapterSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 1


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Module
        fields = ['id','title', 'chapter','description','stage_modules']

    def __init__(self, *args, **kwargs):
        super(ModuleSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 1

class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Stage
        fields = ['id','title', 'module','description']

    def __init__(self, *args, **kwargs):
        super(StageSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 1

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
            self.Meta.depth = 2

class StudentFavoriteCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FavoriteCourse
        fields = ['id','course', 'student', 'is_favorite']   
        # depth = 1

    def __init__(self, *args, **kwargs):
        super(StudentFavoriteCourseSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 2            


class CourseRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseRating
        fields = ['id','course', 'student', 'rating', 'review', 'review_time']   
        # depth = 1

    def __init__(self, *args, **kwargs):
        super(CourseRatingSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 2   
    
class TaskForStudentsSerializer(serializers.ModelSerializer):
    # category_name = serializers.RelatedField(source='category', read_only=True)
    # category = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # category = serializers.StringRelatedField(many=True)
    class Meta:
        model = models.TaskForStudentsFromTeacher
        fields = ['id','teacher','student','complete_status','title','detail','add_time']
        # depth = 1

    def __init__(self, *args, **kwargs):
        super(TaskForStudentsSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 2



class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Notification
        fields = ['teacher','student','notification_subject', 'notification_for']

    def __init__(self, *args, **kwargs):
        super(NotificationSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 2    


class StudyMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudyMaterial
        fields = ['id','course', 'title','description','upload','comment']


