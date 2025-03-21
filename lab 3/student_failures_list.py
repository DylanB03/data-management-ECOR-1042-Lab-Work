# ECOR 1042 Lab 3 - Individual submission for student_failures_list function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Cameron MacGillivray"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101354857"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-051"

#==========================================#
# Place your student_failures_list function after this line
def student_failures_list(filename: str, failures: int) -> list:
    """
    Return a list of students, each of which is a dictionary with the given number of failures.
    If there is no student with the intended number of failures, returns empty list.

    >>> student_failures_list('student-mat.csv', 0) # doctest: +ELLIPSIS
    [{'School': 'GP', 'ID': 1, 'Age': 18, 'StudyTime': 2.5, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6}, ...]

    >>> student_failures_list('student-mat.csv', 2) # doctest: +ELLIPSIS
    [{'School': 'GP', 'ID': 26, 'Age': 16, 'StudyTime': 1.5, 'Health': 5, 'Absences': 14, 'FallGrade': 6, 'WinterGrade': 9}, ...]

    >>> student_failures_list('student-mat.csv', 220)
    []
    """
    result_list = []    #the main list to be returned at end of function

    # open the file and read entire file into a string
    file = open(filename, "r")
    dataString = file.read()
    file.close()

    lines = dataString.splitlines()

    if not lines:
        return result_list  # return an empty list if file is empty

    header_line = lines[0].strip()
    headers = header_line.split(",")

    # reads all the next lines after the initial header, extracts the info
    for line in lines[1:]:
        line = line.strip()
        #skip empty line
        if not line:
            continue

        values = line.split(",")

        # find failures col pos = index
        failures_index = headers.index("Failures")

        #change them to ints
        current_failures = int(values[failures_index])

        # cont if row failures equivalent to intended function input param
        if current_failures == failures:
            #make a dictionary for this case
            student_dict = {}
            for i, h in enumerate(headers):
                if h == "Failures":
                    # Does not include failures column (handles ignore that redundant data)
                    continue
                if h in ["ID", "Age", "Health", "Absences",
                         "FallGrade", "WinterGrade"]:
                    student_dict[h] = int(values[i])
                elif h == "StudyTime":
                    student_dict[h] = float(values[i])
                else:
                    student_dict[h] = values[i]

            # Adds new student dictionary to the list of results
            result_list.append(student_dict)


    return result_list

"""def print_student_failures_blocks():
    for failures in range(4):  # iterates from 0 to 5
        print(f"Students with {failures} failure{'s' if failures != 1 else ''}:")
        student_list = student_failures_list("student-mat.csv", failures)
        for student in student_list:
            print(student)
        print()  # prints an empty line to separate blocks 

# Call the function
print_student_failures_blocks()

"""