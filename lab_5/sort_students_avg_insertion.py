# ECOR 1042 Lab 5 - Individual submission for sort_students_avg_insertion function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Dylan Butz"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101333709"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-051"

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
    

# Do NOT include a main script in your submission
