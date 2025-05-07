from django.shortcuts import render, redirect
from .forms import TeacherForm

from .models import Teacher
# Create your views here.

def index(request):
    return render(request,'home.html')

def teacher_list(request):
    teacher_list = Teacher.objects.all()
    return render(request,'teacher/list.html',{'teacher_list':teacher_list})

def teacher_create(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm()
    return render(request,'teacher/add.html',{'form':form})

def teacher_detail(request, name):
    teacher = Teacher.objects.get(name=name)
    return render(request,'teacher/detail.html',{'teacher':teacher})