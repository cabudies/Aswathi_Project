from django.urls import path
from . import views


urlpatterns = [

    path('login/',views.HodLoginView.as_view(),name='login'),
    path('create_hod/',views.EditHodProfile.as_view(),name='create_hod'),
    path('view_hod/',views.ViewHodProfile.as_view(),name='view_hod'),
    
]