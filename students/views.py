from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from .models import Student
# Create your views here.

def index(request):
    return render(request,'base.html')

class StudentListView(ListView):
    model = Student
    template_name = 'student/list.html'
    context_object_name = 'student_list'


class StudentCreateView(CreateView):
    model = Student
    template_name = 'student/add.html'
    fields = ['full_name','grade','is_active', 'marks']
    success_url = reverse_lazy('created')


class StudentDetailView(DetailView):
    model = Student
    template_name = 'student/detail.html'
    context_object_name = 'student'

    def get_object(self):

        return Student.objects.filter(full_name=self.kwargs['full_name']).first()

class StudentDetail(DetailView):
    model = Student
    template_name = 'student/detail1.html'
    context_object_name = 'students'

    def get_object(self):
        return Student.objects.filter(marks=self.kwargs['marks']).first()
