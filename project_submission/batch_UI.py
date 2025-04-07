# ECOR 1042 Lab 6 - Individual submission for batch_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Arman Rahmani"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101333091"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-051"

# ==========================================#
# Place your script for your batch_UI after this line
import load_data
import sort
import curve_fit
import histogram


def batch_UI():
    """
    Returns a series of commands given a filename with said series of commands, inputted by the user.
    Users are able to load data, sort data, find a line of best fit, and generate histograms.

    >>> batch_UI()
    L;student.csv;School;GP
    S;Age;D;N
    H;Failures
    <assume text above is from file>

    Please enter the name of the file where your commands are stored: <filename>
    Data Loaded
    List sorted. <You selected not to display>
    <Histograms with Failures will be shown>
    """
    user_filename = input("Please enter the name of the file where your commands are stored: ")
    file = open(user_filename, 'r')
    data = []
    data_loaded = False

    for line in file:
        commands_seq = line.strip().split(";")
        if commands_seq[0].upper() == "L":
            filename = commands_seq[1]
            attribute = commands_seq[2]
            if attribute == "All":
                request = {"All": None}
            else:
                request = {attribute: commands_seq[3]}
                if attribute != "School":
                    request[attribute] = int(request[attribute])
            data = load_data.add_average(load_data.load_data(filename, request))
            print("Data Loaded\n")
            data_loaded = True

        elif commands_seq[0].upper() == "S":
            if data_loaded:
                sort.sort(data, commands_seq[2], commands_seq[1])
                print("List sorted.")
                if commands_seq[3].upper() == "Y":
                    print(data)
            else:
                print("You must load a file first before data may be sorted")

        elif commands_seq[0].upper() == "C":
            if len(data) == 0:
                print("Student list is empty")
            elif data_loaded:
                curve_fit_attribute = commands_seq[1]
                poly_order = int(commands_seq[2])
                print(curve_fit.curve_fit(data, curve_fit_attribute, poly_order))
            else:
                print("You must load a file first before data be given a curve fit")

        elif commands_seq[0].upper() == "H":
            if data_loaded:
                histogram_attribute = commands_seq[1]
                histogram.histogram(data, histogram_attribute)
            else:
                print("You must load a file first before data can be graphed")

        elif commands_seq[0].upper() == "E":
            break


if __name__ == "__main__":
    batch_UI()

# You are allowed to create auxiliary functions
