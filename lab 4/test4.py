# ECOR 1042 Lab 4 - Individual submission for test4 function

# import load_data module here
import load_data

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Cameron MacGillivray"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101354857"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-051"

def test_add_average() -> list[int]:
    passed = 0
    failed = 0

    # test that the function returns an empty list when it is called with an empty list
    test_input = []
    result = load_data.add_average(test_input.copy())
    try:
        assert result == [], "Empty list test failed: expected [] but got " + str(result)
    except AssertionError:
        failed += 1
    else:
        passed += 1

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
            try:
                test_dict.pop(key_to_remove)
            except KeyError:
                pass
            finally:
                original_key_count = len(test_dict)

            input_list = [test_dict.copy()]
            result_list = load_data.add_average(input_list)

            try:
                #First check that list length unchanged.
                assert len(result_list) == 1, "Scenario '" + scenario + "', iteration " + str(i) + " failed: expected list length 1 but got " + str(len(result_list))
                #Second check that dict has one new key vs original dict
                assert len(result_list[0]) == original_key_count + 1, "Scenario '" + scenario + "', iteration " + str(i) + " failed: expected dictionary key count " + str(original_key_count + 1) + " but got " + str(len(result_list[0]))
                #third check that AvgGrade is calc correctly.
                assert "AvgGrade" in result_list[0], "Scenario '" + scenario + "', iteration " + str(i) + " failed: missing 'AvgGrade' key"
                assert result_list[0]["AvgGrade"] == expected_avg, "Scenario '" + scenario + "', iteration " + str(i) + " failed: expected AvgGrade " + str(expected_avg) + " but got " + str(result_list[0]["AvgGrade"])
            except AssertionError:
                failed += 1
            else:
                passed += 1

    # return the a list with the number of tests that passed and the number that failed
    return [passed, failed]