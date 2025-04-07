# ECOR 1042 Lab 5 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Dylan Butz, Chloe Ouellette, Cameron MacGillivray, Arman Rahmani"

# Update "" with your team (e.g. T102)
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

#==========================================#
# Place your sort_students_time_selection function after this line
def sort_students_time_selection(students: list[dict], order: str) -> str:
    """
    Return a string stating whether the dictionaries in students have been sorted by study time. The list will be sorted based on whether "A" (for ascending) or "D" (for descending) was typed as a value for order. "Empty list" will be returned if the list is empty. List will not be sorted if StudyTime is not a key in the dictionary and "List not sorted. StudyTime key not present."
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

#==========================================#
# Place your sort_students_avg_insertion function after this line

def sort_students_avg_insertion(students: list, rank: str) -> str:
    """
    Sorts a given list containing dicts based on average grades using insertion sort.
    Implements ascending insertion sort if rank is "A" and descending insertion sort if rank is "D".

    >>> sort_students_avg_insertion([], "D")
    "Empty list."
    >>> sort_students_avg_insertion([{"AvgGrade": 7.2, "School": "GP"}, {"AvgGrade": 9.1, "School": "MS"}], "D")
    "List sorted."
    >>> sort_students_avg_insertion([{"School": "GP"}, {"School": "MS"}], "D")
    "List not sorted. AvgGrade key not present."
    """
    if not students:
        return "Empty list."
    try:
        # Insertion sort directly for the chosen order
        for i in range(1, len(students)):
            key_item = students[i]
            key_value = key_item["AvgGrade"]
            j = i - 1
            if rank == "A":
                while j >= 0 and students[j]["AvgGrade"] > key_value:
                    students[j + 1] = students[j]
                    j -= 1
            elif rank == "D":
                while j >= 0 and students[j]["AvgGrade"] < key_value:
                    students[j + 1] = students[j]
                    j -= 1
            else:
                return "Invalid order."
            students[j + 1] = key_item
        return "List sorted."
    except KeyError:
        return "List not sorted. AvgGrade key not present."


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

#==========================================#
# Place your sort function after this line
def sort(students: list[dict], order: str, attribute: str) -> str:
    """
    Return a string stating whether or not the list of dictionaries students has been sorted in the order specified (either "A" for ascending or "D" for descending). They will be sorted according to the attribute, so either by "Age", "StudyTime", "AvgGrade" or "Failures". If an empty list is inserted, "Empty list." will be returned. If an invalid attribute is inputted, "Invalid input, the list cannot be sorted by attribute." will be returned.
    >>> a = []
    >>> sort(a, "D", "Age")
    <a is not modified>
    Empty list.
    
    >>> a = [{"School":"GP"},{"School":"MS"}]
    >>>sort(a, "D", "School")
    <a is not modified>
    Invalid input, the list cannot be sorted by School.
    
    >>> a = [{"Age":15,"School":"GP"},{"Age":19,"School":"GP"}]
    >>>sort(a, "D", "School")
    <a is not modified>
    List sorted.
    """
    if attribute not in ["Age", "StudyTime", "AvgGrade", "Failures"]:
        return "Invalid input, the list cannot be sorted by " + attribute + "."
    elif not students:
        return "Empty list."
    else:
        if attribute == "Age":
            return sort_students_age_bubble(students, order)
        elif attribute == "StudyTime":
            return sort_students_time_selection(students, order)
        elif attribute == "AvgGrade":
            return sort_students_avg_insertion(students, order)
        else:
            return sort_students_failures_bubble(students, order)

# Do NOT include a main script in your submission
