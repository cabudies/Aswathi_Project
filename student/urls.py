from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.StudentLogin.as_view(),name='student-login'),
    path('get_details/',views.get_details,name='get-cash-trans'),
    path('student_details/',views.student_details,name='student_details'),
    path('student_form/',views.StudentForm.as_view(),name = 'student_form'),
    path('add_details/',views.StudentEditProfile.as_view(),name = 'student_adding_details'),
]     