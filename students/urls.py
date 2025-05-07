from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('student/', views.student_list, name='student_list'),
    path('student/add/', views.student_create, name='student_create'),
    path('student/detail/<str:student_name>/', views.student_detail, name='student_detail'),
]
