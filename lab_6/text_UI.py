# ECOR 1042 Lab 6 - Individual submission for text_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Cameron MacGillivray"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101354857"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-051"

#==========================================#
# Place your script for your text_UI after this line

from lab_3 import load_data
from lab_5 import sort
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
    data = None  # This will hold the loaded dataset
    while True:
        display_menu()
        command = input("Please type your command: ").strip()
        # Process the command (case-insensitive)
        if command.lower() == 'l':
            # Load Data Command
            filename = input("Please enter the name of the file: ").strip()
            filter_attr = input("Please enter the attribute to use as a filter: ").strip()
            # Build the request dictionary depending on user input
            if filter_attr.lower() == "all":
                request = {"All": None}
            else:
                filter_value = input("Please enter the value of the attribute: ").strip()
                request = {filter_attr: filter_value}
            # Call the load_data module's function (assumed to compute AvgGrade)
            data = load_data.load_data(filename, request)
            if data is not None and data != []:
                data_loaded = True
                print("Data loaded")
            else:
                print("Error loading data.")

        elif command.lower() == 's':
            # Sort Data Command
            if not data_loaded:
                print("File not loaded. Please, load a file first.")
                continue
            sort_attr = input("Please enter the attribute you want to use for sorting: ").strip()
            order = input("Ascending (A) or Descending (D) order: ").strip()
            display_choice = input("Do you want to display the data? (Y/N): ").strip()
            # Call the sort module's function
            sort_message = sort.sort(data, order, sort_attr)
            if display_choice.lower() == 'y':
                print(data)
            else:
                print("<<<You selected not to display>>>")
            print(sort_message)

        elif command.lower() == 'c':
            # Curve Fit Command
            if not data_loaded:
                print("File not loaded. Please, load a file first.")
                continue
            fit_attr = input("Please enter the attribute you want to use to find the best fit for AvgGrade: ").strip()
            poly_order_str = input("Please enter the order of the polynomial to be fitted: ").strip()
            try:
                poly_order = int(poly_order_str)
            except ValueError:
                print("Invalid polynomial order. Please enter an integer.")
                continue
            # Call the curve_fit module's function which returns the equation as a string
            equation = curve_fit.curve_fit(data, fit_attr, poly_order)
            print(equation)

        elif command.lower() == 'h':
            # Histogram Command
            if not data_loaded:
                print("File not loaded. Please, load a file first.")
                continue
            hist_attr = input("Please enter the attribute you want for plotting: ").strip()
            # The histogram function both displays the plot and returns a value based on attribute type.
            result = histogram.histogram(data, hist_attr)
            if result == -1:
                print("Histogram displayed for categorical attribute.")
            else:
                print("Histogram displayed. Maximum value:", result)

        elif command.lower() == 'e':
            # Exit Command
            break

        else:
            # Invalid command handling:
            if not data_loaded:
                print("No such command.")
            else:
                print("Invalid command.")


if __name__ == "__main__":
    text_UI()


# You are allowed to create auxiliary functions



