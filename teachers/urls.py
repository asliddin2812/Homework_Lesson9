from django.urls import path
from .views import TeacherListView,index,TeacherCreateView,TeacherDetailView,TeacherDetail


urlpatterns = [
    path('', index, name='index'),
    path('teacher/<str:name>/', TeacherDetailView.as_view(), name='teacher_detail'),
    path('teacher/<str:email>/', TeacherDetail.as_view(), name='teachers'),
    path('created_/', TeacherCreateView.as_view(), name='created_'),
    path('teacher/', TeacherListView.as_view(), name='teacher_list'),
]