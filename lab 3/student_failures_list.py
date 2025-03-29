# ECOR 1042 Lab 3 - Individual submission for student_failures_list function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Cameron MacGillivray"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101354857"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-051"


# ==========================================#
# Place your student_failures_list function after this line
def student_failures_list(filename: str, failures: int) -> list:
    """
    Return a list of students, each of which is a dictionary with the given number of failures.
    If there is no student with the intended number of failures, returns an empty list.

    Modified from original submission to include assertions, try and except format.

    >>> student_failures_list('student-mat.csv', 0) # doctest: +ELLIPSIS
    [{'School': 'GP', 'ID': 1, 'Age': 18, 'StudyTime': 2.5, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6}, ...]

    >>> student_failures_list('student-mat.csv', 2) # doctest: +ELLIPSIS
    [{'School': 'GP', 'ID': 26, 'Age': 16, 'StudyTime': 1.5, 'Health': 5, 'Absences': 14, 'FallGrade': 6, 'WinterGrade': 9}, ...]

    >>> student_failures_list('student-mat.csv', 220)
    []
    """
    result_list = []  # The main list to be returned at the end of the function

    # Open the file and read entire file into a string using try/except to catch file errors
    try:
        file = open(filename, "r")
        dataString = file.read()
        file.close()
    except Exception as e:
        raise Exception("Error opening or reading the file: " + str(e))

    lines = dataString.splitlines()

    # Instead of checking if lines is empty with an if, we try to access the first element.
    try:
        header_line = lines[0].strip()
    except IndexError:
        return result_list  # Return an empty list if the file is empty

    headers = header_line.split(",")
    # Assert that headers exist
    assert len(headers) > 0, "Assertion failed: Header row is empty, no headers available."

    # Get the index of the 'Failures' column. If it does not exist, index() will throw a ValueError.
    try:
        failures_index = headers.index("Failures")
    except ValueError as e:
        raise Exception("Header 'Failures' not found in file: " + str(e))

    # Define converters for columns that need type conversion.
    converters = {
        "ID": int,
        "Age": int,
        "Health": int,
        "Absences": int,
        "FallGrade": int,
        "WinterGrade": int,
        "StudyTime": float,
    }

    # Process each data row starting from the second line
    for line in lines[1:]:
        # Use try/except to simulate "if line is empty" by attempting to access its first character.
        try:
            stripped_line = line.strip()
            _ = stripped_line[0]
        except IndexError:
            continue  # Skip this iteration if the line is empty

        values = stripped_line.split(",")

        # Convert the failures value to an integer
        try:
            current_failures = int(values[failures_index])
        except Exception as e:
            raise Exception("Error converting failures count to int: " + str(e))

        # Assert that the current row's failures matches the specified failures.
        try:
            assert current_failures == failures, (
                f"Assertion failed: Student row failure count {current_failures} does not equal specified {failures}."
            )
        except AssertionError:
            continue  # Skip rows that do not match the specified failure count

        student_dict = {}
        # Process each header/value pair without using if statements.
        for i, h in enumerate(headers):
            try:
                # Use an assertion to skip the 'Failures' column.
                assert h != "Failures", "Skipping column 'Failures'."
                try:
                    converter = converters[h]
                except KeyError:
                    converter = lambda x: x  # Default: leave value as string
                student_dict[h] = converter(values[i])
            except AssertionError:
                # Skip the 'Failures' column (assertion message indicates why)
                continue
        result_list.append(student_dict)

    return result_list