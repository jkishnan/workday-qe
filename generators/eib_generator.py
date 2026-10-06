import csv
import random
from datetime import date, timedelta

employees = []

for i in range(1000):
    employee = {
        "employee_id": str(1001 + i),
        "first_name": f"Employee{i + 1}",
        "last_name": f"Test{i + 1}",
        "salary": random.randint(50000, 150000),
        "hire_date": str(date.today() - timedelta(days=random.randint(1, 2000)))
    }

    employees.append(employee)


# -----------------------------------
# Inject intentionally bad test data
# -----------------------------------

# 1. Missing employee ID
employees[10]["employee_id"] = ""

# 2. Duplicate employee ID
employees[20]["employee_id"] = employees[19]["employee_id"]

# 3. Invalid salary
employees[30]["salary"] = "ABC"

# 4. Missing required first name
employees[40]["first_name"] = ""

# 5. Special characters in last name
employees[50]["last_name"] = "@#$%^&*"

# 6. Extremely long first name
employees[60]["first_name"] = "A" * 300

# 7. Incorrect date format
employees[70]["hire_date"] = "31/15/2025"

employees[10]["employee_id"] = ""


with open("test_data/employees.csv", "w", newline="") as file:
    fieldnames = [
        "employee_id",
        "first_name",
        "last_name",
        "salary",
        "hire_date"
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(employees)


print(f"Generated {len(employees)} employee records.")
print("Negative test data injected successfully.")