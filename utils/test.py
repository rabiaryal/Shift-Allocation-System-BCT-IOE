import pandas as pd

# Load the Excel file
file_path = "D:\\minnor05\SAS\\Updated_Schedule.xlsx"  # Update with your actual file path
df = pd.read_excel(file_path)

# Extract relevant columns (Designation and Shift columns)
days = [col for col in df.columns if col.startswith("Day")]  # Identifying day columns
designation_counts = {}

# Iterate over each day
for day in days:
    shift_data = df[[day, "Designation"]].dropna()  # Extract shift and designation info

    shift_count = {}  # Dictionary to store shift-wise designation count

    # Process each row
    for _, row in shift_data.iterrows():
        shifts = row[day].split(", ")  # Split multiple shifts (e.g., "Morning, Day")
        designation = row["Designation"]

        for shift in shifts:
            shift_count.setdefault(shift, {}).setdefault(designation, 0)
            shift_count[shift][designation] += 1

    designation_counts[day] = shift_count

# Print the shift allocation count
for day, shifts in designation_counts.items():
    print(f"\n### {day} Shift Allocation ###")
    for shift, designations in shifts.items():
        print(f"\n  {shift} Shift:")
        for designation, count in designations.items():
            print(f"    - {designation}: {count}")

