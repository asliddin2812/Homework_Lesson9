from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

import feedback
from students.models import Student
# Create your views here.
from .models import Feedback

def index(request):
    return render(request,'base.html')

class FeedbackListView(ListView):
    model = Feedback
    template_name = 'feedback/list.html'
    context_object_name = 'feedback_list'


class FeedbackCreateView(CreateView):
    model = Feedback
    template_name = 'feedback/add.html'
    fields = ['student_name', 'message']
    success_url = reverse_lazy('create')


class FeedbackDetailView(DetailView):
    model = Feedback
    template_name = 'feedback/detail.html'
    context_object_name = 'feedback'

    def get_object(self):

        return Feedback.objects.filter(student_name=self.kwargs['student_name']).first()

class FeedbackDetail(DetailView):
    model = Feedback
    template_name = 'feedback/detail1.html'
    context_object_name = 'feedbacks'

    def get_object(self):
        return Feedback.objects.filter(message=self.kwargs['message']).first()
