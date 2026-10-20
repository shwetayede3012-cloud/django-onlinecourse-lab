
from django.urls import path
from . import views

urlpatterns = [
    path("course/", views.course_details, name="course_details"),
    path("exam/", views.exam, name="exam"),
    path("submit/", views.submit, name="submit"),
    path("exam-result/", views.show_exam_result, name="show_exam_result"),
]
