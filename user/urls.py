from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserViewSet
from rest_framework.routers import DefaultRouter

from user import views

# router = DefaultRouter()
# router.register(r'', UserViewSet, basename='user')
# urlpatterns = router.urls
urlpatterns = [
    # path('registration/seller/', SellerRegistrationView.as_view(), name='register-seller'),
    path('teacher-register/', views.TeacherRegistrationView.as_view(), name='register-student'),
    path('popular-teachers/', views.TeacherList.as_view()),
    # path('teacher/<int:pk>/', views.TeacherDetail.as_view()),
    # path('teacher/dashboard/<int:pk>/', views.TeacherDashboard.as_view()),
    # path('teacher/reset-password/<int:teacher_id>/', views.teacher_password_reset),
    # path('teacher-login', views.teacher_login),
    # # для студентов
    path('student-register/', views.StudentRegistrationView.as_view(), name='register-student'),
    path('student/', views.StudentList.as_view()),
    # path('student/<int:pk>/', views.StudentDetail.as_view()),
    # path('student/dashboard/<int:pk>/', views.StudentDashboard.as_view()),
    # path('student/reset-password/<int:student_id>/', views.student_password_reset),
    # path('student-login', views.student_login),
    
]