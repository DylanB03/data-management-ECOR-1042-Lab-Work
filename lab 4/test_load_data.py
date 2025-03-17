# ECOR 1042 Lab 4 - team submission

# import load_data module here

# Update "" with your the name of the active members of the team
__author__ = "Dylan Butz, Chloe Ouellette, Cameron MacGillivray, Arman Rahmani"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-051"

#==========================================#

# Place test_return_list function here
import load_data
def test_return_list() -> list[int]:
    # Complete the function with your test cases
    # test that student_school_list returns a list (3 different test cases required
    cases =  ["GP","MB","Carleton"]
    passed = 0
    failed = 0
    for test in cases:
        try:
            assert isinstance(load_data.student_school_list('student-test.csv',test),list)
            passed +=1
        except:
            failed += 1
    # test that student_age_list returns a list (3 different test cases required)
    cases = [0,17,50]
    for test in cases:
        try:
            assert isinstance(load_data.student_age_list('student-test.csv',test),list)
            passed +=1
        except:
            failed += 1
    # test that student_health_list returns a list (3 different test cases required)
    cases = [-10,3,1]
    for test in cases:
        try:
            assert isinstance(load_data.student_health_list('student-test.csv',test),list)
            passed +=1
        except:
            failed += 1
    # test that student_failures_list returns a list (3 different test cases required)
    cases = [0,1,5]
    for test in cases:
        try:
            assert isinstance(load_data.student_failures_list('student-test.csv',test),list)
            passed +=1
        except:
            failed += 1
    # test that load_data returns a list (6 different test cases required)
    cases = [{"Failures": 0},{"ID":10},{"Age":18},{"Health":0},{"All":1000},{"hello":1050}]
    for test in cases:
        try:
            assert isinstance(load_data.load_data('student-test.csv',test),list)
            passed +=1
        except:
            failed += 1
    # test that add_average returns a list (3 different test cases required)
    cases = [load_data.load_data('student-test.csv',{"Failures":0}),load_data.student_school_list('student-test.csv',"GP"),load_data.student_age_list("student-test.csv",0)]
    for test in cases:
        try:
            assert isinstance(load_data.add_average(test),list)
            passed +=1
        except:
            print(6)
            failed += 1

    # return the a list with the number of tests that passed and the number that failed
    return [passed,failed]


# Place test_return_list_correct_lenght function here


# Place test_return_correct_dict_inside_list function here


# Place test_add_average function here


# Do NOT include a main script in your submission
