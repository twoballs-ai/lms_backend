from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from lms import views

urlpatterns = [
    # получение и добавление категорий
    path('category/', views.CategoryList.as_view()),
    # росмотр всех курсов и добавление курса
    path('course/', views.CourseList.as_view()),
    # просмотр курса по айди:
    path('course/<int:pk>', views.CourseDetailView.as_view()),
    # добавление глав
    path('chapter/<int:pk>', views.ChapterDetailView.as_view()),
    path('course-chapter/<int:course_id>', views.CourseChapterList.as_view()),
    path('teacher-courses/<int:teacher_id>', views.TeacherCourseList.as_view()),
    path('teacher-courses-detail/<int:pk>', views.TeacherCourseDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)