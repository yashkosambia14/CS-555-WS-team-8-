#CS555 - TEAM 8 - YASH KOSAMBIA
import unittest

from ged4py.parser import GedcomReader
from ged4py.model import Individual
from Living_married import living_married_output

"""TESTING 5 POSSIBLE ELEMENTS IN THE LIVING MARRIED LIST"""


#print(living_married_output)
class TestStringMethods(unittest.TestCase):
    def test_living_married_testcase1(self):
        result = ''
        expected_output = 'JAYESH KOSAMBIA'
        if expected_output in living_married_output:
            result = expected_output
        self.assertEqual(result, expected_output)

    def test_living_married_testcase2(self):
        result2 = ''
        expected_output2 = 'KAMLA MARKER'
        if expected_output2 in living_married_output:
            result2 = expected_output2
        self.assertEqual(result2, expected_output2)

    def test_living_married_testcase3(self):
        result3 = ''
        expected_output3 = 'PARVATIBEN KOSAMBIA'
        if expected_output3 in living_married_output:
            result3 = expected_output3
        self.assertEqual(result3, expected_output3)

    def test_living_married_testcase4(self):
        result4 = ''
        expected_output4 = 'DIVYA KOSAMBIA'
        if expected_output4 in living_married_output:
            result4 = expected_output4
        self.assertEqual(result4, expected_output4)

    def test_living_married_testcase(self):
        result5 = ''
        expected_output5 = 'MEENA PARMAR'
        if expected_output5 in living_married_output:
            result5 = expected_output5
        self.assertEqual(result5, expected_output5)

    

if __name__ == '__main__':
    unittest.main()
