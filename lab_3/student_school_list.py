# ECOR 1042 Lab 3 - Individual submission for student_school_list function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Dylan Butz"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101333709"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-051"

#==========================================#
# Place your student_school_list function after this line

def student_school_list(fileName: str, school: str) -> list:
    """
    Returns a list containing a dict with the age, ID, study time, number of failures, health, absences, fall grade, and winter grade, for each student who attended the school given a csv file and a school.
    
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

# Do NOT include a main script in your submission
