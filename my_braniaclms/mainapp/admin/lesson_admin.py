from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from mainapp import models as mainapp_models


@admin.register(mainapp_models.Lessons)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["id", "get_course_name", "num", "title", "deleted"]
    ordering = ["-course__name", "num"]
    list_per_page = 10
    list_filter = ["course", "created", "deleted"]
    actions = ["mark_deleted", "mark_undeleted"]

    def get_course_name(self, obj):
        return obj.course.name

    get_course_name.short_description = _("Course")

    def mark_deleted(self, request, queryset):
        queryset.update(deleted=True)

    mark_deleted.short_description = _("Mark deleted")

    def mark_undeleted(self, request, queryset):
        queryset.update(deleted=False)

    mark_undeleted.short_description = _("Mark undeleted")
