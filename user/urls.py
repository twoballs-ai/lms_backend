from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from user import views

urlpatterns = [
    path('teacher/', views.TeacherList.as_view()),
    path('teacher/<int:pk>/', views.TeacherDetail.as_view()),
    path('teacher-login', views.teacher_login),
    # для студентов
    path('student/', views.StudentList.as_view()),
    path('student-login', views.student_login),
]

urlpatterns = format_suffix_patterns(urlpatterns)