
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('superadmin/',include('administrator.urls')),
    path('student/',include('student.urls')),
    path('accountant/',include('accountant.urls')),
    path('teacher/',include('teacher.urls')),
    path('registrar/',include('registrar.urls')),
    path('hod/',include('hod.urls')),
    path('hr/',include('hr.urls')),
    path('course/',include('course.urls')),
]
