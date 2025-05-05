from django.urls import path
from .views import FeedbackListView,index,FeedbackCreateView,FeedbackDetailView,FeedbackDetail


urlpatterns = [
    path('', index, name='index'),
    path('feedback/<str:student_name>/', FeedbackDetailView.as_view(), name='feedback_detail'),
    path('feedback/<str:message>/', FeedbackDetail.as_view(), name='feedbacks'),
    path('create/', FeedbackCreateView.as_view(), name='create'),
    path('feedback/', FeedbackListView.as_view(), name='feedback_list'),
]