# lms_backend для учебной системы (LMS)
![image](https://github.com/twoballs-ai/lms_backend/assets/83840596/b7038a20-e0e1-4685-aed8-cbe736c521bd)

api/ teacher/<br>
api/ teacher<drf_format_suffix:format> <br>
api/ popular-teachers/<br>
api/ popular-teachers<drf_format_suffix:format><br>
api/ teacher/<int:pk>/<br>
api/ teacher/<int:pk><drf_format_suffix:format><br>
api/ teacher/dashboard/<int:pk>/<br>
api/ teacher/dashboard/<int:pk><drf_format_suffix:format><br>
api/ teacher/reset-password/<int:teacher_id>/<br>
api/ teacher/reset-password/<int:teacher_id><drf_format_suffix:format><br>
api/ teacher-login<br>
api/ teacher-login<drf_format_suffix:format><br>
api/ student/<br>
api/ student<drf_format_suffix:format><br>
api/ student/<int:pk>/<br>
api/ student/<int:pk><drf_format_suffix:format><br>
api/ student/dashboard/<int:pk>/<br>
api/ student/dashboard/<int:pk><drf_format_suffix:format><br>
api/ student/reset-password/<int:student_id>/<br>
api/ student/reset-password/<int:student_id><drf_format_suffix:format><br>
api/ student-login<br>
api/ student-login<drf_format_suffix:format><br>
api/ category/<br>
api/ category<drf_format_suffix:format><br>
api/ course/<br>
api/ course<drf_format_suffix:format><br>
api/ popular-courses/<br>
api/ popular-courses<drf_format_suffix:format><br>
api/ search-by-course/<str:search_string><br>
api/ search-by-course/<str:search_string><drf_format_suffix:format><br>
api/ update-view/<int:course_id><br>
api/ update-view/<int:course_id><drf_format_suffix:format><br>
api/ student-testimonial/<br>
api/ student-testimonial<drf_format_suffix:format><br>
api/ course/<int:pk><br>
api/ course/<int:pk><drf_format_suffix:format><br>
api/ chapter/<int:pk><br>
api/ chapter/<int:pk><drf_format_suffix:format><br>
api/ course-chapter/<int:course_id><br>
api/ course-chapter/<int:course_id><drf_format_suffix:format><br>
api/ chapter-module/<int:chapter_id><br>
api/ chapter-module/<int:chapter_id><drf_format_suffix:format>
api/ module-stage/<int:module_id>
api/ module-stage/<int:module_id><drf_format_suffix:format>
api/ teacher-courses/<int:teacher_id>
api/ teacher-courses/<int:teacher_id><drf_format_suffix:format>
api/ teacher-courses-detail/<int:pk>
api/ teacher-courses-detail/<int:pk><drf_format_suffix:format>
api/ student-course-enroll/
api/ student-course-enroll<drf_format_suffix:format>
api/ enroll-course-status/<int:student_id>/<int:course_id>
api/ enroll-course-status/<int:student_id>/<int:course_id><drf_format_suffix:format>
api/ teacher-students/<int:teacher_id>
api/ teacher-students/<int:teacher_id><drf_format_suffix:format>
api/ enrolled-students/<int:course_id>
api/ enrolled-students/<int:course_id><drf_format_suffix:format>
api/ course-rating/<int:course_id>
api/ course-rating/<int:course_id><drf_format_suffix:format>
api/ get-rating-status/<int:student_id>/<int:course_id>
api/ get-rating-status/<int:student_id>/<int:course_id><drf_format_suffix:format>
api/ get-student-courses/<int:student_id>
api/ get-student-courses/<int:student_id><drf_format_suffix:format>
api/ get-student-recommend-courses/<int:student_id>
api/ get-student-recommend-courses/<int:student_id><drf_format_suffix:format>
api/ add-favorite-courses/
api/ add-favorite-courses<drf_format_suffix:format>
api/ remove-favorite-courses/<int:student_id>/<int:course_id>
api/ remove-favorite-courses/<int:student_id>/<int:course_id><drf_format_suffix:format>
api/ get-favorite-status/<int:student_id>/<int:course_id>
api/ get-favorite-status/<int:student_id>/<int:course_id><drf_format_suffix:format>
api/ get-favorite-courses/<int:student_id>
api/ get-favorite-courses/<int:student_id><drf_format_suffix:format>
api/ student-task/<int:teacher_id>
api/ student-task/<int:teacher_id><drf_format_suffix:format>
api/ get-student-upcoming-task/<int:student_id>
api/ get-student-upcoming-task/<int:student_id><drf_format_suffix:format>
api/ update-task/<int:pk>
api/ update-task/<int:pk><drf_format_suffix:format>
api/ student/get-all-notify/<int:student_id>
api/ student/get-all-notify/<int:student_id><drf_format_suffix:format>
api/ teacher/save-notify
api/ teacher/save-notify<drf_format_suffix:format>
api/ study-materials/<int:course_id>
api/ study-materials/<int:course_id><drf_format_suffix:format>
api/ study-material/<int:pk>
api/ study-material/<int:pk><drf_format_suffix:format>
api/ student/study-materials/<int:course_id>
api/ student/study-materials/<int:course_id><drf_format_suffix:format>