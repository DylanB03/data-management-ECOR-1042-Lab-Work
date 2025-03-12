# ECOR 1042 Lab 3 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Dylan Butz, Chloe Ouellette, Cameron MacGillivray, Arman Rahmani"

# Update "" with your team (e.g. T102)
__team__ = "T051"

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


#==========================================#
# Place your student_failures_list function after this line


#==========================================#
# Place your load_data function after this line


#==========================================#
# Place your add_average function after this line


# Do NOT include a main script in your submission
