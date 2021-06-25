from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.StudentSignupView.as_view(),name='student-signup'),
    path('login/',views.StudentLogin.as_view(),name='student-login'),
]