# CS555ws - TEAM - 8
import unittest
from .US_38 import birthdays_output
from datetime import date
today = date.today()
d4 = today.strftime("%d-%b-%Y")
today_date = list(d4.split('-'))
current_month = today_date[1]


#print(birthdays_output)

class TestStringMethodsUS38(unittest.TestCase):
    def test_living_married_testcase1(self):
        result = ''
        expected_output = birthdays_output[0][1]
        if expected_output not in current_month:
            result = expected_output
        self.assertEqual(result, expected_output)

    def test_living_married_testcase2(self):
        result = ''
        expected_output = birthdays_output[1][1]
        if expected_output not in current_month:
            result = expected_output
        self.assertEqual(result, expected_output)

    def test_living_married_testcase3(self):
        result = ''
        expected_output = birthdays_output[2][1]
        if expected_output not in current_month:
            result = expected_output
        self.assertEqual(result, expected_output)

    def test_living_married_testcase4(self):
        result = ''
        expected_output = birthdays_output[3][1]
        if expected_output not in current_month:
            result = expected_output
        self.assertEqual(result, expected_output)

    def test_living_married_testcase5(self):
        result = ''
        expected_output = birthdays_output[4][1]
        if expected_output not in current_month:
            result = expected_output
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()


