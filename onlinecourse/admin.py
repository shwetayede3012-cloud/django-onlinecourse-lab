
from django.contrib import admin
from .models import (
    Course,
    Lesson,
    Question,
    Choice,
    Submission,
    Instructor,
    Learner,
)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1


class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]


class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ("name",)
    list_filter = ("name",)
    search_fields = ("name", "description")


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
admin.site.register(Instructor)
admin.site.register(Learner)
