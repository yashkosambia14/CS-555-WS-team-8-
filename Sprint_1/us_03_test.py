import unittest
from .us_03 import US_03

class TEST_US_03(unittest.TestCase):
    result = US_03()
    def test_US_03_1(self):
        desired_output = ['ERROR: @I6@ has death before birth']
        self.assertEqual(self.result, desired_output)
    def test_US_03_2(self):
        self.assertTrue(self.result.count('ERROR: @I6@ has death before birth') > 0)
    def test_US_03_3(self):
        self.assertFalse(self.result.count('ERROR: @I2@ has death before birth') > 0)
    def test_US_03_4(self):
        self.assertFalse(self.result.count('ERROR: @I4@ has death before birth') > 0)
    def test_US_03_5(self):
        self.assertFalse(self.result.count('ERROR: @I11@ has death before birth') > 0)


if __name__ == "__main__":
    unittest.main(exit=False)
