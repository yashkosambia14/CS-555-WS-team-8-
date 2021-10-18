import unittest
from US05 import Userstories_table
expected_output2 = str(Userstories_table)
class TestStringMethods(unittest.TestCase):

    def test_userstory05(self): # using new well defined variable names
        result = ''
        expected_output = Userstories_table
        if expected_output in Userstories_table:
            result = expected_output
        self.assertEqual(result, expected_output2)

if __name__ == '__main__':
    unittest.main()