import csv
import re
from datetime import datetime
from collections import Counter


FILE_PATH = "test_data/employees.csv"


def load_employees(file_path):
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        return list(reader)


def find_missing_employee_ids(employees):
    return [
        employee
        for employee in employees
        if not employee["employee_id"]
    ]


def find_duplicate_employee_ids(employees):
    employee_ids = [
        employee["employee_id"]
        for employee in employees
        if employee["employee_id"]
    ]

    counts = Counter(employee_ids)

    return [
        employee_id
        for employee_id, count in counts.items()
        if count > 1
    ]


def find_invalid_salaries(employees):
    invalid_salaries = []

    for employee in employees:
        try:
            float(employee["salary"])
        except ValueError:
            invalid_salaries.append(employee)

    return invalid_salaries


def find_missing_first_names(employees):
    return [
        employee
        for employee in employees
        if not employee["first_name"]
    ]


def find_long_first_names(employees):
    return [
        employee
        for employee in employees
        if len(employee["first_name"]) > 100
    ]


def find_invalid_last_names(employees):
    invalid_last_names = []

    for employee in employees:
        last_name = employee["last_name"]

        if last_name and not re.fullmatch(
            r"[A-Za-z0-9'\- ]+",
            last_name
        ):
            invalid_last_names.append(employee)

    return invalid_last_names


def find_invalid_hire_dates(employees):
    invalid_dates = []

    for employee in employees:
        try:
            datetime.strptime(
                employee["hire_date"],
                "%Y-%m-%d"
            )
        except ValueError:
            invalid_dates.append(employee)

    return invalid_dates


if __name__ == "__main__":
    employees = load_employees(FILE_PATH)

    print("------------------------------")
    print("FILE VALIDATION REPORT")
    print("------------------------------")

    print(
        f"Missing employee IDs: "
        f"{len(find_missing_employee_ids(employees))}"
    )

    print(
        f"Duplicate employee IDs: "
        f"{find_duplicate_employee_ids(employees)}"
    )

    print(
        f"Invalid salaries: "
        f"{len(find_invalid_salaries(employees))}"
    )

    print(
        f"Missing first names: "
        f"{len(find_missing_first_names(employees))}"
    )

    print(
        f"Long first names: "
        f"{len(find_long_first_names(employees))}"
    )

    print(
        f"Invalid last names: "
        f"{len(find_invalid_last_names(employees))}"
    )

    print(
        f"Invalid hire dates: "
        f"{len(find_invalid_hire_dates(employees))}"
    )