from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from quiz import views

urlpatterns = [
    # квизы
    path('quiz/', views.QuizList.as_view()),
    path('teacher-quiz/<int:teacher_id>', views.TeacherQuizList.as_view()),
    path('teacher-quiz-detail/<int:pk>', views.TeacherQuizDetail.as_view()),
    path('quiz/<int:pk>', views.QuizDetailView.as_view()),
    path('quiz-questions/<int:quiz_id>', views.QuizQuestionList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)