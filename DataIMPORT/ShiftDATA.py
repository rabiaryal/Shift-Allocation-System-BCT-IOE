import os
import django
import sys

sys.path.append('C:\\django\\SAS_final\\SAS')

# Set the DJANGO_SETTINGS_MODULE environment variable to your settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

# Initialize Django
django.setup()

# Now you can import your models and interact with the database
from swap.models import Shift
from configure.models import Employee
from utils.opt2 import assign_shifts  # Import your function from opt2.py

# Step 1: Define shift data for each day (Day1 to Day7)
shifts = {
    f"Day{i}": [
        {"shift_id": "Morning", "shift_duration": 4, "shift_timing": "7am to 11am"},
        {"shift_id": "Day", "shift_duration": 4, "shift_timing": "11am to 3pm"},
        {"shift_id": "Evening", "shift_duration": 4, "shift_timing": "3pm to 7pm"},
        {"shift_id": "Night", "shift_duration": 4, "shift_timing": "7pm to 11pm"}
    ]
    for i in range(1, 8)  # Generates Day1 to Day7
}

# Step 2: Create Shift objects for Day1 to Day7
for day, shift_list in shifts.items():
    for shift_data in shift_list:
        # Create or get the shift for each day (no need for the 'day' argument in Shift creation, since it's handled by ShiftSchedule)
        shift, created = Shift.objects.get_or_create(
            shift_id=shift_data["shift_id"],
            day=day,  # Ensure the day field is added for Day1 to Day7
            defaults={
                "shift_duration": shift_data["shift_duration"],
                "shift_timing": shift_data["shift_timing"]
            }
        )
        # if created:
        #     print(f"Created Shift: {shift_data['shift_id']} on {day}")

# print("Shift data has been created for Day1 to Day7.")
