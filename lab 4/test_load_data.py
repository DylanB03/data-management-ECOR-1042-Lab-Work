# ECOR 1042 Lab 4 - team submission

# import load_data module here
import load_data
# Update "" with your the name of the active members of the team
__author__ = "Dylan Butz, Chloe Ouellette, Cameron MacGillivray, Arman Rahmani"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-051"

#==========================================#

# Place test_return_list function here
def test_return_list() -> list[int]:
    # Complete the function with your test cases
    # test that student_school_list returns a list (3 different test cases required
    cases =  ["GP","MB","Carleton"]
    passed = 0
    failed = 0
    for test in cases:
        try:
            assert isinstance(load_data.student_school_list('student-test.csv',test),list), "test_return_list() case 1, student_school_list: " + test + "failed"
            passed +=1
        except:
            failed += 1
    # test that student_age_list returns a list (3 different test cases required)
    cases = [0,17,50]
    for test in cases:
        try:
            assert isinstance(load_data.student_age_list('student-test.csv',test),list), "test_return_list() case 2, student_age_list: " + test + "failed"
            passed +=1
        except:
            failed += 1
    # test that student_health_list returns a list (3 different test cases required)
    cases = [-10,3,1]
    for test in cases:
        try:
            assert isinstance(load_data.student_health_list('student-test.csv',test),list), "test_return_list() case 3, student_health_list: " + test + "failed"
            passed +=1
        except:
            failed += 1
    # test that student_failures_list returns a list (3 different test cases required)
    cases = [0,1,5]
    for test in cases:
        try:
            assert isinstance(load_data.student_failures_list('student-test.csv',test),list), "test_return_list() case 4, student_failures_list: " + test + "failed"
            passed +=1
        except:
            failed += 1
    # test that load_data returns a list (6 different test cases required)
    cases = [{"Failures": 0},{"ID":10},{"Age":18},{"Health":0},{"All":1000},{"hello":1050}]
    for test in cases:
        try:
            assert isinstance(load_data.load_data('student-test.csv',test),list), "test_return_list() case 5, load_data: " + test + "failed"
            passed +=1
        except:
            failed += 1
    # test that add_average returns a list (3 different test cases required)
    cases = [load_data.load_data('student-test.csv',{"Failures":0}),load_data.student_school_list('student-test.csv',"GP"),load_data.student_age_list("student-test.csv",0)]
    for test in cases:
        try:
            assert isinstance(load_data.add_average(test),list), "test_return_list() case 6, add_average: " + test + "failed"
            passed +=1
        except:
            print(6)
            failed += 1

    # return the a list with the number of tests that passed and the number that failed
    return [passed,failed]

# Place test_return_list_correct_lenght function here
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
        assert len(load_data.add_average([{'School': 'GP', 'ID': 10, 'Age': 18, 'StudyTime': 2.5, 'Failures': 0,
                                           'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6},
                                          {'School': 'GP', 'ID': 100, 'Age': 17, 'StudyTime': 2, 'Failures': 0,
                                           'Health': 3, 'Absences': 4, 'FallGrade': 5, 'WinterGrade': 5},
                                          {'School': 'GP', 'ID': 20, 'Age': 15, 'StudyTime': 2, 'Failures': 3,
                                           'Health': 3, 'Absences': 10, 'FallGrade': 7, 'WinterGrade': 8}])) == 3
        passed += 1
    except:
        failed += 1

    try:
        assert len(load_data.add_average([])) == 0
        passed += 1
    except:
        failed += 1

    try:
        assert len(load_data.add_average([{'School': 'GP', 'ID': 10, 'Age': 18, 'StudyTime': 2.5, 'Failures': 0,
                                           'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6},
                                          {'School': 'GP', 'ID': 100, 'Age': 17, 'StudyTime': 2, 'Failures': 0,
                                           'Health': 3, 'Absences': 4, 'FallGrade': 5, 'WinterGrade': 5}])) == 2
        passed += 1
    except:
        failed += 1

    # return the a list with the number of tests that passed and the number that failed
    return [passed, failed]

# Place test_return_correct_dict_inside_list function here
def test_return_correct_dict_inside_list() -> list[int]:
    # Complete the function with your test cases
    filename = 'student-test.csv'
    success = 0
    failure = 0

    # test that student_school_list returns a correct dictionary inside the list (3 different test cases required)
    school_names = ['GP', 'hi', 'MS']
    school_dict_first = [{'ID': 10, 'Age': 18, 'StudyTime': 2.5, 'Failures': 0, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6}, [
    ], {'ID': 29, 'Age': 17, 'StudyTime': 1, 'Failures': 0, 'Health': 4, 'Absences': 8, 'FallGrade': 11, 'WinterGrade': 10}]
    school_dict_last = [{'ID': 20, 'Age': 15, 'StudyTime': 2, 'Failures': 3, 'Health': 3, 'Absences': 10, 'FallGrade': 7, 'WinterGrade': 8}, [
    ], {'ID': 32, 'Age': 18, 'StudyTime': 3, 'Failures': 0, 'Health': 5, 'Absences': 2, 'FallGrade': 9, 'WinterGrade': 8}]
    for i in range(len(school_names)):
        try:
            school_result = load_data.student_school_list(
                filename, school_names[i])
            if school_result == []:
                assert school_result == school_dict_first[i], "Second school test failed"
                success += 1
            else:
                assert school_result[0] == school_dict_first[i], "First half of " + str(
                    school_names[i]) + " school test failed"
                assert school_result[-1] == school_dict_last[i], "Second half of " + str(
                    school_names[i]) + " school test failed"
                success += 1
        except AssertionError as msg:
            print(msg)
            failure += 1

    # test that student_age_list returns a correct dictionary inside the list  (3 different test cases required)
    age_values = [18, 'hello', 15]
    age_dict_first = [{'School': 'GP', 'ID': 10, 'StudyTime': 2.5, 'Failures': 0, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6}, [
    ], {'School': 'GP', 'ID': 20, 'StudyTime': 2, 'Failures': 3, 'Health': 3, 'Absences': 10, 'FallGrade': 7, 'WinterGrade': 8}]
    age_dict_last = [{'School': 'MS', 'ID': 32, 'StudyTime': 3, 'Failures': 0, 'Health': 5, 'Absences': 2, 'FallGrade': 9, 'WinterGrade': 8}, [
    ], {'School': 'CF', 'ID': 23, 'StudyTime': 5, 'Failures': 2, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 9}]
    for i in range(len(age_values)):
        try:
            age_result = load_data.student_age_list(filename, age_values[i])
            if age_result == []:
                assert age_result == age_dict_first[i], "Second age test failed"
                success += 1
            else:
                assert age_result[0] == age_dict_first[i], "First half of " + \
                    str(age_values[i]) + " age test failed"
                assert age_result[-1] == age_dict_last[i], "Second half of " + \
                    str(age_values[i]) + " age test failed"
                success += 1
        except AssertionError as msg:
            print(msg)
            failure += 1

    # test that student_health_list returns a correct dictionary inside the list  (3 different test cases required)

    health_values = [3, 'woof', 5]
    health_dict_first = [{'School': 'GP', 'ID': 10, 'Age': 18, 'StudyTime': 2.5, 'Failures': 0, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6}, [
    ], {'School': 'CF', 'ID': 24, 'Age': 16, 'StudyTime': 2, 'Failures': 1, 'Absences': 4, 'FallGrade': 10, 'WinterGrade': 12}]
    health_dict_last = [{'School': 'BD', 'ID': 27, 'Age': 18, 'StudyTime': 3, 'Failures': 0, 'Absences': 1, 'FallGrade': 13, 'WinterGrade': 12}, [
    ], {'School': 'MS', 'ID': 32, 'Age': 18, 'StudyTime': 3, 'Failures': 0, 'Absences': 2, 'FallGrade': 9, 'WinterGrade': 8}]
    for i in range(len(health_values)):
        try:
            health_result = load_data.student_health_list(
                filename, health_values[i])
            if health_result == []:
                assert health_result == health_dict_first[i], "Second health test failed"
                success += 1
            else:
                assert health_result[0] == health_dict_first[i], "First half of " + str(
                    health_values[i]) + " health test failed"
                assert health_result[-1] == health_dict_last[i], "Second half of " + str(
                    health_values[i]) + " health test failed"
                success += 1
        except AssertionError as msg:
            print(msg)
            failure += 1

    # test that student_failures_list returns a correct dictionary inside the list (3 different test cases required)
    failures_values = [0, 'ALL', 3]
    failures_dict_first = [{'School': 'GP', 'ID': 10, 'Age': 18, 'StudyTime': 2.5, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6}, [
    ], {'School': 'GP', 'ID': 20, 'Age': 15, 'StudyTime': 2, 'Health': 3, 'Absences': 10, 'FallGrade': 7, 'WinterGrade': 8}]
    failures_dict_last = [{'School': 'MS', 'ID': 32, 'Age': 18, 'StudyTime': 3, 'Health': 5, 'Absences': 2, 'FallGrade': 9, 'WinterGrade': 8}, [
    ], {'School': 'GP', 'ID': 20, 'Age': 15, 'StudyTime': 2, 'Health': 3, 'Absences': 10, 'FallGrade': 7, 'WinterGrade': 8}]
    for i in range(len(failures_values)):
        try:
            failures_result = load_data.student_failures_list(
                filename, failures_values[i])
            if failures_result == []:
                assert failures_result == failures_dict_first[i], "Second failures test failed"
                success += 1
            else:
                assert failures_result[0] == failures_dict_first[i], "First half of " + str(
                    failures_values[i]) + " failures test failed"
                assert failures_result[-1] == failures_dict_last[i], "Second half of " + str(
                    failures_values[i]) + " failures test failed"
                success += 1
        except AssertionError as msg:
            print(msg)
            failure += 1
    # test that load_data returns a correct dictionary inside the list (6 different test cases required)
    load_values = [{'Failures': 0}, {'All': -1}, {'ID': 0},
                   {'Hello': 1000}, {'School': 'GP'}, {'Health': 500}]
    load_dict_first = [{'School': 'GP', 'ID': 10, 'Age': 18, 'StudyTime': 2.5, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6}, {'School': 'GP', 'ID': 10, 'Age': 18, 'StudyTime': 2.5,
                                                                                                                                               'Failures': 0, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6}, [], [], {'ID': 10, 'Age': 18, 'StudyTime': 2.5, 'Failures': 0, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6}, []]
    load_dict_last = [{'School': 'MS', 'ID': 32, 'Age': 18, 'StudyTime': 3, 'Health': 5, 'Absences': 2, 'FallGrade': 9, 'WinterGrade': 8}, {'School': 'MS', 'ID': 32, 'Age': 18, 'StudyTime': 3, 'Failures': 0,
                                                                                                                                            'Health': 5, 'Absences': 2, 'FallGrade': 9, 'WinterGrade': 8}, [], [], {'ID': 20, 'Age': 15, 'StudyTime': 2, 'Failures': 3, 'Health': 3, 'Absences': 10, 'FallGrade': 7, 'WinterGrade': 8}, []]
    for i in range(len(load_values)):
        try:
            load_result = load_data.load_data(filename, load_values[i])
            if load_result == []:
                assert load_result == load_dict_first[i], str(
                    load_values[i]) + " load test failed"
                success += 1
            else:
                assert load_result[0] == load_dict_first[i], "First half of " + \
                    str(load_values[i]) + " load test failed"
                assert load_result[-1] == load_dict_last[i], "Second half of " + \
                    str(load_values[i]) + " load test failed"
                success += 1
        except AssertionError as msg:
            print(msg)
            failure += 1

    # test that add_average returns a correct dictionary inside the list  (3 different test cases required)
    average_values = [[{'School': 'GP', 'ID': 10, 'Age': 18, 'StudyTime': 2.5, 'Failures': 0, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6}], [], [{'School': 'MS', 'ID': 32, 'Age': 18, 'StudyTime': 3,
                                                                                                                                                                   'Failures': 0, 'Health': 5, 'Absences': 2, 'FallGrade': 9, 'WinterGrade': 8}, {'School': 'CF', 'ID': 23, 'Age': 15, 'StudyTime': 5, 'Failures': 2, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 9}]]
    average_dict_first = [{'School': 'GP', 'ID': 10, 'Age': 18, 'StudyTime': 2.5, 'Failures': 0, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6, 'AvgGrade': 5.5}, [
    ], {'School': 'MS', 'ID': 32, 'Age': 18, 'StudyTime': 3, 'Failures': 0, 'Health': 5, 'Absences': 2, 'FallGrade': 9, 'WinterGrade': 8, 'AvgGrade': 8.5}]
    average_dict_last = [{'School': 'GP', 'ID': 10, 'Age': 18, 'StudyTime': 2.5, 'Failures': 0, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6, 'AvgGrade': 5.5}, [
    ], {'School': 'CF', 'ID': 23, 'Age': 15, 'StudyTime': 5, 'Failures': 2, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 9, 'AvgGrade': 7}]
    for i in range(len(average_values)):
        try:
            average_result = load_data.add_average(average_values[i])
            if average_result == []:
                assert average_result == average_dict_first[i], "Second average test failed"
                success += 1
            else:
                assert average_result[0]['School'] == average_dict_first[i]['School'], "First half of " + str(
                    average_values[i]) + " average test failed"
                assert average_result[-1]['AvgGrade'] == average_dict_last[i]['AvgGrade'], "Second half of " + str(
                    average_values[i]) + " average test failed"
                success += 1
        except AssertionError as msg:
            print(msg)
            failure += 1
    # return the a list with the number of tests that passed and the number that failed
    return [success, failure]

# Do NOT include a main script in your submission


# Place test_add_average function here
def test_add_average() -> list[int]:
    # Complete the function with your test cases
    passed = 0
    failed = 0

    # test that the function returns an empty list when it is called with an empty list
    test_input = []
    result = load_data.add_average(test_input.copy())
    if result == []:
        passed += 1
    else:
        failed += 1


    base_dict = {
        "School": "GP",
        "ID": 1,
        "Age": 18,
        "StudyTime": 2.5,
        "Failures": 0,
        "Health": 3,
        "Absences": 6,
        "FallGrade": 5,
        "WinterGrade": 6
    }

    #all possible scenarios to be tested for in set
    scenarios = {
        "all": None,
        "missing_school": "School",
        "missing_health": "Health",
        "missing_age": "Age",
        "missing_failures": "Failures",
    }

    # test that the function does not change the length of the list provided as input parameter (5 different test cases required)
    # test that the function inscrememnts the number of keys of the dictionary inside the list by one  (5 different test cases required)
    # test that the G_Avg value is properly calculated  (5 different test cases required)

    for scenario, key_to_remove in scenarios.items():
        for i in range(3):

            test_dict = base_dict.copy()
            test_dict["ID"] += i
            test_dict["Failures"] += 1
            test_dict["WinterGrade"] += 1

            #average expected
            expected_avg = round((test_dict["FallGrade"] + test_dict["WinterGrade"]) / 2, 2)

            original_key_count = len(test_dict)
            if key_to_remove is not None:
                test_dict.pop(key_to_remove)
                original_key_count = len(test_dict)

            input_list = [test_dict.copy()]
            result_list = load_data.add_average(input_list)

            #First check that list length unchanged.
            if len(result_list) != 1:
                failed += 1
                continue

            #Second check that dict has one new key vs original dict
            if len(result_list[0]) != original_key_count + 1:
                failed += 1
                continue

            #third check that AvgGrade is calc correctly.
            if "AvgGrade" not in result_list[0]:
                failed += 1
                continue
            if result_list[0]["AvgGrade"] != expected_avg:
                failed += 1
                continue

            passed += 1

    # return the a list with the number of tests that passed and the number that failed
    return [passed,failed]

# Do NOT include a main script in your submission
