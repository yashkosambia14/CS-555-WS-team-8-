import unittest
from .us_09 import US_09

class TEST_US_09(unittest.TestCase):
    result = US_09()
    def test_US_09_1(self):
        desired_output = ['@I1@ was born before parents marriage Family ID: @F1@']
        self.assertEqual(self.result, desired_output)
    def test_US_09_2(self):
        self.assertTrue(self.result.count('@I1@ was born before parents marriage Family ID: @F1@') > 0)
    def test_US_09_3(self):
        self.assertTrue(self.result.count('@I2@ was born before parents marriage Family ID: @F2@') == 0)
    def test_US_09_4(self):
        self.assertFalse(self.result.count('@I4@ was born before parents marriage Family ID: @F1@') > 0)
    def test_US_09_5(self):
        self.assertFalse(self.result.count('@I13@ was born before parents marriage Family ID: @F4@') > 0)


if __name__ == "__main__":
    unittest.main(exit=False)