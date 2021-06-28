from django.urls import path
from . import views


urlpatterns = [
  path('login/',views.RegistrarLoginView.as_view(),name='registrar-login'),
  path('approve/',views.approve_student,name='approve_student'),
]  