# ECOR 1042 Lab 3 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Dylan Butz, Chloe Ouellette, Cameron MacGillivray, Arman Rahmani"

# Update "" with your team (e.g. T102)
__team__ = "T-051"

#==========================================#
# Place your student_school_list function after this line

def student_school_list(fileName: str, school: str) -> list:
    """
    Return a list containing a dict with the age, ID, study time, number of failures, health, absences, fall grade, and winter grade, for each student who attended the school given a csv file and a school.
    
    >>> student_school_list('student-mat.csv','GP')
    [{'ID': 1, 'Age': 18, 'StudyTime': 2.5, 'Failures': 0, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6}, {another element}, ... ]
    >>> student_school_list('student-mat.csv','hello')
    []
    >>> student_school_list('student-mat.csv','MS')
    [{'ID': 320, 'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Health': 5, 'Absences': 2, 'FallGrade': 11, 'WinterGrade': 11}, {another element}, ...]
    
    """
    dataString=""
    #open the given file in reading mode and put it in a variable called csv
    file = open(fileName, "r")
    #iterate through the file and add it to the dataString variable so that the entire file is converted into a str
    for line in file:
        dataString+=line
    file.close()
    
    #create a list splitting at each new line so each row is in a seperate index
    dataString= dataString.splitlines()
    #create the list that will contain the list we will return
    studentInformation = []
    #get all headers
    headers = dataString[0].rsplit(',')
    #get the location of the school header and delete it from the list of headers
    schoolIndex = headers.index('School')
    del headers[schoolIndex]

    #iterate through each row (meaning each student) of the new list
    for student in dataString:
        #convert the string into an array
        student = student.rsplit(',')
        #if the school in the students information matches then add their data 
        if(student[schoolIndex]==school):
            #delete the school information from the student 
            del student[schoolIndex]
            #create an empty dict then iterate through the students data and create new keys from the headers that match the students information
            currentDict = {}

            for value in range(len(student)):
                #convert to proper type
                if student[value].isdigit():
                    currentDict[headers[value]] = int(student[value])
                else:
                    try:
                        currentDict[headers[value]] = float(student[value])
                    except:
                        currentDict[headers[value]] = student[value]
            #add the dict to a new index in the array
            studentInformation += [currentDict]

    return studentInformation

#==========================================#
# Place your student_health_list function after this line

def student_health_list(filename: str, health: int) -> list[dict]:
    """
    Return a list of students, stored as dictionaries, whose health values are equivalent to health, given a csv file. Each dictionary contains a student's school, ID, age, study time, failures, absenses, fall grades and winter grades.
    Preconditions: 1 <= health <= 5.
    
    >>> student_health_list('student-mat.csv', 2)
    [ {'School': 'MS', 'ID': 20, 'Age': 20, 'StudyTime': 1.0, 'Failures': 1,'Absences': 10, 'FallGrade': 9, 'WinterGrade': 11},{another element}, …]
    >>> student_health_list('student-mat.csv', 'health')
    []
    >>> student_health_list('student-mat.csv', 5)
    [ {'School': 'GP', 'ID': 4, 'Age': 15, 'StudyTime': 3.0, 'Failures': 0,'Absences': 2, 'FallGrade': 15, 'WinterGrade': 14},{another element}, …]
    """
    
    data_str = ""
    file = open(filename, "r")
    for ch in file:
        data_str += ch
    file.close()

    data_str = data_str.splitlines()
    category = data_str[0].split(',')
    students = []
    health_index = category.index('Health')
    del category[health_index]

    for student in data_str:
        student = student.split(',')
        if student[health_index] == str(health):
            del student[health_index]
            student_dict = {}
            for x in range(len(student)):
                if student[x].isdigit():
                    student_dict[category[x]] = int(student[x])
                else:
                    try:
                        student_dict[category[x]] = float(student[x])
                    except:
                        student_dict[category[x]] = student[x]
            students += [student_dict]

    return students

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
#==========================================#
# Place your student_failures_list function after this line
def student_failures_list(filename: str, failures: int) -> list:
    """
     Return a list of students, each of which is a dictionary with the given number of failures.
    If there is no student with the intended number of failures, returns empty list.

     >>> student_failures_list('student-mat.csv', 0)
    [{'School': 'GP', 'ID': 201, 'Age': 18, 'StudyTime': 7.0, 'Health': 3,
      'Absences': 7, 'FallGrade': 12, 'WinterGrade': 13},
     {... more students with 0 failures ...}]

    >>> student_failures_list('student-mat.csv', 2)
    [{'School': 'GP', 'ID': 125, 'Age': 17, 'StudyTime': 3.0, 'Health': 4,
      'Absences': 5, 'FallGrade': 10, 'WinterGrade': 9},
     {... more students with 2 failures ...}]

    >>> student_failures_list('student-mat.csv', 220)
    []
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

        # find failures col pos = index
        failures_index = headers.index("Failures")

        #change them to ints
        current_failures = int(values[failures_index])

        # cont if row failures equivalent to intended function input param
        if current_failures == failures:
            #make a dictionary for this case
            student_dict = {}
            for i, h in enumerate(headers):
                if h == "Failures":
                    # Does not include failures column (handles ignore that redundant data)
                    continue
                if h in ["ID", "Age", "Health", "Absences",
                         "FG", "WG"]:
                    student_dict[h] = int(values[i])
                elif h == "ST":
                    student_dict[h] = float(values[i])
                else:
                    student_dict[h] = values[i]

            # Adds new student dictionary to the list of results
            result_list.append(student_dict)


    return result_list



#==========================================#
# Place your load_data function after this line

def load_data(fileName: str,request: dict) -> list:
    """
    Returns a list of all students information that matches the given dict except for the key value from a given dict and a given file name. A key value of All returns all information.

    >>> load_data('student-mat.csv', {'Failures': 0})
    [ {'School': 'GP', 'ID': 22, 'Age': 18, 'StudyTime':7.0, 'Health': 3, Absences': 7, 'FallGrade': 12, 'WinterGrade': 13},  {another element}, … ]
    >>> load_data('student-mat.csv',{'ID':1})
    Invalid Value
    []
    >>> load_data('student-mat.csv',{'HELLO':1000000000000})
    Invalid Value
    []
    """

    dataString = ""
    file = open(fileName,"r")
    for line in file:
        dataString += line
    file.close()
    
    dataString = dataString.split()
    information = []
    headers = dataString[0].split(',')
    #create a list of all information
    del dataString[0]
    for student in dataString:
        student=student.split(',')
        currentDict = {}
        for value in range(len(student)):
            if student[value].isdigit():
                currentDict[headers[value]] = int(student[value])
            else:
                try:
                    currentDict[headers[value]] = float(student[value])
                except:
                    currentDict[headers[value]] = student[value]
        information += [currentDict]

    finalInfo = []
    #if key is not all iterate through the information list and delete the key value given
    key = ""
    value = ""
    for i in request.keys():
        key = i
        value = request[key]
    if key != 'All':
        for student in information:
            try:
                student[key]
                if key == "FallGrade" or key == "WinterGrade" or key == "Absences" or key == "StudyTime" or key == "ID":
                    print("Invalid Value")
                    return []
            except:
                print("Invalid Value")
                return []
            if student[key] == value:
                del student[key]
                finalInfo += [student]
    else:
        return information
    return finalInfo

#==========================================#
# Place your add_average function after this line

def add_average(info: list) -> list:
    """
    Returns a list containing a dictionary with each students information with their average grade as an additional key given the original student information list.
    >>> add_average('studentmatList')
    [{'School': 'GP', 'ID': 1, 'Age': 18, 'StudyTime': 2.5, 'Failures': 0, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6, 'AvgGrade': 5.5}, ... ]
    """
    for student in info:
        student['AvgGrade'] = round((student['FallGrade'] + student['WinterGrade']) /2 , 2)
    return info

# Do NOT include a main script in your submission
