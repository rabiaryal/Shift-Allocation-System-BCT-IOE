import pandas as pd
import random

# ----- Helper Function to Assign Duty Off -----
def assign_duty_off(e_id):
    mod = e_id % 7
    return f"Day{mod if mod != 0 else 7}"

# ----- Input Mode: Manual or Auto-Generate Employees -----
use_manual_input = True  # Set to False to auto-generate employees

if use_manual_input:
    # Manually provided employees list
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
        }
    ]
else:
    # Auto-generate employees (example for 40 employees)
    designations = ["Cashier", "Inventory Manager", "Customer Help", "Cleaning Staff", "Manager", "Supervisor"]
    employees = []
    num_employees = 40
    for i in range(1, num_employees + 1):
        designation = designations[(i - 1) % len(designations)]
        employee = {
            "e_id": i,
            "e_name": f"Employee {i}",
            "no_of_hours_worked": 0,
            "designation": designation,
            "e_gmail": f"employee{i}@example.com",
            "e_priority": random.randint(7, 10)
        }
        employees.append(employee)

# ----- Normalize Employee Data -----
# Ensure that each employee has 'duty_off', 'assigned_shifts', and 'overtime_hours_worked'
for emp in employees:
    if "duty_off" not in emp:
        emp["duty_off"] = assign_duty_off(emp["e_id"])
    if "assigned_shifts" not in emp:
        emp["assigned_shifts"] = []
    if "overtime_hours_worked" not in emp:
        emp["overtime_hours_worked"] = 0

# ----- Shifts Definition -----
# Updated Shifts: Three shifts per day (8 hours each)
shifts = {
    "Day1": [
        {"shift_id": "Morning", "shift_duration": 8, "shift_timing": "6am to 2pm"},
        {"shift_id": "Day",     "shift_duration": 8, "shift_timing": "2pm to 10pm"},
        {"shift_id": "Night",   "shift_duration": 8, "shift_timing": "10pm to 6am"}
    ],
    "Day2": [
        {"shift_id": "Morning", "shift_duration": 8, "shift_timing": "6am to 2pm"},
        {"shift_id": "Day",     "shift_duration": 8, "shift_timing": "2pm to 10pm"},
        {"shift_id": "Night",   "shift_duration": 8, "shift_timing": "10pm to 6am"}
    ],
    "Day3": [
        {"shift_id": "Morning", "shift_duration": 8, "shift_timing": "6am to 2pm"},
        {"shift_id": "Day",     "shift_duration": 8, "shift_timing": "2pm to 10pm"},
        {"shift_id": "Night",   "shift_duration": 8, "shift_timing": "10pm to 6am"}
    ],
    "Day4": [
        {"shift_id": "Morning", "shift_duration": 8, "shift_timing": "6am to 2pm"},
        {"shift_id": "Day",     "shift_duration": 8, "shift_timing": "2pm to 10pm"},
        {"shift_id": "Night",   "shift_duration": 8, "shift_timing": "10pm to 6am"}
    ],
    "Day5": [
        {"shift_id": "Morning", "shift_duration": 8, "shift_timing": "6am to 2pm"},
        {"shift_id": "Day",     "shift_duration": 8, "shift_timing": "2pm to 10pm"},
        {"shift_id": "Night",   "shift_duration": 8, "shift_timing": "10pm to 6am"}
    ],
    "Day6": [
        {"shift_id": "Morning", "shift_duration": 8, "shift_timing": "6am to 2pm"},
        {"shift_id": "Day",     "shift_duration": 8, "shift_timing": "2pm to 10pm"},
        {"shift_id": "Night",   "shift_duration": 8, "shift_timing": "10pm to 6am"}
    ],
    "Day7": [
        {"shift_id": "Morning", "shift_duration": 8, "shift_timing": "6am to 2pm"},
        {"shift_id": "Day",     "shift_duration": 8, "shift_timing": "2pm to 10pm"},
        {"shift_id": "Night",   "shift_duration": 8, "shift_timing": "10pm to 6am"}
    ]
}

# ----- Scheduling Parameters -----
MAX_WORKING_HOURS = {
    "Cashier": 40,
    "Inventory Manager": 35,
    "Customer Help": 42,
    "Cleaning Staff": 28,
    "Manager": 35,
    "Supervisor": 40
}

MAX_OVERTIME_HOURS = {
    "Cashier": 16,
    "Inventory Manager": 16,
    "Customer Help": 16,
    "Cleaning Staff": 16,
    "Manager": 16,
    "Supervisor": 16
}

allowed_shifts_per_day = {
    "Cashier": 1,
    "Inventory Manager": 1,
    "Customer Help": 1,
    "Cleaning Staff": 1,
    "Manager": 1,
    "Supervisor": 1
}

# In this example, the keys in required_employees_config must match a shift_id.
required_employees_config = {
    "Cashier": {"Morning": 2, "Day": 2, "Night": 1},
    "Inventory Manager": {"Morning": 1, "Day": 0, "Night": 0},
    "Customer Help": {"Morning": 1, "Day": 2, "Night": 1},
    "Cleaning Staff": {"Morning": 1, "Day": 1, "Night": 0},
    "Manager": {"Morning": 1, "Day": 1, "Night": 0},
    "Supervisor": {"Morning": 0, "Day": 1, "Night": 1}
}

# ----- Custom Group Colors for Excel Row Grouping -----
group_colors_input = {
    "Cashier": "#ADD8E6",            # Light Blue
    "Inventory Manager": "#90EE90",  # Light Green
    "Customer Help": "#FFFFE0",       # Light Yellow
    "Cleaning Staff": "#FFDAB9",      # Light Peach
    "Manager": "#D3D3D3",             # Light Gray
    "Supervisor": "#FFB6C1"           # Light Pink
}

# For grouping in the Excel output, define the desired order of designations.
designations_order = ["Cashier", "Inventory Manager", "Customer Help", "Cleaning Staff", "Manager", "Supervisor"]

# ----- Helper Function: Determine Eligible Employees (Regular and/or Overtime) -----
def get_available_employees(designation, shift_duration, day):
    """
    Returns a list of eligible employees for the given designation who can work
    an additional shift of the given duration on the specified day.
    Eligibility criteria:
      - Skip if the day is the employee's duty off.
      - The number of shifts already assigned for that day is less than the allowed limit.
      - The employee can take the shift as regular hours OR as overtime.
    The list is sorted by priority (descending) and then by total assigned hours (regular + overtime, ascending).
    """
    eligible = []
    for emp in employees:
        if emp["designation"] != designation:
            continue

        # Skip if today is the employee's duty off.
        if day == emp.get("duty_off"):
            continue

        # Check allowed shifts per day.
        assigned_today = sum(1 for shift in emp["assigned_shifts"] if shift["day"] == day)
        if assigned_today >= allowed_shifts_per_day.get(designation, 0):
            continue

        # Check eligibility for regular hours.
        can_regular = emp["no_of_hours_worked"] + shift_duration <= MAX_WORKING_HOURS.get(designation, 0)
        # Check eligibility for overtime.
        can_overtime = emp["overtime_hours_worked"] + shift_duration <= MAX_OVERTIME_HOURS.get(designation, 0)

        if can_regular or can_overtime:
            total_hours = emp["no_of_hours_worked"] + emp["overtime_hours_worked"]
            emp['_total_hours'] = total_hours
            eligible.append(emp)
    eligible.sort(key=lambda x: (-x["e_priority"], x["_total_hours"]))
    for emp in eligible:
        del emp['_total_hours']
    return eligible

# ----- Shift Allocation Algorithm with Overtime Support -----
for day, day_shifts in shifts.items():
    for shift in day_shifts:
        shift_id = shift["shift_id"]
        shift_duration = shift["shift_duration"]
        shift_timing = shift["shift_timing"]

        for designation, config in required_employees_config.items():
            required_count = config.get(shift_id, 0)
            if required_count == 0:
                continue  # Skip if none required.

            eligible_emps = get_available_employees(designation, shift_duration, day)
            if len(eligible_emps) < required_count:
                print(f"[ERROR] On {day} shift {shift_id} ({shift_timing}) for '{designation}': "
                      f"Required {required_count}, but found only {len(eligible_emps)} eligible employees.")
            else:
                selected_emps = eligible_emps[:required_count]
                for emp in selected_emps:
                    # Determine if the shift is assigned as regular or overtime.
                    if emp["no_of_hours_worked"] + shift_duration <= MAX_WORKING_HOURS[designation]:
                        emp["no_of_hours_worked"] += shift_duration
                        assign_mode = "Regular"
                    elif emp["overtime_hours_worked"] + shift_duration <= MAX_OVERTIME_HOURS[designation]:
                        emp["overtime_hours_worked"] += shift_duration
                        assign_mode = "Overtime"
                    else:
                        assign_mode = "Unassigned"  # This should not occur.

                    emp["assigned_shifts"].append({
                        "day": day,
                        "shift_id": shift_id,
                        "shift_timing": shift_timing,
                        "shift_duration": shift_duration,
                        "assignment_mode": assign_mode
                    })

# ----- Build Aggregated Report -----
# For each day, if it matches an employee's duty off, we mark it as "Leave"; otherwise, "NE" for No Entry.
days = [f"Day{i}" for i in range(1, 8)]
report_rows = []
for emp in employees:
    row = {
        "Employee ID": emp["e_id"],
        "Employee Name": emp["e_name"],
        "Department": "ND",  # Not provided.
        "Position": emp["designation"]
    }
    # Prepare a dictionary to collect shift info for each day.
    day_shifts_collected = {day: [] for day in days}
    for assign in emp.get("assigned_shifts", []):
        # Annotate with (R) for Regular or (O) for Overtime.
        shift_label = f"{assign['shift_id']} ({assign['assignment_mode'][0]})"
        day_shifts_collected[assign["day"]].append(shift_label)
    for day in days:
        # If today is the employee's duty off, mark as "Leave"; otherwise, if no shift assigned, mark as "NE".
        if day == emp.get("duty_off"):
            row[day] = "Leave"
        else:
            row[day] = ", ".join(day_shifts_collected[day]) if day_shifts_collected[day] else "NE"
    row["Regular Hours"] = emp["no_of_hours_worked"]
    row["Overtime Hours"] = emp.get("overtime_hours_worked", 0)
    row["Total Working Hours"] = row["Regular Hours"] + row["Overtime Hours"]
    report_rows.append(row)

df_report = pd.DataFrame(report_rows, columns=[
    "Employee ID", "Employee Name", "Department", "Position",
    "Day1", "Day2", "Day3", "Day4", "Day5", "Day6", "Day7",
    "Regular Hours", "Overtime Hours", "Total Working Hours"
])

# ----- Write Excel Report with Enhanced Formatting -----
excel_filename = "shift_assignments_report.xlsx"
with pd.ExcelWriter(excel_filename, engine="xlsxwriter") as writer:
    workbook = writer.book
    worksheet = workbook.add_worksheet("Report")
    writer.sheets["Report"] = worksheet

    # Freeze the header row.
    worksheet.freeze_panes(1, 0)

    # Define distinct header colors.
    header_colors = [
        "#FFC7CE", "#C6EFCE", "#FFEB9C", "#9CC3E6",
        "#F4B084", "#B6D7A8", "#A4C2F4", "#D9D2E9",
        "#C9DAF8", "#FFE699", "#D9D2E9", "#B4C7E7", "#D9D2E9"
    ]

    header = df_report.columns.tolist()
    # Write header row.
    for col_num, col_name in enumerate(header):
        header_format = workbook.add_format({
            'bold': True,
            'bg_color': header_colors[col_num % len(header_colors)],
            'border': 1,
            'align': 'center',
            'valign': 'vcenter'
        })
        worksheet.write(0, col_num, col_name, header_format)
        worksheet.set_column(col_num, col_num, 15)

    data_format = workbook.add_format({'border': 1, 'align': 'center', 'valign': 'vcenter'})

    current_row = 1
    # Group rows by designation using the explicitly defined order.
    for group in designations_order:
        group_df = df_report[df_report["Position"] == group]
        if not group_df.empty:
            if current_row > 1:
                current_row += 1  # Add a blank row between groups.
            group_format = workbook.add_format({
                'bg_color': group_colors_input.get(group, "#FFFFFF"),
                'border': 1,
                'align': 'center',
                'valign': 'vcenter'
            })
            for _, row in group_df.iterrows():
                for col_num, value in enumerate(row):
                    worksheet.write(current_row, col_num, value, group_format)
                current_row += 1

    # ----- Conditional Formatting for "Leave" and "NE" in Day Columns -----
    # Define formats for "Leave" and "NE"
    leave_format = workbook.add_format({'bg_color': '#FFFF00'})  # Light green for Leave
    ne_format = workbook.add_format({'bg_color': '#FFA500'})     # Light red for NE

    last_row = current_row - 1  # Last written row index
    # The Day columns are from "Day1" (column index 4) to "Day7" (column index 10)
    for col in range(4, 11):
        worksheet.conditional_format(1, col, last_row, col, {
            'type': 'cell',
            'criteria': '==',
            'value': '"Leave"',
            'format': leave_format
        })
        worksheet.conditional_format(1, col, last_row, col, {
            'type': 'cell',
            'criteria': '==',
            'value': '"NE"',
            'format': ne_format
        })

    # Write the workbook
    writer.close()

print(f"Shift assignment completed. Excel workbook generated: {excel_filename}")
