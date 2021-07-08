from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('signup/',views.createuser,name='sign-up'),
    path('add_student/',views.StudentSignupView.as_view(),name='student-signup'),
    path('login/', views.LoginTokenView.as_view(), name='token_obtain_pair'),
    path('logout/', views.LogoutView.as_view(), name='blacklist-token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('approve/', views.approve, name='approve-student'),
    path('forgetpassword/<int:pk>',views.ChangePasswordView.as_view(),name='forget-password')
]