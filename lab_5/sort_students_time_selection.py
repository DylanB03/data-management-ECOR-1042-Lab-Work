# ECOR 1042 Lab 5 - Individual submission for sort_students_time_selection function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Chloe Ouellette"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101337142"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-051"

#==========================================#
# Place your sort_students_time_selection function after this line
def sort_students_time_selection(students: list[dict], order: str) -> str:
    """
    Return a string stating whether the dictionaries in students have been sorted. The list will be sorted based on whether "A" (for ascending) or "D" (for descending) was typed as a value for order. 
    >>> a = []
    >>> sort_students_time_selection(a, "A")
    < a is not modified >
    'Empty list.'

    >>> a = [{"StudyTime":10, "School":"GP"}, {"StudyTime":19, "School":"MS"}]
    >>> sort_students_time_selection(a, "D")
    < a is now sorted: a = [{"StudyTime":19, "School":"MS"}, {"StudyTime":10, "School":"GP"}]
    'List sorted.'

    >>> a = [{"School":"GP"}, {"School":"MS"}]
    >>> sort_students_time_selection (a, "D")
    <a is not modified>
    List not sorted. StudyTime key not present.
    """
    if students == []:
        return 'Empty list.'
    else:
        for student in students:
            if order == "A" and "StudyTime" in student.keys():
                for i in range(len(students)):
                    min_index = i
                    for j in range(i + 1, len(students)):
                        if students[min_index]['StudyTime'] > students[j]['StudyTime']:
                            min_index = j
                    students[i], students[min_index] = students[min_index], students[i]
                return 'List sorted.'
            elif order == "D" and "StudyTime" in student.keys():
                for i in range(len(students)):
                    max_index = i
                    for j in range(i + 1, len(students)):
                        if students[max_index]['StudyTime'] < students[j]['StudyTime']:
                            max_index = j
                    students[i], students[max_index] = students[max_index], students[i]
                return 'List sorted.'
            else:
                return "List not sorted. StudyTime key not present."


# Do NOT include a main script in your submission
