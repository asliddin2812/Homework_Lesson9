from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from .models import Teacher
# Create your views here.

def index(request):
    return render(request,'base.html')

class TeacherListView(ListView):
    model = Teacher
    template_name = 'teacher/list.html'
    context_object_name = 'teacher_list'


class TeacherCreateView(CreateView):
    model = Teacher
    template_name = 'teacher/add.html'
    fields = ['name','email','experience_year', 'subject']
    success_url = reverse_lazy('created_')


class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'teacher/detail.html'
    context_object_name = 'teacher'

    def get_object(self):

        return Teacher.objects.filter(name=self.kwargs['name']).first()

class TeacherDetail(DetailView):
    model = Teacher
    template_name = 'teacher/detail1.html'
    context_object_name = 'teachers'

    def get_object(self):
        return Teacher.objects.filter(email=self.kwargs['email']).first()
