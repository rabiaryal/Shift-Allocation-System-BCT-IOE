from django.urls import path, include
from .views import *


# urlpatterns = [
#     path('config/', configure_view, name='configure'),
#     path('employees/', EmployeesView.as_view({'get': 'list'}), name='employees_list'),
# ]



urlpatterns = [
    path('api/employee/', EmployeeListAPIView.as_view(), name='employee_list'),  # List & Create
    path('api/employee/<int:pk>/', EmployeeDetailAPIView.as_view(), name='employee_detail'),  # Retrieve, Update, Delete
    path('assign-shifts/', assign_shifts_api, name='assign_shifts_api'),
    path("get-excel/", RetrieveExcelView.as_view(), name="get-excel"),
    path('employees/<int:employee_id>/', EmployeeSearchView.as_view(), name='employee-search'),
    path('employeecsv/<int:employee_id>/', EmployeeCSVSearchView.as_view(), name='employee-search'),
]
