from django.db import models

# Create your models here.
class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_id = models.CharField(max_length=3)
    mobile = models.CharField(max_length=10)


    # Create / Insert / Add - POST
    # Retrieve / Fetch - GET
    # Update / Edit - PUT
    # Delete / Remove - DELETE