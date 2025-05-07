from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

def index(request):
    return render(request, 'base.html')

def student_list(request):
    student_list = Student.objects.all()
    return render(request, 'student/list.html', {'student_list': student_list})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student/add.html', {'form': form})

def student_detail(request, full_name):
    student = Student.objects.filter(full_name=full_name).first()
    return render(request, 'student/detail.html', {'student': student})
