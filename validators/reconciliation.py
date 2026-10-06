import csv
from collections import Counter


INPUT_FILE = "test_data/employees.csv"
OUTPUT_FILE = "test_data/employees_outbound.csv"


def load_employees(file_path):
    rows = []
    employees = {}
    employee_ids = []

    with open(file_path, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            rows.append(row)

            employee_id = row["employee_id"]

            if employee_id:
                employee_ids.append(employee_id)
                employees[employee_id] = row

    return rows, employees, employee_ids


input_rows, input_employees, input_ids = load_employees(INPUT_FILE)
output_rows, output_employees, output_ids = load_employees(OUTPUT_FILE)


print("------------------------------")
print("RECONCILIATION REPORT")
print("------------------------------")

print(f"Input physical records:  {len(input_rows)}")
print(f"Output physical records: {len(output_rows)}")

print(f"Input unique IDs:         {len(input_employees)}")
print(f"Output unique IDs:        {len(output_employees)}")


# -----------------------------------
# Find missing employee IDs
# -----------------------------------

missing_employees = (
    set(input_employees.keys())
    - set(output_employees.keys())
)

print("\nMISSING EMPLOYEES")

if missing_employees:
    for employee_id in sorted(missing_employees):
        print(f"Employee {employee_id}")
else:
    print("None")


# -----------------------------------
# Find unexpected employee IDs
# -----------------------------------

unexpected_employees = (
    set(output_employees.keys())
    - set(input_employees.keys())
)

print("\nUNEXPECTED EMPLOYEES")

if unexpected_employees:
    for employee_id in sorted(unexpected_employees):
        print(f"Employee {employee_id}")
else:
    print("None")


# -----------------------------------
# Find duplicate IDs
# -----------------------------------

print("\nDUPLICATE INPUT IDs")

input_id_counts = Counter(input_ids)

duplicate_input_ids = [
    employee_id
    for employee_id, count in input_id_counts.items()
    if count > 1
]

if duplicate_input_ids:
    for employee_id in duplicate_input_ids:
        print(
            f"Employee {employee_id} appears "
            f"{input_id_counts[employee_id]} times"
        )
else:
    print("None")
# -----------------------------------
# Find duplicate output IDs
# -----------------------------------

print("\nDUPLICATE OUTPUT IDs")

output_id_counts = Counter(output_ids)

duplicate_output_ids = [
    employee_id
    for employee_id, count in output_id_counts.items()
    if count > 1
]

if duplicate_output_ids:
    for employee_id in duplicate_output_ids:
        print(
            f"Employee {employee_id} appears "
            f"{output_id_counts[employee_id]} times"
        )
else:
    print("None")


# -----------------------------------
# Find field mismatches
# -----------------------------------

print("\nFIELD MISMATCHES")

mismatch_found = False

fields_to_compare = [
    "first_name",
    "last_name",
    "salary",
    "hire_date"
]

for employee_id in input_employees:

    if employee_id not in output_employees:
        continue

    input_employee = input_employees[employee_id]
    output_employee = output_employees[employee_id]

    for field in fields_to_compare:

        expected = input_employee[field]
        actual = output_employee[field]

        if expected != actual:
            mismatch_found = True

            print(f"\nEmployee: {employee_id}")
            print(f"Field:    {field}")
            print(f"Expected: {expected}")
            print(f"Actual:   {actual}")


if not mismatch_found:
    print("None")