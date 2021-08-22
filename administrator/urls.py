from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('signup/',views.createuser,name='sign-up'),
    path('add_student/',views.StudentSignupView.as_view(),name='student-signup'),
    path('add_accountant/',views.AccountantSignupView.as_view(),name='accountant-signup'),
    path('add_registrar/',views.RegistrarSignupView.as_view(),name='accountant-signup'),
    path('add_hod/',views.HodSignupView.as_view(),name='hod-signup'),
    path('add_hr/',views.HrSignupView.as_view(),name='hr-signup'),
    path('login/', views.LoginTokenView.as_view(), name='token_obtain_pair'),
    path('logout/', views.LogoutView.as_view(), name='blacklist-token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('approve/', views.approve, name='approve-student'),
    path('view_student_forms/', views.view_student_forms, name='view_student_forms'),
    path('forgetpassword/<int:pk>',views.ChangePasswordView.as_view(),name='forget-password')
]