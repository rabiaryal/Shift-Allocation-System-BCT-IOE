from rest_framework import serializers
from configure.models import Employee
from swap.models import ShiftSchedule, Shift

class ShiftSwapSerializer(serializers.Serializer):
    employee1_id = serializers.CharField()
    employee2_id = serializers.CharField()
    day = serializers.CharField()

    def validate(self, data):
        emp1_id = int(data["employee1_id"])  # Convert to int
        emp2_id = int(data["employee2_id"])  # Convert to int
        day = data["day"]

        # Check if employees exist
        try:
            emp1 = Employee.objects.get(e_id=emp1_id)
            emp2 = Employee.objects.get(e_id=emp2_id)
        except Employee.DoesNotExist:
            raise serializers.ValidationError("One or both employees do not exist.")

        # Ensure employees have the same designation
        if emp1.designation != emp2.designation:
            raise serializers.ValidationError("Employees have different designations.")

        # Ensure both employees have shifts assigned for that day
        if not ShiftSchedule.objects.filter(employee=emp1, shift__day=day).exists() or \
           not ShiftSchedule.objects.filter(employee=emp2, shift__day=day).exists():
            raise serializers.ValidationError("One or both employees do not have a shift assigned on this day.")

        return data