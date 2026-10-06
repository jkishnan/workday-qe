from utilities.log_parser import get_errors, get_warnings


LOG_FILE = "test_data/integration.log"


def test_detects_error_count():
    errors = get_errors(LOG_FILE)

    assert len(errors) == 2


def test_detects_warning_count():
    warnings = get_warnings(LOG_FILE)

    assert len(warnings) == 1


def test_detects_missing_employee_1472():
    errors = get_errors(LOG_FILE)

    assert any(
        "Employee 1472 missing" in error
        for error in errors
    )


def test_detects_missing_employee_1831():
    errors = get_errors(LOG_FILE)

    assert any(
        "Employee 1831 missing" in error
        for error in errors
    )


def test_detects_invalid_salary_warning():
    warnings = get_warnings(LOG_FILE)

    assert any(
        "Employee 1031 has invalid salary" in warning
        for warning in warnings
    )