# ECOR 1042 Lab 6 - Individual submission for curve_fit function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Dylan Butz"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101333709"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-051"

#==========================================#
# Place your curve_fit function after this line

import numpy as np
def curve_fit(data: list, compare: str, order: int) -> str:
    """
    Returns a string representing the equation of best fit for the average grade in comparison to another value given a list of dicts containing the average grades, the string key to compare it to, and the order.
    
    >>> curve_fit([{"AvgGrade": 10, "Age": 10}, {"AvgGrade":20, "Age": 20}], "Age", 1)
    y = x
    >>> curve_fit([{"AvgGrade": 10, "Age": 10}, {"AvgGrade":20, "Age": 20}], "Age", 5)
    y = x
    >>> curve_fit([{"AvgGrade": 10, "Age": 10}, {"AvgGrade":20, "Age": 20}, {"AvgGrade": 15, "Age": 5}], "Age", 10)
    y = -1.5*x^2+30.5*x^1+-190
    
    """

    x = []
    y= []
    for person in data:
        x += person["AvgGrade"]
        y+= person[compare]
    
    rep = ""
    if order>len(x):
        power = len(np.polyfit(x,y,len(x)-1).split())
        for value in np.polyfit(x,y,len(x)-1).split():
            if power != 0:
                if value == 1:
                    rep += "x^" + str(power) + "+"
                else:
                    rep += str(value) + "*x^" + str(power) + "+"
            else:
                rep += str(value)
            power -= 1
    else:
        for value in np.polyfit(x,y,order).split():
            if order != 0:
                if value == 1:
                    rep += "x^" + str(order) + "+"
                else:
                    rep += str(value) + "*x^" + str(order) + "+"
            else:
                rep += str(value)
            order -= 1
    return "y = " + rep






# Do NOT include a main script in your submission
