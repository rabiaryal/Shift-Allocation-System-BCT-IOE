from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        


class ShiftAssignmentSerializer(serializers.Serializer):
    designation_counts = serializers.DictField(child=serializers.DictField(child=serializers.IntegerField()))
