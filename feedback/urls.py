from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('feedback/', views.feedback_list, name='feedback_list'),
    path('feedback/add/', views.feedback_create, name='feedback_create'),
    path('feedback/detail/<str:student_name>/', views.feedback_detail_by_student, name='feedback_detail_by_student'),
]
