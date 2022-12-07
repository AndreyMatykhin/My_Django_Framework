# Generated by Django 4.1.3 on 2022-12-07 06:40

from django.db import migrations


def forwards_func(apps, schema_editor):
    # Get model
    CourseTeachers = apps.get_model("mainapp", "CourseTeachers")
    # Create model's objects
    CourseTeachers.objects.create(
        name_first="Альфред",
        name_second="Нуцубидзе",
        day_birth="1990-07-10",
    ).course.set(apps.get_model("mainapp", "Courses").objects.filter(id__in=[1, 3]))
    CourseTeachers.objects.create(
        name_first="Роман",
        name_second="Доржинов",
        day_birth="1988-02-04",
    ).course.set(apps.get_model("mainapp", "Courses").objects.filter(id__in=[2, 4]))
    CourseTeachers.objects.create(
        name_first="Ярослав",
        name_second="Конягин",
        day_birth="1981-12-08",
    ).course.set(apps.get_model("mainapp", "Courses").objects.filter(id__in=[3, 5]))
    CourseTeachers.objects.create(
        name_first="Автандил",
        name_second="Наварский",
        day_birth="1983-05-16",
    ).course.set(apps.get_model("mainapp", "Courses").objects.filter(id__in=[4, 6]))
    CourseTeachers.objects.create(
        name_first="Роза",
        name_second="Уланова",
        day_birth="1986-05-09",
    ).course.set(apps.get_model("mainapp", "Courses").objects.filter(id__in=[5, 7]))
    CourseTeachers.objects.create(
        name_first="Бронислава",
        name_second="Алиева",
        day_birth="1971-01-07",
    ).course.set(apps.get_model("mainapp", "Courses").objects.filter(id__in=[6, 8]))
    CourseTeachers.objects.create(
        name_first="Диана",
        name_second="Попова",
        day_birth="1990-08-25",
    ).course.set(apps.get_model("mainapp", "Courses").objects.filter(id__in=[1, 8]))


def reverse_func(apps, schema_editor):
    # Get model
    CourseTeachers = apps.get_model("mainapp", "CourseTeachers")
    # Delete objects
    CourseTeachers.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ('mainapp', '0004_data_lessons_migration'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
