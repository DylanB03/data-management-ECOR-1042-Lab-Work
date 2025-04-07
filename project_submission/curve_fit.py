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
    Returns a string representing the equation of best fit for the average grade
    in comparison to another value given a list of dictionaries containing the average grades,
    the string key to compare it to, and the degree of the polynomial.

    If order is negative, returns an error message.

    >>> curve_fit([{"AvgGrade": 10, "Age": 10}, {"AvgGrade":20, "Age": 20}], "Age", 1)
    y = x
    >>> curve_fit([{"AvgGrade": 10, "Age": 10}, {"AvgGrade":20, "Age": 20}], "Age", -1)
    Error: Polynomial order must be >= 0.
    """
    if order < 0:
        return "Error: Polynomial order must be >= 0."

    x = []
    y = []
    for person in data:
        try:
            yval = float(person["AvgGrade"])
            xval = float(person[compare])
            y.append(yval)
            x.append(xval)
        except Exception:
            continue

    # Average out duplicate x values
    rep = ""
    covered = []
    newx = []
    newy = []
    for idx in range(len(x)):
        if x[idx] not in covered:
            covered.append(x[idx])
            avgy = 0
            num = 0
            for j in range(len(x)):
                if x[j] == x[idx]:
                    avgy += y[j]
                    num += 1
            newx.append(x[idx])
            newy.append(avgy / num)
    x = newx
    y = newy

    # Use interpolation (degree = len(x)-1) if requested order is higher than possible
    full_degree = len(x) - 1
    if order > full_degree:
        coeffs = np.polyfit(x, y, full_degree).tolist()
        current_degree = full_degree
    else:
        coeffs = np.polyfit(x, y, order).tolist()
        current_degree = order

    # Build string representation of the polynomial
    for coef in coeffs:
        if current_degree > 0:
            if coef == 1:
                rep += "x^" + str(current_degree) + "+"
            else:
                rep += str(coef) + "*x^" + str(current_degree) + "+"
        else:
            rep += str(coef)
        current_degree -= 1

    return "y = " + rep






# Do NOT include a main script in your submission
