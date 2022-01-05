from django.urls import path,include
from rest_framework import views
from .import views

urlpatterns = [
    
    path('students/',views.student_list),
    path('students/<int:pk>/',views.student_detail),
]