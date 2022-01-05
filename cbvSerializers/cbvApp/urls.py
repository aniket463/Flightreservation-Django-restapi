
from django.db import router
from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter

# urlpatterns = [
  
#     path('students/',views.StudentList.as_view()),
#     path('students/<int:pk>/',views.StudentDetail.as_view() )
# ]

#Creating a router
router = DefaultRouter()
router.register('students',views.StudentViewSet)
urlpatterns = [
    path('',include(router.urls)),
]
