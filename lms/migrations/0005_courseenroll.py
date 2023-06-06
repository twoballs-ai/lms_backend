# Generated by Django 4.2.1 on 2023-06-06 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_rename_phone_student_username_remove_student_address_and_more'),
        ('lms', '0004_alter_course_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseEnroll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrolled_time', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrolled_courses', to='lms.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrolled_students', to='user.student')),
            ],
            options={
                'verbose_name': 'Подписанный курс',
                'verbose_name_plural': 'Подписанные курсы',
            },
        ),
    ]
