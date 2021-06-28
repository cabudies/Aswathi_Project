from django.urls import path
from . import views


urlpatterns = [

    path('login/',views.HodLoginView.as_view(),name='login'),
    
]