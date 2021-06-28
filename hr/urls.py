from django.urls import path
from . import views

urlpatterns = [

    path('login/',views.HrLoginView.as_view(),name="hr-login"),
]