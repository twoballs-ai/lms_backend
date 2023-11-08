from rest_framework import serializers
from rest_framework.authtoken.models import Token
from . import models
from dj_rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('id','email', 'password', 'is_student', 'is_teacher')
# StudentSerializer

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True, many=False)
    class Meta:
        model = models.Student
        fields = ('user','user_id','student_image','interested_categories')


class CustomRegisterSerializer(RegisterSerializer):
    is_student = serializers.BooleanField()
    is_teacher = serializers.BooleanField()
    class Meta:
        model = models.CustomUser
        fields = ('email','password', 'is_student', 'is_teacher')

    def get_cleaned_data(self):
        return {
            'password': self.validated_data.get('password', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'is_student': self.validated_data.get('is_student', ''),
            'is_teacher': self.validated_data.get('is_teacher', '')
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.is_student = self.cleaned_data.get('is_student')
        user.is_teacher = self.cleaned_data.get('is_teacher')
        user.save()
        adapter.save_user(request, user, self)
        return user


class StudentCustomRegistrationSerializer(RegisterSerializer):
    student = serializers.PrimaryKeyRelatedField(read_only=True,) #by default allow_null = False
    # student_image = serializers.ImageField(required=True)
    # interested_categories = serializers.CharField(required=True)
    # description = serializers.CharField(required=True)

    def get_cleaned_data(self):
            data = super(StudentCustomRegistrationSerializer, self).get_cleaned_data()
            extra_data = {
                # 'student_image' : self.validated_data.get('student_image', ''),
                # 'interested_categories' : self.validated_data.get('interested_categories', ''),
                # 'description': self.validated_data.get('description', ''),
            }
            data.update(extra_data)
            return data

    def save(self, request):
        user = super(StudentCustomRegistrationSerializer, self).save(request)
        user.is_student = True
        user.save()
        student = models.Student.objects.create(user=user)
        # student = models.Student.objects.create(user=user, student_image=self.cleaned_data.get('student_image'),interested_categories=self.cleaned_data.get('interested_categories'))
        
        student.save()
        return user

    # def save(self, request):
    #     adapter = get_adapter()
    #     user = adapter.new_user(request)
    #     self.cleaned_data = self.get_cleaned_data()
    #     # user.is_student = self.cleaned_data.get('is_student')
    #     user.is_student = True
    #     user.save()
    #     adapter.save_user(request, user, self)
    #     student = models.Student.objects.create(user=user, student_image=self.cleaned_data.get('student_image'),interested_categories=self.cleaned_data.get('interested_categories'))
    #     student.save()
    #     return user

class TeacherCustomRegistrationSerializer(RegisterSerializer):
    teacher = serializers.PrimaryKeyRelatedField(read_only=True,) #by default allow_null = False
    # teacher_image = serializers.ImageField(required=True)
    # skills = serializers.CharField(required=True)
    # qualification = serializers.CharField(required=True)
    
    def get_cleaned_data(self):
            data = super(TeacherCustomRegistrationSerializer, self).get_cleaned_data()
            extra_data = {
                # 'teacher_image' : self.validated_data.get('teacher_image', ''),
                # 'skills' : self.validated_data.get('skills', ''),
                # 'qualification': self.validated_data.get('qualification', ''),
            }
            data.update(extra_data)
            return data

    # def save(self, request):
    #     adapter = get_adapter()
    #     user = adapter.new_user(request)
    #     self.cleaned_data = self.get_cleaned_data()
    #     # user.is_student = self.cleaned_data.get('is_student')
    #     user.is_teacher = True
    #     user.save()
    #     adapter.save_user(request, user, self)
    #     teacher = models.Teacher.objects.create(user=user, teacher_image=self.cleaned_data.get('teacher_image'),
    #                                             interested_categories=self.cleaned_data.get('interested_categories'),
    #                                             qualification=self.cleaned_data.get('qualification'))
    #     teacher.save()
    #     return user


    def save(self, request):
        user = super(TeacherCustomRegistrationSerializer, self).save(request)
        user.is_teacher = True
        user.save()
        teacher = models.Teacher.objects.create(user=user)
        # teacher = models.Teacher.objects.create(user=user, teacher_image=self.cleaned_data.get('teacher_image'),
        #                                         skills=self.cleaned_data.get('skills'),
        #                                         qualification=self.cleaned_data.get('qualification'))        
        teacher.save()
        return user



class TokenSerializer(serializers.ModelSerializer):
    user_type = serializers.SerializerMethodField()

    class Meta:
        model = Token
        fields = ('key', 'user', 'user_type')

    def get_user_type(self, obj):
        serializer_data = UserSerializer(
            obj.user
        ).data
        is_student = serializer_data.get('is_student')
        is_teacher = serializer_data.get('is_teacher')
        return {
            'is_student': is_student,
            'is_teacher': is_teacher
        }
class TeacherSerializer(serializers.ModelSerializer):
    # user = UserSerializer(required=True, many=False)
    class Meta:
        model = models.Teacher
        fields = [ 'qualification',  'skills','teacher_course','skill_list','teacher_image', 'total_teacher_courses']
        # fields = ['user','full_name','email', 'password', 'qualification', 'phone', 'skills','teacher_course','skill_list','teacher_image', 'total_teacher_courses']

    def __init__(self, *args, **kwargs):
        super(TeacherSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 1

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.CustomUser
#         fields = ['id','first_name','last_name','email', 'password','is_student', 'is_teacher']

#         extra_kwargs = {
#             'password' :{'write_only':True}  #  to does not return password in api ## postman
#         }


    # def __init__(self, *args, **kwargs):
    #     super(TeacherSerializer, self).__init__(*args, **kwargs)
    #     request = self.context.get('request')
    #     self.Meta.depth = 0
    #     if request and request.method == 'GET':
    #         self.Meta.depth = 1

# class TeacherDashboardSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Teacher
#         fields = ['total_teacher_courses','total_teacher_chapters','total_teacher_students']


# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Student
#         fields = ['id','full_name','email', 'password', 'username', 'interested_categories','student_image']

#     def __init__(self, *args, **kwargs):
#         super(StudentSerializer, self).__init__(*args, **kwargs)
#         request = self.context.get('request')
#         self.Meta.depth = 0
#         if request and request.method == 'GET':
#             self.Meta.depth = 1


# class StudentDashboardSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Student
#         fields = ['total_student_enroll_courses','total_student_score','total_student_energy','total_favorite_courses','total_completed_tasks', 'total_pending_tasks']