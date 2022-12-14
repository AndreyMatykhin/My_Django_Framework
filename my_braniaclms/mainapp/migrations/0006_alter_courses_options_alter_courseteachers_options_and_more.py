# Generated by Django 4.1.4 on 2022-12-13 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_data_course_teachers_migration'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courses',
            options={'verbose_name': 'Course', 'verbose_name_plural': 'Courses'},
        ),
        migrations.AlterModelOptions(
            name='courseteachers',
            options={'verbose_name': 'Teacher', 'verbose_name_plural': 'Teachers'},
        ),
        migrations.AlterModelOptions(
            name='lessons',
            options={'ordering': ('course', 'num'), 'verbose_name': 'Lesson', 'verbose_name_plural': 'Lessons'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ('-created',), 'verbose_name': 'News', 'verbose_name_plural': 'News'},
        ),
    ]
