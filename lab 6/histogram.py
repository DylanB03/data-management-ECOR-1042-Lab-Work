# ECOR 1042 Lab 6 - Individual submission for histogram

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Chloe Ouellette"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101337142"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-051"

# ==========================================#
# Place your histogram function after this line
import matplotlib.pyplot as plt
import numpy as np


def histogram(students: list[dict], attribute: str) -> int:
    """
    Return a histogram of the attribute specified for the list of students inputted. If the attribute is organized numerically, there will be ten even-sized bins on the histogram and the highest value of attribute will be returned. Otherwise, it will be organized by category and -1 will be returned.
    >>> histogram([{'Age': 17, 'School': 'GP', 'Health': 5, 'Failures': 3}, {'Age': 19, 'School': 'MS', 'Health': 3, 'Failures': 0}], 'Health')
    5
    >>> histogram([{'School': 'GP', 'Age': 19}, {'School': 'GP', 'Age': 18}, {'School': 'MS', 'Age': 15}], 'Age')
    19
    >>> histogram([{'School': 'MS', 'Failures': 0}, {'School': 'GP', 'Age': 14}], 'School')
    -1
    """
    val_dict = {}
    x_vals = []
    y_vals = []
    for student in students:
        stu_att = student[attribute]
        freq = val_dict.get(stu_att, 0)
        val_dict[stu_att] = freq + 1

    if isinstance(students[0][attribute], str):
        x_vals += val_dict.keys()
        y_vals += val_dict.values()
        max_val = -1

    elif isinstance(students[0][attribute], (float, int)):
        max_val = max(student[attribute] for student in students)
        temp_x = np.linspace(0, max_val, 11)
        x_vals = [0] * 10
        for i in range(0, 10):
            x_vals[i] = f'(round(temp_x[i], 2) to (round(temp_x[i + 1], 2))'
        y_vals = [0] * 10
        for key in val_dict.keys():
            for i in range(10):
                if temp_x[i] <= float(key) < temp_x[i + 1]:
                    y_vals[i] += 1

    fig = plt.figure()
    plt.title(attribute + 'Histogram')
    plt.xlabel(attribute + 'Category')
    plt.ylabel('Number of students')
    plt.bar(x_vals, y_vals)
    plt.show()
    return max_val
# Do NOT include a main script in your submission

