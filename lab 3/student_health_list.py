# ECOR 1042 Lab 3 - Individual submission for student_health_list function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Chloe Ouellette"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101337142"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-051"

# ==========================================#
# Place your student_health_list function after this line


def student_health_list(filename: str, health: int) -> list[dict]:
    """Return a list of students, stored as dictionaries, whose health values are equivalent to health, given a csv file. Each dictionary contains a student's school, ID, age, study time, failures, absenses, fall grades and winter grades.
    Preconditions: 1 <= health <= 5.
    >>> student_health_list('student-mat.csv', 2)
    [ {'School': 'MS', 'ID': 20, 'Age': 20, 'StudyTime': 1.0, 'Failures': 1,'Absences': 10, 'FallGrade': 9, 'WinterGrade': 11},{another element}, …]
    >>> student_health_list('student-mat.csv', 'health')
    []
    >>> student_health_list('student-mat.csv', 5)
    [ {'School': 'GP', 'ID': 4, 'Age': 15, 'StudyTime': 3.0, 'Failures': 0,'Absences': 2, 'FallGrade': 15, 'WinterGrade': 14},{another element}, …]
    """
    data_str = ""
    with open(filename, "r") as file:
        for ch in file:
            data_str += ch

    data_str = data_str.splitlines()
    category = data_str[0].split(',')
    students = []
    health_index = category.index('Health')
    del category[health_index]

    for student in data_str:
        student = student.split(',')
        if student[health_index] == str(health):
            del student[health_index]
            student_dict = {}
            for x in range(len(student)):
                if student[x].isdigit():
                    student_dict[category[x]] = int(student[x])
                else:
                    try:
                        student_dict[category[x]] = float(student[x])
                    except:
                        student_dict[category[x]] = student[x]
            students += [student_dict]

    return students

# Do NOT include a main script in your submission
