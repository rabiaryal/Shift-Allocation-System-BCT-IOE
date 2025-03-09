from django.db import models
from configure.models import Employee

class Shift(models.Model):
    shift_id = models.CharField(max_length=50)  # Shift name like 'Morning', 'Day', etc.
    shift_duration = models.IntegerField()  # Duration in hours
    shift_timing = models.CharField(max_length=50)  # Shift time like '7am to 11am'
    day = models.CharField(max_length=10, null=True, blank=True)# Day name like 'Day1', 'Day2', etc.

    def __str__(self):
        return f"{self.shift_id} - {self.shift_timing} on {self.day}"

    class Meta:
        unique_together = ('shift_id', 'day')  # Ensures no duplicate shift for the same day


class ShiftSchedule(models.Model):
    # day = models.CharField(max_length=10)  # Day name like 'Day1', 'Day2', etc.
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)  # Foreign key to Shift
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)  # Employee assigned to the shift

    class Meta:
        unique_together = ( 'shift', 'employee')  # Avoid duplicate assignments

    def __str__(self):
        return f"{self.employee} is assigned to {self.shift}"
