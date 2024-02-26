# student_management/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('standards/', views.StandardList.as_view()),
    path('standards/<int:pk>/', views.StandardDetail.as_view()),
    path('students/', views.StudentList.as_view()),
    path('students/<int:pk>/', views.StudentDetail.as_view()),
]
