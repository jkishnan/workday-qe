import csv
import copy


INPUT_FILE = "test_data/employees.csv"
OUTPUT_FILE = "test_data/employees_outbound.csv"


# Read inbound employee data
employees = []

with open(INPUT_FILE, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        employees.append(row)


# Create a separate copy for outbound processing
outbound_employees = copy.deepcopy(employees)


# -----------------------------------
# Simulate integration problems
# -----------------------------------

# 1. Remove employee 1472
outbound_employees = [
    employee
    for employee in outbound_employees
    if employee["employee_id"] != "1472"
]

# 2. Remove employee 1831
outbound_employees = [
    employee
    for employee in outbound_employees
    if employee["employee_id"] != "1831"
]


# 3. Change salary for employee 1291
for employee in outbound_employees:
    if employee["employee_id"] == "1291":
        employee["salary"] = "102000"
# 4. Create duplicate employee 1550
for employee in outbound_employees:
    if employee["employee_id"] == "1550":
        duplicate_employee = copy.deepcopy(employee)
        outbound_employees.append(duplicate_employee)
        break


# 5. Add unexpected employee
unexpected_employee = {
    "employee_id": "9999",
    "first_name": "Unexpected",
    "last_name": "Employee",
    "salary": "75000",
    "hire_date": "2025-01-15"
}

outbound_employees.append(unexpected_employee)


# Write outbound file
with open(OUTPUT_FILE, "w", newline="") as file:
    fieldnames = [
        "employee_id",
        "first_name",
        "last_name",
        "salary",
        "hire_date"
    ]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()
    writer.writerows(outbound_employees)


print("------------------------------")
print("OUTBOUND FILE GENERATED")
print("------------------------------")
print(f"Input records:  {len(employees)}")
print(f"Output records: {len(outbound_employees)}")
print("Simulated missing employees: 1472, 1831")
print("Simulated salary change: 1291")