from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ShiftSwapSerializer
from configure.models import Employee
from swap.models import ShiftSchedule, Shift
import os

@api_view(["POST"])
def swap_shifts_api(request):
    serializer = ShiftSwapSerializer(data=request.data)

    if serializer.is_valid():
        # Extract validated data
        emp1_id = int(serializer.validated_data["employee1_id"])
        emp2_id = int(serializer.validated_data["employee2_id"])
        day = serializer.validated_data["day"]

        try:
            # Fetch employees from the database
            emp1 = Employee.objects.get(e_id=emp1_id)
            emp2 = Employee.objects.get(e_id=emp2_id)
        except Employee.DoesNotExist:
            return Response({"message": "One or both employees do not exist."}, status=status.HTTP_400_BAD_REQUEST)

        # Ensure both employees have the same designation
        if emp1.designation != emp2.designation:
            return Response({"message": "Employees have different designations."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Find the shift schedules for both employees
            emp1_shift_schedule = ShiftSchedule.objects.get(employee=emp1, shift__day=day)
            emp2_shift_schedule = ShiftSchedule.objects.get(employee=emp2, shift__day=day)
        except ShiftSchedule.DoesNotExist:
            return Response({"message": "One or both employees do not have a shift assigned on this day."}, status=status.HTTP_400_BAD_REQUEST)

        # Swap the shifts
        emp1_shift_schedule.employee, emp2_shift_schedule.employee = emp2, emp1
        emp1_shift_schedule.save()
        emp2_shift_schedule.save()

        return Response({"message": f"Shifts swapped successfully for {day}!"}, status=status.HTTP_200_OK)

    # If the serializer is not valid, return errors
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)