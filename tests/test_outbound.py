import csv
from collections import Counter


INPUT_FILE = "test_data/employees.csv"
OUTPUT_FILE = "test_data/employees_outbound.csv"


def load_employees(file_path):
    with open(file_path, "r") as file:
        return list(csv.DictReader(file))


input_employees = load_employees(INPUT_FILE)
output_employees = load_employees(OUTPUT_FILE)


def get_valid_ids(employees):
    return [
        employee["employee_id"]
        for employee in employees
        if employee["employee_id"]
    ]


def test_outbound_record_count():
    assert len(output_employees) == 1000


def test_detects_missing_employees():
    input_ids = set(get_valid_ids(input_employees))
    output_ids = set(get_valid_ids(output_employees))

    missing_ids = input_ids - output_ids

    assert missing_ids == {"1472", "1831"}


def test_detects_unexpected_employee():
    input_ids = set(get_valid_ids(input_employees))
    output_ids = set(get_valid_ids(output_employees))

    unexpected_ids = output_ids - input_ids

    assert unexpected_ids == {"9999"}


def test_detects_output_duplicates():
    output_ids = get_valid_ids(output_employees)
    counts = Counter(output_ids)

    duplicates = {
        employee_id
        for employee_id, count in counts.items()
        if count > 1
    }

    assert duplicates == {"1020", "1550"}


def test_detects_salary_mismatch():
    input_by_id = {
        employee["employee_id"]: employee
        for employee in input_employees
        if employee["employee_id"]
    }

    output_by_id = {
        employee["employee_id"]: employee
        for employee in output_employees
        if employee["employee_id"]
    }

    salary_mismatches = []

    for employee_id in input_by_id:
        if employee_id not in output_by_id:
            continue

        if (
            input_by_id[employee_id]["salary"]
            != output_by_id[employee_id]["salary"]
        ):
            salary_mismatches.append(employee_id)

    assert salary_mismatches == ["1291"]