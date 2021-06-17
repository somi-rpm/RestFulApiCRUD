from EmployeeAPI.viewsets import EmployeeViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Employee', EmployeeViewset)

# localhost:p/api/
# Get, POST, PUT, DELETE
# list <->  localhost:p/api/Employee
# retrieve <->  localhost:p/api/Employee/5