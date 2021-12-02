import unittest
from .US_21 import US_21

class TEST_US_21(unittest.TestCase):
    result = US_21()
    print('US21: ')
    print(result)
    def test_US_21_1(self):
        desired_output = ["All Families have correct gender roles"]
        self.assertEqual(self.result, desired_output)
    def test_US_21_2(self):
        self.assertTrue(self.result.count('ERROR: @I4@ has incorrect gender role in family @F1@') < 1)
    def test_US_21_3(self):
        self.assertTrue(self.result.count('ERROR: @I3@ has incorrect gender role in family @F1@') == 0)
    def test_US_21_4(self):
        self.assertFalse(self.result.count('ERROR: @I6@ has incorrect gender role in family @F2@') > 0)
    def test_US_21_5(self):
        self.assertFalse(self.result.count('ERROR: @I8@ has incorrect gender role in family @F3@') > 0)


if __name__ == "__main__":
    unittest.main(exit=False)