# Workday Integration QE Automation Project

A Python-based Quality Engineering automation project that simulates testing of Workday-style employee integrations.

The project demonstrates automated validation of inbound employee data, outbound integration files, REST APIs, integration logs, and source-to-target reconciliation.

## Technologies

- Python
- Pytest
- Requests
- CSV
- REST APIs
- Git

## Project Structure

```text
workday-qe/
├── generators/
│   ├── eib_generator.py
│   └── outbound_generator.py
├── validators/
│   ├── file_validator.py
│   ├── reconciliation.py
│   └── api_validator.py
├── utilities/
│   └── log_parser.py
├── test_data/
│   ├── employees.csv
│   ├── employees_outbound.csv
│   └── integration.log
├── tests/
│   ├── test_inbound.py
│   ├── test_outbound.py
│   ├── test_api.py
│   └── test_logs.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Test Scenarios

### Inbound Data Validation

Validates employee input data including:

- Record count
- Missing employee IDs
- Duplicate employee IDs
- Invalid salaries
- Missing required names
- Field length validation
- Invalid characters
- Invalid date formats

### Outbound Reconciliation

Compares source and outbound employee data to detect:

- Missing employees
- Unexpected employees
- Duplicate records
- Salary mismatches
- Record-count differences

This demonstrates why record-count validation alone is not sufficient for integration testing.

### REST API Validation

Uses a public test REST API to validate:

- HTTP status codes
- JSON response payloads
- Required fields
- Expected employee/user ID
- Negative 404 scenarios

### Log Validation

Parses integration logs and validates:

- ERROR entries
- WARNING entries
- Missing employee errors
- Invalid salary warnings

## Negative Testing

The test-data generator deliberately injects invalid records, including:

- Missing employee ID
- Duplicate employee ID
- Non-numeric salary
- Missing first name
- Invalid last-name characters
- Excessively long first name
- Invalid hire date

The automated tests verify that the validation framework correctly detects these conditions.

## Running the Tests

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the complete test suite:

```bash
python -m pytest tests/ -v
```

Run a concise test report:

```bash
python -m pytest tests/ -q
```

## Current Test Results

```text
22 passed
```

The framework currently contains automated coverage for inbound validation, outbound reconciliation, REST API testing, negative testing, and integration-log validation.

## QE Approach

The project follows an end-to-end integration testing approach:

```text
Generate Test Data
        ↓
Validate Inbound Data
        ↓
Simulate Outbound Integration
        ↓
Reconcile Source and Target
        ↓
Validate REST API
        ↓
Validate Integration Logs
        ↓
Execute Automated Pytest Suite
```

The goal is to validate not only whether an integration job completes, but whether the correct data is processed and delivered without missing, duplicate, unexpected, or incorrectly transformed records.