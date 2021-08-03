from django.urls import path
from . import views

urlpatterns = [
    path('course_details/', views.CourseDetails, name='course_details'),
    path('list_courses/', views.CoursesList, name='list_courses'),
]
