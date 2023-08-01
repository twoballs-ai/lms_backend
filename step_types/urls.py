from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from step_types import views

urlpatterns = [
    # квизы
    path('class/', views.ClassicLessonList.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)