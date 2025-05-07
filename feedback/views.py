from django.shortcuts import render, redirect, get_object_or_404
from .models import Feedback
from .forms import FeedbackForm

def index(request):
    return render(request, 'base.html')

def feedback_list(request):
    feedback_list = Feedback.objects.all()
    return render(request, 'feedback/list.html', {'feedback_list': feedback_list})

def feedback_create(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_list')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/add.html', {'form': form})

def feedback_detail_by_student(request, student_name):
    feedback = Feedback.objects.filter(student_name=student_name).first()
    return render(request, 'feedback/detail.html', {'feedback': feedback})
