from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from step_types import views

urlpatterns = [
    # квизы
    path('classic-lesson/<int:stage_id>', views.ClassicLessonList.as_view()),
    path('quiz-lesson/<int:stage_id>', views.QuizLessonList.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)