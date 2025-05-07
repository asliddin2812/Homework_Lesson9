from django.urls import path
from .views import index,teacher_list,teacher_create,teacher_detail


urlpatterns = [
    path('', index, name='index'),
    path('teacher/<str:name>/', teacher_detail, name='teacher_detail'),
    path('created_/', teacher_create, name='teacher_create'),
    path('teacher/', teacher_list, name='teacher_list'),
]