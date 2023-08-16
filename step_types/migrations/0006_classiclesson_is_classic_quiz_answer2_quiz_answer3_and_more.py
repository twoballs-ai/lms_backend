# Generated by Django 4.2.1 on 2023-08-15 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('step_types', '0005_remove_classiclesson_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='classiclesson',
            name='is_classic',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='answer2',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='answer3',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='answer4',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='is_quiz',
            field=models.BooleanField(default=True),
        ),
    ]
