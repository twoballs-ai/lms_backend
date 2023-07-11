from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from lms import views

urlpatterns = [
    # получение и добавление категорий
    path('category/', views.CategoryList.as_view()),
    # росмотр всех курсов и добавление курса
    path('course/', views.CourseList.as_view()),
    path('popular-courses/', views.CourseRatingList.as_view()),
    path('search-by-course/<str:search_string>', views.CourseList.as_view()),
    # просмотр курса по айди:
    path('course/<int:pk>', views.CourseDetailView.as_view()),
    # добавление глав
    path('chapter/<int:pk>', views.ChapterDetailView.as_view()),
    path('course-chapter/<int:course_id>', views.CourseChapterList.as_view()),
    path('teacher-courses/<int:teacher_id>', views.TeacherCourseList.as_view()),
    path('teacher-courses-detail/<int:pk>', views.TeacherCourseDetail.as_view()),
    path('student-course-enroll/', views.StudenEnrollList.as_view()),
    path('enroll-course-status/<int:student_id>/<int:course_id>', views.enroll_course_status),
    path('teacher-students/<int:teacher_id>', views.EnrolledUsersByCourse.as_view()),
    path('enrolled-students/<int:course_id>', views.EnrolledUsersByCourse.as_view()),
    path('course-rating/<int:course_id>', views.CourseRatingList.as_view()),
    path('get-rating-status/<int:student_id>/<int:course_id>', views.rating_course_status),
    # показать курсы студента
    path('get-student-courses/<int:student_id>', views.EnrolledUsersByCourse.as_view()),
    path('get-student-recommend-courses/<int:student_id>', views.EnrolledUsersByCourse.as_view()),
    path('add-favorite-courses/', views.StudentFavoriteCourse.as_view()),
    path('remove-favorite-courses/<int:student_id>/<int:course_id>', views.remove_favorite_status),
    path('get-favorite-status/<int:student_id>/<int:course_id>', views.get_favorite_status),
    path('get-favorite-courses/<int:student_id>', views.StudentFavoriteCourse.as_view()),
    path('student-task/<int:teacher_id>', views.TaskForStudentList.as_view()),
    path('get-student-upcoming-task/<int:student_id>', views.StudentUpcomingTask.as_view()),
    path('update-task/<int:pk>', views.UpdateTask.as_view()),
    path('student/get-all-notify/<int:student_id>', views.NotificationList.as_view()),
    path('teacher/save-notify', views.NotificationList.as_view()),
# материалы курса
    path('study-materials/<int:course_id>', views.StudyMaterialList.as_view()),
    path('study-material/<int:pk>', views.StudyMaterialDetail.as_view()),
    path('student/study-materials/<int:course_id>', views.StudentStudyMaterialList.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)