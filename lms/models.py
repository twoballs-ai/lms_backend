from django.db import models
from django.core import serializers



# Create your models here.
from user.models import Student, Teacher
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class CourseCategory(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=1000)

    class Meta:
        verbose_name = '1. категория курса'
        verbose_name_plural = '1. категории курсов'

    def total_courses(self):
        return Course.objects.filter(category = self).count()

    def __str__(self):
        return self.title


class Course(models.Model):
    category = models.ForeignKey(CourseCategory,on_delete=models.CASCADE , related_name='category_course')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher_course')
    title = models.CharField(max_length=150)
    description = models.TextField(null=True)
    course_image = models.ImageField(upload_to='course_images/', null=True)
    technologicals = models.TextField(blank=True, null=True)
    course_views = models.BigIntegerField(default=0)

    class Meta:
        verbose_name = '2. курс'
        verbose_name_plural = '2. курсы'

    def related_courses(self):
        related_courses = Course.objects.filter(technologicals__icontains=self.technologicals)
        return serializers.serialize('json',related_courses)
        
    def technological_list(self):
        technological_list=self.technologicals.split(',')
        return technological_list
    
    def total_enrolled_students(self):
        total_enrolled_students= CourseEnroll.objects.filter(course = self).count()
        return total_enrolled_students

    def course_rating(self):
        course_rating= CourseRating.objects.filter(course = self).aggregate(avg_rating=models.Avg('rating'))
        return course_rating['avg_rating']

    def __str__(self):
        return self.title
    

class Chapter(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_chapters')
    title = models.CharField(max_length=150)
    description = models.TextField()
    
    class Meta:
        verbose_name = '3. Глава'
        verbose_name_plural = '3. Глава'

    def __str__(self):
        return self.title


class Module(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='chapter_modules')
    title = models.CharField(max_length=150)
    description = models.TextField(null=True,blank=True)

    class Meta:
        verbose_name = '4. модули'
        verbose_name_plural = '4. модули'

    def __str__(self):
        return f'{self.title}'    
    
class Stage(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='stage_modules')

    class Meta:
        verbose_name = '5. этап'
        verbose_name_plural = '5. этап'

    # def get_stage_pass_status(self):
    #     get_stage_pass_status = StagePass.objects.filter(stage=self.pk)
    #     return serializers.serialize('json',get_stage_pass_status)


    
    def __str__(self):
        return f"{self.module}"   
    


class StagePass(models.Model):
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE, related_name='stage_stage_pass')
    # student = models.ForeignKey(Student, on_delete=models.CASCADE,related_name='stage_passed_students')
    is_passed = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'пройденные уроки'
        verbose_name_plural = 'пройденные уроки'


    def __str__(self):
        return f"{self.student}-{self.stage}-{self.is_passed}"   



class CourseEnroll(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE,related_name='enrolled_courses')
    # student = models.ForeignKey(Student, on_delete=models.CASCADE,related_name='enrolled_students')
    enrolled_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Студент подписанный на курс'
        verbose_name_plural = 'Студенты подписанные на курсы'

    def __str__(self):
        return f"{self.course}-{self.student}"   
# Эта функция необходима для перехода на первый модуль первого урока курса 
    def student_course_first_module(self):
        student_course_first_module = Chapter.objects.filter(course= self.course).first()
        course_module = Module.objects.filter(chapter = student_course_first_module).values_list('pk', flat=True).first()
        first_module_stage_pk = Stage.objects.filter(module = course_module).values_list('pk', flat=True).first()
        print(first_module_stage_pk)
        return {'first_module_pk':course_module,'first_stage_pk':first_module_stage_pk}
    

class CourseRating(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='rating_courses')
    # student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='rating_students')
    rating = models.PositiveBigIntegerField(default=0)
    review = models.TextField(null=True)
    review_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Рейтинг курса'
        verbose_name_plural = 'Рейтинги курсов'

    def __str__(self):
        return f"{self.course}-{self.student}-{self.rating}"   
    

class TotalStudentScore(models.Model):
    # student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='total_score_students')
    total_student_score = models.PositiveBigIntegerField(default=0)

    class Meta:
        verbose_name = 'Баллы ученика'
        verbose_name_plural = 'Баллы ученика'

    def __str__(self):
        return f"{self.student}-{self.total_student_score}"       


class TotalStudentEnergy(models.Model):
    # student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='total_energy_students')
    total_student_energy = models.PositiveBigIntegerField(default=100)

    class Meta:
        verbose_name = 'Энергия ученика'
        verbose_name_plural = 'Энергия ученика'

    def __str__(self):
        return f"{self.student}-{self.total_student_energy}"       
    

class FavoriteCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='favorite_courses')
    # student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='favorite_students')
    is_favorite = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Избранный курс'
        verbose_name_plural = 'Избранные курсы'

    def __str__(self):
        return f"{self.course}-{self.student}"   
    

class TaskForStudentsFromTeacher(models.Model):
    # student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='tasks_student')
    # teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='tasks_teacher')
    complete_status = models.BooleanField(default=False, null=True)
    title = models.CharField(max_length=150)
    detail = models.TextField(null=True)
    add_time = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = 'Упражнения для ученика'
        verbose_name_plural = 'Упражнение для ученика'

    def __str__(self):
        return f"{self.title}"   
    

class Notification(models.Model):
    # teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    # student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    # notification_text= models.TextField(verbose_name='Notification Text')
    notification_subject= models.CharField(max_length=150, verbose_name='Notification Subject', null=True)
    notification_for= models.CharField(max_length=150, verbose_name='Notification For', null=True)
    notification_created_time = models.DateTimeField(auto_now_add=True)
    notification_read_status = models.BooleanField(default=False, verbose_name='Notification Status')

    class Meta:
        verbose_name = 'Оповещение'
        verbose_name_plural = 'Оповещения'



class StudyMaterial(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    upload = models.FileField(upload_to='study_material/', null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Материалы для курса'
        verbose_name_plural = 'Материалы для курса'

    def __str__(self):
        return self.title
        

# class stageScore(models.Model):
