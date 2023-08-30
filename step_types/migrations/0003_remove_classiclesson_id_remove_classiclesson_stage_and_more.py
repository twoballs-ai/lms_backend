# Generated by Django 4.2.1 on 2023-08-14 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0001_initial'),
        ('step_types', '0002_alter_classiclesson_stage_alter_quiz_stage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classiclesson',
            name='id',
        ),
        migrations.RemoveField(
            model_name='classiclesson',
            name='stage',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='id',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='stage',
        ),
        migrations.CreateModel(
            name='LessonType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='lms.stage')),
            ],
        ),
        migrations.AddField(
            model_name='classiclesson',
            name='lessontype_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='step_types.lessontype'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='lessontype_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='step_types.lessontype'),
            preserve_default=False,
        ),
    ]