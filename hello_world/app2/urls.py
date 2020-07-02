from django.contrib import admin
from django.urls import path
from . import views
from app2.views import (EmployeeUpdate, EmployeeProfile)
urlspatterns =[
    path('admin/',admin.site.urls),
    path('signup/',views.signup,name='signup'),
    path('employee/update',EmployeeUpdate.as_view(),name="update_employee"),
    path('employee/',EmployeeProfile.as_view(),name="employee_profile"),
    path('delete_employee/',views.employee_delete,name='employee_delete')
]