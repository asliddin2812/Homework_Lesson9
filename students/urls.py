from django.urls import path
from .views import StudentListView,index,StudentCreateView,StudentDetailView,StudentDetail


urlpatterns = [
    path('', index, name='index'),
    path('student/<str:full_name>/', StudentDetailView.as_view(), name='student_detail'),
    path('student/<str:marks>/', StudentDetail.as_view(), name='students'),
    path('created/', StudentCreateView.as_view(), name='created'),
    path('student/', StudentListView.as_view(), name='student_list'),
]