import unittest
from .US_36 import deathdays
from datetime import date
today = date.today()
d4 = today.strftime("%d-%b-%Y")
today_date = list(d4.split('-'))
current_month = today_date[1]

class Test_US_36(unittest.TestCase):
    def test_US_36_testcase1(self):
        result = []
        expected_output = deathdays[1][1]
        if expected_output != current_month:
            result = expected_output
        self.assertEqual(result, expected_output)

    def test_US_36_testcase2(self):
        result = []
        expected_output = deathdays[2][1]
        if expected_output != current_month:
            result = expected_output
        self.assertEqual(result, expected_output)

    def test_US_36_testcase3(self):
        result = []
        expected_output = deathdays[4][1]
        if expected_output != current_month:
            result = expected_output
        self.assertEqual(result, expected_output)

    def test_US_36_testcase4(self):
        result = []
        expected_output = deathdays[5][1]
        if expected_output != current_month:
            result = expected_output
        self.assertEqual(result, expected_output)

    def test_US_36_testcase5(self):
        result = []
        expected_output = deathdays[6][1]
        if expected_output != current_month:
            result = expected_output
        self.assertEqual(result, expected_output)




if __name__ == '__main__':
    unittest.main()

