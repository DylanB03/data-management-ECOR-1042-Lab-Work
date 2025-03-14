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

        age_index = headers.index("Age")

        #change to ints
        current_age = int(values[age_index])

        # keep if row age equivalent to intended function input param
        if current_age == age:
            #make a dict
            student_dict = {}
            for i, h in enumerate(headers):
                if h == "Age":
                    # doesn't include age column
                    continue
                if h in ["ID", "Failures", "Health", "Absences",
                         "FG", "WG"]:
                    student_dict[h] = int(values[i])
                elif h == "ST":
                    student_dict[h] = float(values[i])
                else:
                    student_dict[h] = values[i]

            result_list.append(student_dict)


    return result_list


# Do NOT include a main script in your submission
