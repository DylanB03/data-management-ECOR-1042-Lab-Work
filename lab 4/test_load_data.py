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

def test_return_correct_dict_inside_list() -> list[int]:
    # Complete the function with your test cases
    filename = 'student-mat.csv'
    success = 0
    failure = 0

    # test that student_school_list returns a correct dictionary inside the list (3 different test cases required)
    school_names = ['GP', 'hi', 'MS']
    school_dict_first = [{'ID': 1, 'Age': 18, 'StudyTime': 2.5, 'Failures': 0, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6}, [
    ], {'ID': 320, 'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Health': 5, 'Absences': 2, 'FallGrade': 11, 'WinterGrade': 11}]
    school_dict_last = [{'ID': 79, 'Age': 17, 'StudyTime': 1, 'Failures': 3, 'Health': 3, 'Absences': 2, 'FallGrade': 8, 'WinterGrade': 8}, [
    ], {'ID': 395, 'Age': 19, 'StudyTime': 1, 'Failures': 0, 'Health': 5, 'Absences': 5, 'FallGrade': 8, 'WinterGrade': 9}]
    for i in range(len(school_names)):
        try:
            school_result = load_data.student_school_list(filename, school_names[i])
            if school_result == [] and school_dict_first[i] == []:
                success += 1
            else:
                assert school_result[0] == school_dict_first[i]
                assert school_result[-1] == school_dict_last[i]
                success += 1
        except:
            failure += 1

    # test that student_age_list returns a correct dictionary inside the list  (3 different test cases required)
    age_values = [18, 'hello', 19]
    age_dict_first = [{'School': 'GP', 'ID': 1, 'StudyTime': 2.5, 'Failures': 0, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6}, [
    ], {'School': 'MB', 'ID': 128, 'StudyTime': 2, 'Failures': 3, 'Health': 5, 'Absences': 2, 'FallGrade': 7, 'WinterGrade': 8}]
    age_dict_last = [{'School': 'MS', 'ID': 394, 'StudyTime': 1, 'Failures': 0, 'Health': 5, 'Absences': 0, 'FallGrade': 11, 'WinterGrade': 12}, [
    ], {'School': 'MS', 'ID': 395, 'StudyTime': 1, 'Failures': 0, 'Health': 5, 'Absences': 5, 'FallGrade': 8, 'WinterGrade': 9}]
    for i in range(len(age_values)):
        try:
            age_result = load_data.student_age_list(filename, age_values[i])
            if age_result == [] and school_dict_first[i] == []:
                success += 1
            else:
                assert age_result[0] == age_dict_first[i]
                assert age_result[-1] == age_dict_last[i]
                success += 1
        except:
            failure += 1

    # test that student_health_list returns a correct dictionary inside the list  (3 different test cases required)

    health_values = [3, 'woof', 5]
    health_dict_first = [{'School': 'GP', 'ID': 1, 'Age': 18, 'StudyTime': 2.5, 'Failures': 0, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6}, [
    ], {'School': 'GP', 'ID': 4, 'Age': 15, 'StudyTime': 3, 'Failures': 0, 'Absences': 2, 'FallGrade': 15, 'WinterGrade': 14}]
    health_dict_last = [{'School': 'MS', 'ID': 393, 'Age': 21, 'StudyTime': 1, 'Failures': 3, 'Absences': 3, 'FallGrade': 10, 'WinterGrade': 8}, [
    ], {'School': 'MS', 'ID': 395, 'Age': 19, 'StudyTime': 1, 'Failures': 0, 'Absences': 5, 'FallGrade': 8, 'WinterGrade': 9}]
    for i in range(len(health_values)):
        try:
            health_result = load_data.student_health_list(filename, health_values[i])
            if health_result == [] and health_dict_first[i] == []:
                success += 1
            else:
                assert health_result[0] == health_dict_first[i]
                assert health_result[-1] == health_dict_last[i]
                success += 1
        except:
            failure += 1

    # test that student_failures_list returns a correct dictionary inside the list (3 different test cases required)
    failures_values = [0, 'ALL', 3]
    failures_dict_first = [{'School': 'GP', 'ID': 1, 'Age': 18, 'StudyTime': 2.5, 'Health': 3, 'Absences': 6, 'FallGrade':5, 'WinterGrade': 6}, [
    ], {'School': 'GP', 'ID': 3, 'Age': 15, 'StudyTime': 2, 'Health': 3, 'Absences': 10, 'FallGrade': 7, 'WinterGrade': 8}]
    failures_dict_last = [{'School': 'MS', 'ID': 395, 'Age': 19, 'StudyTime': 1, 'Health': 5, 'Absences': 5, 'FallGrade': 8, 'WinterGrade': 9}, [
    ], {'School': 'MS', 'ID': 393, 'Age': 21, 'StudyTime': 1, 'Health': 3, 'Absences': 3, 'FallGrade': 10, 'WinterGrade': 8}]
    for i in range(len(failures_values)):
        try:
            failures_result = load_data.student_failures_list(filename, failures_values[i])
            if failures_result == [] and failures_dict_first[i] == []:
                success += 1
            else:
                assert failures_result[0] == failures_dict_first[i]
                assert failures_result[-1] == failures_dict_last[i]
                success += 1
        except:
            failure += 1
    # test that load_data returns a correct dictionary inside the list (6 different test cases required)
    load_values = [{'Failures': 0}, {'All': -1}, {'ID': 0},
                   {'Hello': 1000}, {'School': 'GP'}, {'Health': 500}]
    load_dict_first = [{'School': 'GP', 'ID': 1, 'Age': 18, 'StudyTime': 2.5, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6}, {'School': 'GP', 'ID': 1, 'Age': 18, 'StudyTime': 2.5,
                                                                                                                                              'Failures': 0, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6}, [], [], {'ID': 1, 'Age': 18, 'StudyTime': 2.5, 'Failures': 0, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6}, []]
    load_dict_last = [{'School': 'MS', 'ID': 395, 'Age': 19, 'StudyTime': 1, 'Health': 5, 'Absences': 5, 'FallGrade': 8, 'WinterGrade': 9}, {'School': 'MS', 'ID': 395, 'Age': 19, 'StudyTime': 1, 'Failures': 0,
                                                                                                                                             'Health': 5, 'Absences': 5, 'FallGrade': 8, 'WinterGrade': 9}, [], [], {'ID': 79, 'Age': 17, 'StudyTime': 1, 'Failures': 3, 'Health': 3, 'Absences': 2, 'FallGrade': 8, 'WinterGrade': 8}, []]
    for i in range(len(load_values)):
        try:
            load_result = load_data.load_data(filename, load_values[i])
            if load_result == [] and load_dict_first[i] == []:
                success += 1
            else:
                assert load_result[0] == load_dict_first[i]
                assert load_result[-1] == load_dict_last[i]
                success += 1
        except:
            failure += 1

    # test that add_average returns a correct dictionary inside the list  (3 different test cases required)
    average_values = [[{'School': 'GP', 'ID': 1, 'Age': 18, 'StudyTime': 2.5, 'Failures': 0, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6}], [], [{'School': 'MS', 'ID': 390, 'Age': 18, 'StudyTime': 2,
                                                                                                                                                                   'Failures': 1, 'Health': 5, 'Absences': 0, 'FallGrade': 6, 'WinterGrade': 5}, {'School': 'MS', 'ID': 391, 'Age': 20, 'StudyTime': 2, 'Failures': 2, 'Health': 4, 'Absences': 11, 'FallGrade': 9, 'WinterGrade': 9}]]
    average_dict_first = [{'School': 'GP', 'ID': 1, 'Age': 18, 'StudyTime': 2.5, 'Failures': 0, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6, 'AvgGrade': 5.5}, [
    ], {'School': 'MS', 'ID': 390, 'Age': 18, 'StudyTime': 2, 'Failures': 1, 'Health': 5, 'Absences': 0, 'FallGrade': 6, 'WinterGrade': 5, 'AvgGrade': 5.5}]
    average_dict_last = [{'School': 'GP', 'ID': 1, 'Age': 18, 'StudyTime': 2.5, 'Failures': 0, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6, 'AvgGrade': 5.5}, [
    ], {'School': 'MS', 'ID': 391, 'Age': 20, 'StudyTime': 2, 'Failures': 2, 'Health': 4, 'Absences': 11, 'FallGrade': 9, 'WinterGrade': 9, 'AvgGrade': 9}]
    for i in range(len(average_values)):
        try:
            average_result = load_data.add_average(average_values[i])
            if average_result == [] and average_dict_first[i] == []:
                success += 1
            else:
                assert average_result[0]['School'] == average_dict_first[i]['School']
                assert average_result[-1]['AvgGrade'] == average_dict_last[i]['AvgGrade']
                success += 1
        except:
            failure += 1
    # return the a list with the number of tests that passed and the number that failed
    return [success, failure]

# Place test_add_average function here


# Do NOT include a main script in your submission
