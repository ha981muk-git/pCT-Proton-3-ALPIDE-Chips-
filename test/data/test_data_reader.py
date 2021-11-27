from unittest.mock import call
import pytest
from project_Mukhiya_inf3692_SS21.src.data.data_reader import preprocess, convert_to_float, row_to_list

@pytest.fixture
def raw_and_clean_data_file(tmpdir):
    raw_path = tmpdir.join('raw_data_file_path')
    clean_path = tmpdir.join('clean_data_file_path')
    with open(raw_path, "w") as f:
        f.write("1,494.0,314.0,32,21600\n"
        "1,495.0,314.0,32,21600\n"
        "1,496.0,312.0,32,21600\n"
        "1,496.0,313.0,32,21600\n"
        "1,492.0,310.0,33,22400\n"
                )

    return raw_path, clean_path


def row_to_list_bug_free(row):
    return_values = {"1,494.0,314.0,32,1600\n": ["1", "494", "314", "32", "21600"],
                       "1,495.0,314.0,21600\n": None,
                             "1,496.0,312.0\n": None,
                   "1,496.0,313.0,32,21600\n" : ["1", "496.0", "313.0","32", "21600"],
                     "1,492.0,310.0,33,2400\n": ["1", "492.0", "310.0", "33", "22400"],
                                         "\n" :  None,
                                   "1,492.0\n": None,
                                       "492\n": None
                     }
    return return_values[row]


def convert_to_int_bug_free(comma_separated_integer_string):
    return_values = {"1801": 1801,
                     "201411": 201411,
                     "2002": 2002,
                     "333209": 333209,
                     "313.0": 313,
                     "782911": 782911,
                     "1285": 1285,
                     "389.129": None,
                     }
    return return_values[comma_separated_integer_string]


class TestConvertToInt(object):
    def test_with_no_comma(self):
        test_argument = "756"
        expected = 756
        actual = convert_to_float(test_argument)
        assert actual == expected, "Expected: 756, Actual: {0}".format(actual)

    def test_with_one_comma(self):
        test_argument = "2081"
        expected = 2081
        actual = convert_to_float(test_argument)
        assert actual == expected, "Expected: 2081, Actual: {0}".format(actual)

    def test_with_two_commas(self):
        test_argument = "891"
        expected = 891
        actual = convert_to_float(test_argument)
        assert actual == expected, "Expected: 1034891, Actual: {0}".format(actual)

    def test_on_string_with_incorrectly_placed_comma(self):
        test_argument = "313.0"
        expected = 313
        actual = convert_to_float(test_argument)
        assert actual == expected, "Expected: None, Actual: {0}".format(actual)

    def test_on_string_with_missing_comma(self):
        test_argument = "3.91"
        expected = None
        actual = convert_to_float(test_argument)
        assert actual == expected, "Expected: None, Actual: {0}".format(actual)

    def test_on_float_valued_string(self):
        test_argument = "6.9889"
        expected = None
        actual = convert_to_float(test_argument)
        assert actual == expected, "Expected: None, Actual: {0}".format(actual)


class TestRowToList(object):
    def test_on_four_missing_value(self):    # (0, 0) boundary value
        actual = row_to_list("492\n")
        assert actual is None, "Expected: None, Actual: {0}".format(actual)

def test_on_two_missing_value(self):    # (2, 0) boundary value
        actual = row_to_list("1,496.0,312.0\n")
        assert actual is None, "Expected: None, Actual: {0}".format(actual)

def test_on_two_line_with_missing_value(self):    # (1, 1) boundary value
        actual = row_to_list("\n567\n")
        assert actual is None, "Expected: None, Actual: {0}".format(actual)

def test_on_one_missing_value(self):  # (1, 1) boundary value
        actual = row_to_list("1,495.0,314.0,21600\n")
        assert actual is None, "Expected: None, Actual: {0}".format(actual)

def test_on_empty_line_missing_value(self):    # (0, 1) case
        actual = row_to_list("\n")
        assert actual is None, "Expected: None, Actual: {0}".format(actual)

def test_on_three_with_missing_value(self):    # (0, 1) case
        actual = row_to_list("1,492.0\n")
        assert actual is None, "Expected: None, Actual: {0}".format(actual)

def test_on_normal_argument_1(self):
        actual = row_to_list("1,494.0,314.0,32,1600\n")
        expected = ["1", "494", "314", "32", "21600"]
        assert actual == expected, "Expected: {0}, Actual: {1}".format(expected, actual)

def test_on_normal_argument_2(self):
        actual = row_to_list("1,496.0,313.0,32,21600\n")
        expected = ["1", "496.0", "313.0","32", "21600"]
        assert actual == expected, "Expected: {0}, Actual: {1}".format(expected, actual)


def test_on_normal_argument_3(self):
       actual = row_to_list( "1,492.0,310.0,33,2400\n")
       expected = ["1", "492.0", "310.0", "33", "22400"]
       assert actual == expected, "Expected: {0}, Actual: {1}".format(expected, actual)


class TestPreprocess(object):
    def test_on_raw_data(self, raw_and_clean_data_file, mocker):
        raw_path, clean_path = raw_and_clean_data_file
        row_to_list_mock = mocker.patch("data.preprocessing_helpers.row_to_list", side_effect=row_to_list_bug_free)
        convert_to_int_mock = mocker.patch("data.preprocessing_helpers.convert_to_int",
                                           side_effect=convert_to_int_bug_free
                                           )
        preprocess(raw_path, clean_path)
        assert row_to_list_mock.call_args_list == [call("1", "494.0", "314.0", "32", "21600\n"),
                                                   call("2", "559.0", "423.0", "47", "33598\n"),
                                                   call("1", "495.0", "314.0", "32", "21600\n"),
                                                   call("2", "558.0", "422.0", "47", "33598\n"),
                                                   call("1", "492.0", "310.0", "33", "22400\n")
                                                   ]

        assert convert_to_int_mock.call_args_list == [call("1"), call("0"), call("314.0"), call("32"),
                                                      call("492.0"),  call("33"), call("22400"), call("33598")
                                                      ]
        with open(clean_path, "r") as f:
            lines = f.readlines()
        first_line = lines[0]
        assert first_line == "1,492.0,310.0,32,21600\n"
        second_line = lines[1]
        assert second_line == "1,493.0,310.0,32,21600\n"


