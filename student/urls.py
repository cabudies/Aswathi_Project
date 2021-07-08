from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.StudentLogin.as_view(),name='student-login'),
    path('get_details/',views.get_details,name='get-cash-trans'),
]