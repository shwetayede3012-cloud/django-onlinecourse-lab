

from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Question, Choice, Submission


def course_details(request, course_id=1):
    course = get_object_or_404(Course, id=course_id)
    return render(
        request,
        "onlinecourse/course_details_bootstrap.html",
        {"course": course}
    )


def exam(request):
    questions = Question.objects.prefetch_related("choices").all()
    return render(
        request,
        "onlinecourse/exam.html",
        {"questions": questions}
    )


def submit(request):
    if request.method != "POST":
        return redirect("exam")

    if not request.user.is_authenticated:
        return redirect("/admin/login/")

    questions = Question.objects.prefetch_related("choices").all()
    selected_choices = []

    for question in questions:
        choice_id = request.POST.get(f"choices_{question.id}")

        if choice_id:
            choice = question.choices.filter(id=choice_id).first()
            if choice:
                selected_choices.append(choice)

    score = sum(
        1 for choice in selected_choices if choice.is_correct
    )

    submission = Submission.objects.create(
        user=request.user,
        score=score,
        total_questions=questions.count()
    )
    submission.selected_choices.set(selected_choices)

    return render(
        request,
        "onlinecourse/exam_result.html",
        {"submission": submission}
    )


def show_exam_result(request):
    if not request.user.is_authenticated:
        return redirect("/admin/login/")

    submission = Submission.objects.filter(
        user=request.user
    ).order_by("-submitted_at").first()

    return render(
        request,
        "onlinecourse/exam_result.html",
        {"submission": submission}
    )
