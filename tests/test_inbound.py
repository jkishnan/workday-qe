from validators.file_validator import (
    load_employees,
    find_missing_employee_ids,
    find_duplicate_employee_ids,
    find_invalid_salaries,
    find_missing_first_names,
    find_long_first_names,
    find_invalid_last_names,
    find_invalid_hire_dates,
)


INPUT_FILE = "test_data/employees.csv"

employees = load_employees(INPUT_FILE)


def test_employee_record_count():
    assert len(employees) == 1000


def test_detects_missing_employee_id():
    missing_ids = find_missing_employee_ids(employees)

    assert len(missing_ids) == 1


def test_detects_duplicate_employee_id():
    duplicates = find_duplicate_employee_ids(employees)

    assert duplicates == ["1020"]


def test_detects_invalid_salary():
    invalid_salaries = find_invalid_salaries(employees)

    assert len(invalid_salaries) == 1
    assert invalid_salaries[0]["employee_id"] == "1031"
    assert invalid_salaries[0]["salary"] == "ABC"


def test_detects_missing_first_name():
    missing_names = find_missing_first_names(employees)

    assert len(missing_names) == 1
    assert missing_names[0]["employee_id"] == "1041"


def test_detects_long_first_name():
    long_names = find_long_first_names(employees)

    assert len(long_names) == 1
    assert long_names[0]["employee_id"] == "1061"


def test_detects_invalid_last_name():
    invalid_names = find_invalid_last_names(employees)

    assert len(invalid_names) == 1
    assert invalid_names[0]["employee_id"] == "1051"


def test_detects_invalid_hire_date():
    invalid_dates = find_invalid_hire_dates(employees)

    assert len(invalid_dates) == 1
    assert invalid_dates[0]["employee_id"] == "1071"