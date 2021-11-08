import unittest
from .us_10 import US_10

class TEST_US_10(unittest.TestCase):
    result = US_10()
    def test_US_10_1(self):
        desired_output = ['@I2@ was married before age 14, Age: 11']
        self.assertEqual(self.result, desired_output)
    def test_US_10_2(self):
        self.assertTrue(self.result.count('@I2@ was married before age 14, Age: 11') > 0)
    def test_US_10_3(self):
        self.assertTrue(self.result.count('@I8@ was married before age 14, Age: 13') == 0)
    def test_US_10_4(self):
        self.assertFalse(self.result.count('@I9@ was married before age 14, Age: 10') > 0)
    def test_US_10_5(self):
        self.assertFalse(self.result.count('@I2@ was married before age 14, Age: 30') > 0)


if __name__ == "__main__":
    unittest.main(exit=False)