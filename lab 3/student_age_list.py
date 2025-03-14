# ECOR 1042 Lab 3 - Individual submission for student_age_list function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Arman Rahmani"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101333091"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-051"

#==========================================#
# Place your student_age_list function after this line
def student_age_list(filename: str, age: int) -> list:
    """
     Return a list of students, each of which is a dictionary with the given number of failures.
    If there is no student with the intended number of failures, returns empty list.


    """
    result_list = []    #the main list to be returned at end of function

    # open the file and read entire file into a string
    file = open(filename, "r")
    dataString = file.read()
    file.close()

    lines = dataString.splitlines()

    if not lines:
        return result_list  # return an empty list if file is empty

    header_line = lines[0].strip()
    headers = header_line.split(",")

    # reads all the next lines after the initial header, extracts the info
    for line in lines[1:]:
        line = line.strip()
        #skip empty line
        if not line:
            continue

        values = line.split(",")

        # find age col pos = index
        age_index = headers.index("Age")

        #change them to ints
        current_age = int(values[age_index])

        # cont if row age equivalent to intended function input param
        if current_age == age:
            #make a dictionary for this case
            student_dict = {}
            for i, h in enumerate(headers):
                if h == "Age":
                    # Does not include age column (handles ignore that redundant data)
                    continue
                if h in ["ID", "Failures", "Health", "Absences",
                         "FG", "WG"]:
                    student_dict[h] = int(values[i])
                elif h == "ST":
                    student_dict[h] = float(values[i])
                else:
                    student_dict[h] = values[i]

            # Adds new student dictionary to the list of results
            result_list.append(student_dict)


    return result_list


# Do NOT include a main script in your submission
