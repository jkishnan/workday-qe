LOG_FILE = "test_data/integration.log"


def get_log_entries(file_path, level):
    entries = []

    with open(file_path, "r") as file:
        for line in file:
            if f" {level} " in line:
                entries.append(line.strip())

    return entries


def get_errors(file_path):
    return get_log_entries(file_path, "ERROR")


def get_warnings(file_path):
    return get_log_entries(file_path, "WARNING")


if __name__ == "__main__":
    errors = get_errors(LOG_FILE)
    warnings = get_warnings(LOG_FILE)

    print("------------------------------")
    print("LOG VALIDATION REPORT")
    print("------------------------------")
    print(f"Errors:   {len(errors)}")
    print(f"Warnings: {len(warnings)}")

    for error in errors:
        print(error)

    for warning in warnings:
        print(warning)