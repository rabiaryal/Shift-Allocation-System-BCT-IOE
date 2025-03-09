from django.db import models

class Employee(models.Model):
    e_id = models.IntegerField(primary_key=True)
    e_name = models.CharField(max_length=50)
    no_of_hours_worked = models.IntegerField()
    designation = models.CharField(max_length=50)
    e_gmail = models.EmailField(max_length=100)
    e_priority = models.IntegerField()
