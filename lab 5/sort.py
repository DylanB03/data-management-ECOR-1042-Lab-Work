# ECOR 1042 Lab 5 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Dylan Butz, Chloe Ouellette, Cameron MacGillivray, Arman Rahmani"

# Update "" with your team (e.g. T102)
__team__ = "T-051"

#==========================================#
# Place your sort_students_age_bubble function after this line


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

#==========================================#
# Place your sort_students_avg_insertion function after this line

def sort_students_avg_insertion(students: list, rank: str) -> str:
    """
    Sorts a given list containing dicts based on average grades, either ascending or descending, and returns whether or not it was sorted.
    
    >>> sort_students_avg_insertion([], "D")
    "Empty list."
    >>> sort_students_avg_insertion([{"AvgGrade":7.2,"School":"GP"}, {"AvgGrade":9.1,"School":"MS"}], "D")
    "List sorted."
    >>> sort_students_avg_insertion([{"School":"GP"}, {"School":"MS"}], "D")
    "List not sorted. AvgGrade key not present."
    """
    if len(students)==0:
        return "Empty list."
    
    for index in range(1,len(students)):
        try:
            key = students[index]
            value = key["AvgGrade"]
            j = index - 1
        except:
            return "List not sorted. AvgGrade key not present."
        while j >= 0 and value < students[j]["AvgGrade"]:
            students[j+1] = students[j]
            j -=1
        students[j+1] = key
    
    if rank == "D":
        for index in range(0,len(students)//2):
            temp = students[index]
            students[index]= students[len(students)-1-index]
            students[len(students)-1-index] = temp
        return "List sorted."
    elif rank == "A":
        return "List sorted."


#==========================================#
# Place your sort_students_failures_bubble function after this line


#==========================================#
# Place your sort function after this line


# Do NOT include a main script in your submission
