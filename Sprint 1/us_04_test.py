import unittest
from us_04 import US_04

class TEST_US_04(unittest.TestCase):
    result = US_04()
    def test_US_04_1(self):
        desired_output = ['ERROR: @F6@ has divorce before marriage','ERROR: @F11@ has divorce before marriage']
        self.assertEqual(self.result, desired_output)
    def test_US_04_2(self):
        self.assertTrue(self.result.count('ERROR: @F6@ has divorce before marriage') > 0)
    def test_US_04_3(self):
        self.assertFalse(self.result.count('ERROR: @F10@ has divorce before marriage') > 0)
    def test_US_04_4(self):
        self.assertFalse(self.result.count('ERROR: @F9@ has divorce before marriage') > 0)
    def test_US_04_5(self):
        self.assertFalse(self.result.count('ERROR: @F5@ has divorce before marriage') > 0)


if __name__ == "__main__":
    unittest.main(exit=False)