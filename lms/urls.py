from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from lms import views

urlpatterns = [
    path('category/', views.CategoryList.as_view()),
    path('course/', views.CourseList.as_view()),
    # path('teacher/', views.TeacherList.as_view()),
    # path('teacher/<int:pk>/', views.TeacherDetail.as_view()),
    # path('teacher-login', views.teacher_login),
]

urlpatterns = format_suffix_patterns(urlpatterns)