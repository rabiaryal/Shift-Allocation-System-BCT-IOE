from pulp import LpProblem, LpVariable, lpSum, LpMinimize
import pandas as pd
import csv
import random


# Sample data
employees = [
    {
        "e_id": 1,
        "e_name": "Alice Johnson",
        "no_of_hours_worked": 0,
        "designation": "Cashier",
        "e_gmail": "alice.johnson@email.com",
        "e_priority": 8
    },
    {
        "e_id": 2,
        "e_name": "Bob Smith",
        "no_of_hours_worked": 0,
        "designation": "Inventory Manager",
        "e_gmail": "bob.smith@email.com",
        "e_priority": 7
    },
    {
        "e_id": 3,
        "e_name": "Carol Davis",
        "no_of_hours_worked": 0,
        "designation": "Customer Help",
        "e_gmail": "carol.davis@email.com",
        "e_priority": 8
    },
    {
        "e_id": 4,
        "e_name": "David Wilson",
        "no_of_hours_worked": 0,
        "designation": "Cleaning Staff",
        "e_gmail": "david.wilson@email.com",
        "e_priority": 3
    },
    {
        "e_id": 5,
        "e_name": "Eva Brown",
        "no_of_hours_worked": 0,
        "designation": "Cashier",
        "e_gmail": "eva.brown@email.com",
        "e_priority": 8
    },
    {
        "e_id": 6,
        "e_name": "Shashank Katuwal",
        "no_of_hours_worked": 0,
        "designation": "Cashier",
        "e_gmail": "katu@email.com",
        "e_priority": 8
    },
    {
        "e_id": 7,
        "e_name": "Bishwa Kandel",
        "no_of_hours_worked": 0,
        "designation": "Customer Help",
        "e_gmail": "carolbishwa@email.com",
        "e_priority": 8
    },
    {
        "e_id": 8,
        "e_name": "Rabi Aryal",
        "no_of_hours_worked": 0,
        "designation": "Customer Help",
        "e_gmail": "carolRabi@email.com",
        "e_priority": 8
    },
    {
        "e_id": 9,
        "e_name": "Bishwa Kandel",
        "no_of_hours_worked": 0,
        "designation": "Manager",
        "e_gmail": "carolbis@email.com",
        "e_priority": 8
    },
    {
        "e_id": 10,
        "e_name": "Sumesh Dhonju",
        "no_of_hours_worked": 0,
        "designation": "Supervisor",
        "e_gmail": "carolSum@email.com",
        "e_priority": 8
    },
    {
        "e_id": 11,
        "e_name": "John Doe",
        "no_of_hours_worked": 0,
        "designation": "Inventory Manager",
        "e_gmail": "john.doe@email.com",
        "e_priority": 7
    },
    {
        "e_id": 12,
        "e_name": "Jane Smith",
        "no_of_hours_worked": 0,
        "designation": "Cashier",
        "e_gmail": "jane.smith@email.com",
        "e_priority": 8
    },
    {
        "e_id": 13,
        "e_name": "Mike Brown",
        "no_of_hours_worked": 0,
        "designation": "Cleaning Staff",
        "e_gmail": "mike.brown@email.com",
        "e_priority": 3
    },
    {
        "e_id": 14,
        "e_name": "Emily Davis",
        "no_of_hours_worked": 0,
        "designation": "Customer Help",
        "e_gmail": "emily.davis@email.com",
        "e_priority": 8
    },
    {
        "e_id": 15,
        "e_name": "Chris Wilson",
        "no_of_hours_worked": 0,
        "designation": "Supervisor",
        "e_gmail": "chris.wilson@email.com",
        "e_priority": 8
    },
    {
        "e_id": 16,
        "e_name": "Sophia Martinez",
        "no_of_hours_worked": 0,
        "designation": "Cashier",
        "e_gmail": "sophia.martinez@email.com",
        "e_priority": 8
    },
    {
        "e_id": 17,
        "e_name": "Liam Taylor",
        "no_of_hours_worked": 0,
        "designation": "Manager",
        "e_gmail": "liam.taylor@email.com",
        "e_priority": 8
    },
    {
        "e_id": 18,
        "e_name": "Emma White",
        "no_of_hours_worked": 0,
        "designation": "Cleaning Staff",
        "e_gmail": "emma.white@email.com",
        "e_priority": 3
    },
    {
        "e_id": 19,
        "e_name": "Noah Harris",
        "no_of_hours_worked": 0,
        "designation": "Customer Help",
        "e_gmail": "noah.harris@email.com",
        "e_priority": 8
    },
  
]


shifts = {
    "Day1": [
        {"shift_id": "M1", "shift_duration": 3, "shift_timing": "8am to 11am"},
        {"shift_id": "D1", "shift_duration": 3, "shift_timing": "11am to 2pm"},
        {"shift_id": "E1", "shift_duration": 3, "shift_timing": "2pm to 5pm"},
        {"shift_id": "E2", "shift_duration": 3, "shift_timing": "5pm to 8pm"},
        {"shift_id": "N1", "shift_duration": 3, "shift_timing": "8pm to 11pm"}
    ],
    "Day2": [
        {"shift_id": "M1", "shift_duration": 3, "shift_timing": "8am to 11am"},
        {"shift_id": "D1", "shift_duration": 3, "shift_timing": "11am to 2pm"},
        {"shift_id": "E1", "shift_duration": 3, "shift_timing": "2pm to 5pm"},
        {"shift_id": "E2", "shift_duration": 3, "shift_timing": "5pm to 8pm"},
        {"shift_id": "N1", "shift_duration": 3, "shift_timing": "8pm to 11pm"}
    ],
    "Day3": [
        {"shift_id": "M1", "shift_duration": 3, "shift_timing": "8am to 11am"},
        {"shift_id": "D1", "shift_duration": 3, "shift_timing": "11am to 2pm"},
        {"shift_id": "E1", "shift_duration": 3, "shift_timing": "2pm to 5pm"},
        {"shift_id": "E2", "shift_duration": 3, "shift_timing": "5pm to 8pm"},
        {"shift_id": "N1", "shift_duration": 3, "shift_timing": "8pm to 11pm"}
    ],
    "Day4": [
        {"shift_id": "M1", "shift_duration": 3, "shift_timing": "8am to 11am"},
        {"shift_id": "D1", "shift_duration": 3, "shift_timing": "11am to 2pm"},
        {"shift_id": "E1", "shift_duration": 3, "shift_timing": "2pm to 5pm"},
        {"shift_id": "E2", "shift_duration": 3, "shift_timing": "5pm to 8pm"},
        {"shift_id": "N1", "shift_duration": 3, "shift_timing": "8pm to 11pm"}
    ],
    "Day5": [
        {"shift_id": "M1", "shift_duration": 3, "shift_timing": "8am to 11am"},
        {"shift_id": "D1", "shift_duration": 3, "shift_timing": "11am to 2pm"},
        {"shift_id": "E1", "shift_duration": 3, "shift_timing": "2pm to 5pm"},
        {"shift_id": "E2", "shift_duration": 3, "shift_timing": "5pm to 8pm"},
        {"shift_id": "N1", "shift_duration": 3, "shift_timing": "8pm to 11pm"}
    ],
    "Day6": [
        {"shift_id": "M1", "shift_duration": 3, "shift_timing": "8am to 11am"},
        {"shift_id": "D1", "shift_duration": 3, "shift_timing": "11am to 2pm"},
        {"shift_id": "E1", "shift_duration": 3, "shift_timing": "2pm to 5pm"},
        {"shift_id": "E2", "shift_duration": 3, "shift_timing": "5pm to 8pm"},
        {"shift_id": "N1", "shift_duration": 3, "shift_timing": "8pm to 11pm"}
    ],
    "Day7": [
        {"shift_id": "M1", "shift_duration": 3, "shift_timing": "8am to 11am"},
        {"shift_id": "D1", "shift_duration": 3, "shift_timing": "11am to 2pm"},
        {"shift_id": "E1", "shift_duration": 3, "shift_timing": "2pm to 5pm"},
        {"shift_id": "E2", "shift_duration": 3, "shift_timing": "5pm to 8pm"},
        {"shift_id": "N1", "shift_duration": 3, "shift_timing": "8pm to 11pm"}
    ]
}

# defining MAX WORKING HOURS for each designation
MAX_WORKING_HOURS = {
    "Cashier": 36,
    "Inventory Manager": 28,
    "Customer Help": 42,
    "Cleaning Staff": 21,
    "Manager": 28,
    "Supervisor": 36
}

# Initialize the optimization model
model = LpProblem("Weekly_Shift_Schedule", LpMinimize)


# Function to get input counts
def get_employee_count_by_designation():
    designation_counts = {}
    for designation in MAX_WORKING_HOURS.keys():
        while True:
            try:
                count = int(
                    input(f"Enter the number of employees for {designation}: "))
                if count < 0:
                    print("Please enter a non-negative number.")
                else:
                    designation_counts[designation] = count
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    return designation_counts

# Random assignment logic

def assign_shifts_randomly(designation_counts, employees, shifts):
    schedule = {day: [] for day in shifts}
    for day, day_shifts in shifts.items():
        for shift in day_shifts:
            for designation, count in designation_counts.items():
                available_employees = [
                    e for e in employees if e["designation"] == designation]
                random.shuffle(available_employees)
                assigned_employees = available_employees[:count]
                for emp in assigned_employees:
                    # Check if the employee exceeds max hours
                    total_hours = emp["no_of_hours_worked"] + \
                        shift["shift_duration"]
                    if total_hours <= MAX_WORKING_HOURS[designation]:
                        emp["no_of_hours_worked"] += shift["shift_duration"]
                        schedule[day].append({
                            "e_id": emp["e_id"],
                            "e_name": emp["e_name"],
                            "designation": emp["designation"],
                            "shift_id": shift["shift_id"],
                            "shift_timing": shift["shift_timing"],
                        })
    return schedule


# Get employee counts from the user
designation_counts = get_employee_count_by_designation()

# Assign shifts based on input
schedule = assign_shifts_randomly(designation_counts, employees, shifts)

# Exporting the schedule to the required CSV format


def export_schedule_to_csv(schedule, output_file):
    # Create a dictionary to hold formatted data
    formatted_schedule = {"Employee ID": [], "Designation": []}

    # Add columns for each day
    for day in schedule.keys():
        formatted_schedule[day] = []

    # Fill the formatted data
    for employee in employees:
        formatted_schedule["Employee ID"].append(employee["e_id"])
        formatted_schedule["Designation"].append(employee["designation"])
        for day in schedule.keys():
            # Find the assigned shift for this employee and day
            assigned_shift = next(
                (entry["shift_id"] for entry in schedule[day]
                 if entry["e_id"] == employee["e_id"]),
                "Leave"
            )
            formatted_schedule[day].append(assigned_shift)

    # Convert to DataFrame and export to CSV
    df_formatted_schedule = pd.DataFrame(formatted_schedule)
    df_formatted_schedule.to_csv(output_file, index=False)
    print(f"Formatted schedule exported to {output_file}")


# Use the export function
output_file = "formatted_shift_schedule.csv"
export_schedule_to_csv(schedule, output_file)
