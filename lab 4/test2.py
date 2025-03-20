# ECOR 1042 Lab 4 - Individual submission for test2 function

# import load_data module here
import load_data
# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Arman Rahmani"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101333091"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-051"

#==========================================#
# Do not modify the code alreayd provided.


def test_return_list_correct_length() -> list[int]:
    # Complete the function with your test cases
    passed = 0
    failed = 0
    # test that student_school_list returns a list with the correct length (3 different test cases required)
    cases = ["GP", "MS", "DE"]
    case_answers = [3, 4, 0]
    for i in range(len(cases)):
        try:
            assert len(load_data.student_school_list('student-test.csv', cases[i])) == case_answers[i]
            passed += 1
        except:
            failed += 1
                       
    # test that student_age_list returns a list  with the correct length (3 different test cases required)
    cases = [18, 15, 2]
    case_answers = [4, 3, 0]
    for i in range(len(cases)):
        try:
            assert len(load_data.student_age_list('student-test.csv', cases[i])) == case_answers[i]
            passed += 1
        except:
            failed += 1            

    # test that student_health_list returns a list with the correct length (3 different test cases required)
    cases = [1, 5, 2]
    case_answers = [1, 3, 0]
    for i in range(len(cases)):
        try:
            assert len(load_data.student_health_list('student-test.csv', cases[i])) == case_answers[i]
            passed += 1
        except:
            failed += 1            

    # test that student_failures_list returns a list with the correct length(3 different test cases required)
    cases = [0, 5, 1]
    case_answers = [11, 0, 1]
    for i in range(len(cases)):
        try:
            assert len(load_data.student_failures_list('student-test.csv', cases[i])) == case_answers[i]
            passed += 1
        except:
            failed += 1
            
    # test that load_data returns a list  with the correct length (6 different test cases required)
    try:
        assert len(load_data.load_data('student-test.csv', {'Failures': 0})) == 11
        passed += 1
    except:
        failed += 1   
          
    try:
        assert len(load_data.load_data('student-test.csv', {'Age': 16})) == 2
        passed += 1
    except:
        failed += 1     

    try:
        assert len(load_data.load_data('student-test.csv', {'Health': 0})) == 0
        passed += 1
    except:
        failed += 1             
            
    try:
        assert len(load_data.load_data('student-test.csv', {'School': "A"})) == 0
        passed += 1
    except:
        failed += 1  
    
    try:
        assert len(load_data.load_data('student-test.csv', {'Age': 0})) == 0
        passed += 1
    except:
        failed += 1     
        
    try:
        assert len(load_data.load_data('student-test.csv', {'Health': 3})) == 8
        passed += 1
    except:
        failed += 1             
    
    # test that add_average returns a list   with the correct length (3 different test cases required)
    try:
        assert len(load_data.add_average([{'School': 'GP', 'ID': 10, 'Age': 18, 'StudyTime': 2.5, 'Failures': 0, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6}, {'School': 'GP', 'ID': 100, 'Age': 17, 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 4, 'FallGrade': 5, 'WinterGrade': 5}, {'School': 'GP', 'ID': 20, 'Age': 15, 'StudyTime': 2, 'Failures': 3, 'Health': 3, 'Absences': 10, 'FallGrade': 7, 'WinterGrade': 8}])) == 3
        passed += 1
    except:
        failed += 1        
        
    try:
        assert len(load_data.add_average([])) == 0
        passed += 1
    except:
        failed += 1        
        
    try:
        assert len(load_data.add_average([{'School': 'GP', 'ID': 10, 'Age': 18, 'StudyTime': 2.5, 'Failures': 0, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6}, {'School': 'GP', 'ID': 100, 'Age': 17, 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 4, 'FallGrade': 5, 'WinterGrade': 5}])) == 2
        passed += 1
    except:
        failed += 1
        
    # return the a list with the number of tests that passed and the number that failed
    return [passed, failed]

# Do NOT include a main script in your submission
