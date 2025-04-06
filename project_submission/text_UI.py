# ECOR 1042 Lab 6 - Individual submission for text_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Cameron MacGillivray"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101354857"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-051"

"""
!
! !
! ! !
! ! ! ! PLEASE SEE README  !
! ! !
! !
!

This module provides the full text-based user interface that incorporates functionality from
various previous lab submissions, including curve_fit, histogram, load_data and sort.

As such, the program can be run, and all former programmed functionality can be used 
simply from the terminal, inputting parameters when requested for order of curve fit, 
file to be read, or any other parameter appropriate to the previous modules.

"""
#==========================================#
# Place your script for your text_UI after this line

import load_data
import sort
import curve_fit
import histogram


def display_menu():
    print("L)oad Data")
    print("S)ort Data")
    print("C)urve Fit")
    print("H)istogram")
    print("E)xit")


def text_UI():
    data_loaded = False
    data = None  # Holds all data
    while True:
        display_menu()
        command = input("Please type your command: ").strip()

        # Load Data Option
        if command.lower() == 'l':
            filename = input("Please enter the name of the file: ").strip()
            filter_attr = input("Please enter the attribute to use as a filter: ").strip()

            if filter_attr.lower() == "all":
                # No filtering
                request = {"All": None}
            else:
                # Filter by (attribute = value)
                filter_value = input("Please enter the value of the attribute: ").strip()
                request = {filter_attr: filter_value}

            data = load_data.load_data(filename, request)

            if data is not None and data != []:
                data_loaded = True
                print("Data loaded")
            else:
                print("Error loading data.")

        # Sort Data Option
        elif command.lower() == 's':
            if not data_loaded:
                print("File not loaded. Please, load a file first.")
                continue

            # Allows multiple varying capitalization, since personal testing led to a bunch of issues unless strictly follow what's in the file, like "age", "AGE", "Age" to sort by "Age".
            valid_attributes = {
                "age": "Age",
                "studytime": "StudyTime",
                "avggrade": "AvgGrade",
                "failures": "Failures"
            }

            # The user enters the attribute to use in sorting
            sort_attr_input = input("Please enter the attribute you want to use for sorting:\n'Age', 'Failures', 'AvgGrade', 'StudyTime': ").strip()
            attr_lower = sort_attr_input.lower()
            if attr_lower in valid_attributes: #check if it is one of the valid attributes to sort by, otherwise presents error message
                sort_attr = valid_attributes[attr_lower]
            else:
                print(f"Invalid input, the list cannot be sorted by {sort_attr_input}.")
                continue

            order = input("Ascending (A) or Descending (D) order: ").strip()
            display_choice = input("Do you want to display the data? (Y/N): ").strip()

            sort_message = sort.sort(data, order, sort_attr)

            if display_choice.lower() == 'y':
                print(data)
            else:
                print("<<<You selected not to display>>>")

            print(sort_message)

        # Curve Fit Option
        elif command.lower() == 'c':
            if not data_loaded:
                print("File not loaded. Please, load a file first.")
                continue

            fit_attr_input = input("Please enter the attribute you want to use to find the best fit for AvgGrade: ").strip()

            poly_order_str = input("Please enter the order of the polynomial to be fitted: ").strip()
            try:
                poly_order = int(poly_order_str)
            except ValueError:
                print("Invalid polynomial order. Please enter an integer.")
                continue

            equation = curve_fit.curve_fit(data, fit_attr_input, poly_order)
            print(equation)

        # Histogram Option
        elif command.lower() == 'h':
            if not data_loaded:
                print("File not loaded. Please, load a file first.")
                continue

            hist_attr = input("Please enter the attribute you want for plotting: ").strip()

            result = histogram.histogram(data, hist_attr)
            if result == -1:
                print("Histogram displayed for categorical attribute.")
            else:
                print("Histogram displayed. Maximum value:", result)

        # Exit Option
        elif command.lower() == 'e':
            break

        # Invalid Case Handling
        else:
            if not data_loaded:
                print("No such command.")
            else:
                print("Invalid command.")


if __name__ == "__main__":
    text_UI()

# You are allowed to create auxiliary functions
