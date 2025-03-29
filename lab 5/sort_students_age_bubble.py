# ECOR 1042 Lab 5 - Individual submission for sort_students_age_bubble

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Arman Rahmani"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101333091"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-051"

#==========================================#
# Place your sort_students_age_bubble function after this line

def sort_students_age_bubble(students: list[dict], rank: str) -> str:
    """ 
    Returns a string of a list of students' dictionaries, bubble sorted in ascending or descending order based off age. If the inputted list is empty, the function returns the string “Empty list.”. If “Age” is not a key in the dictionary, the function returns the string “List not sorted. Age key not present.”.
    
    >>> a = []
    >>> sort_students_age_bubble(a, "A")
    'Empty list.'
    
    >>> a = [{"Age":15,"School":"GP"},{"Age":19,"School":"GP"}]
    >>> sort_students_age_bubble(a, "D")
    'List sorted.'
    
    >>> a = [{"StudyTime":20}, {"Studytime":12}]
    >>> sort_students_age_bubble(a, "D")
    'List not sorted. Age key not present.'
    """
    
    if not students:
        return "Empty list."

    if not all("Age" in student for student in students):
        return "List not sorted. Age key not present."

    if rank == "A":
        for i in range(len(students)):
            for j in range(len(students) - i - 1):
                if students[j]["Age"] > students[j + 1]["Age"]:
                    students[j], students[j + 1] = students[j + 1], students[j]

    elif rank == "D":      
        for i in range(len(students)):
            for j in range(len(students)- i - 1):
                if students[j]["Age"] < students[j + 1]["Age"]:
                    students[j], students[j + 1] = students[j + 1], students[j]

    return "List sorted."

# Do NOT include a main script in your submission
