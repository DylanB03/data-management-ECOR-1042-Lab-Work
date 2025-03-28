# ECOR 1042 Lab 5 - Individual submission for sort_students_failures_bubble function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Cameron MacGillivray"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101354857"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-051"

#==========================================#
# Place your sort_students_failures_bubble function after this line

def sort_students_failures_bubble(student: list[dict], order: str) -> str:
    """
    Sort a list of student dicts with a bubble sort algo for "Failures".

    >>> students = []
    >>> sort_students_failures_bubble(students, "A")
    'Empty list.'

    >>> students = [{"School": "GP"}, {"School": "MS"}]
    >>> sort_students_failures_bubble(students, "D")
    'List not sorted. Failures key not present.'

    >>> students = [{"Failures": 19, "School": "GP"}, {"Failures": 10, "School": "MS"}]
    >>> sort_students_failures_bubble(students, "A")
    'List sorted.'

    """
    if not student:
        return "Empty list."

    # Check if "Failures" key exists in the dictionaries.
    if "Failures" not in student[0]:
        return "List not sorted. Failures key not present."

    n = len(student)
    # Bubble sort algo
    for i in range(n):
        for j in range(0, n - i - 1):
            if order == "A":
                # For the ascending order, swap if the current element's Failures is greater than the next.
                if student[j]["Failures"] > student[j + 1]["Failures"]:
                    student[j], student[j + 1] = student[j + 1], student[j]
            elif order == "D":
                # For the descending order, swap if the current element's Failures less than the next.
                if student[j]["Failures"] < student[j + 1]["Failures"]:
                    student[j], student[j + 1] = student[j + 1], student[j]
            else: #Shouldn't be needed to pass
                pass
    return "List sorted."

# Do NOT include a main script in your submission
