from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    ordering = 'group'

    template = 'school/students_list.html'

    students = Student.objects.all().prefetch_related('teacher').order_by(ordering)

    context = {'object_list': students}

    return render(request, template, context)
