#CS555 - TEAM 8 - YASH KOSAMBIA


from  .US_living_single import living_single_output
import unittest


"""TESTING 5 POSSIBLE CASES FROM LIVING SINGLE"""

class TestStringMethodsUS30(unittest.TestCase):
    print('testing us 30')
    def test_living_singles_testcase1(self):
        result = ''
        expected_output = 'YASH JAYESH KOSAMBIA'
        if expected_output in living_single_output:
            result = expected_output
        self.assertEqual(result, expected_output)

    def test_living_singles_testcase2(self):
        result2 = ''
        expected_output2 = 'MANILAL MARKER'
        if expected_output2 in living_single_output:
            result2 = expected_output2
        self.assertEqual(result2, expected_output2)

    def test_living_singles_testcase3(self):
        result3 = ''
        expected_output3 = 'ANIL KOSAMBIA'
        if expected_output3 in living_single_output:
            result3 = expected_output3
        self.assertEqual(result3, expected_output3)

    def test_living_singles_testcase4(self):
        result4 = ''
        expected_output4 = 'MANILAL MARKER'
        if expected_output4 in living_single_output:
            result4 = expected_output4
        self.assertEqual(result4, expected_output4)

    def test_living_singles_testcase5(self):
        result5 = ''
        expected_output5 = 'MANILAL MARKER'
        if expected_output5 in living_single_output:
            result5 = expected_output5
        self.assertEqual(result5, expected_output5)

if __name__ == '__main__':
    unittest.main(exit=False)