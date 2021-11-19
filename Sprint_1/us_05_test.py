import unittest
from .us_05 import US_05

class TEST_US_05(unittest.TestCase):
    result = US_05()
    def test_US_05_1(self):
        desired_output = ['US05: Individial @I16@ has death before marriage']
        self.assertEqual(self.result, desired_output)
    def test_US_05_2(self):
        self.assertTrue(self.result.count('US05: Individial @I16@ has death before marriage') > 0)
    def test_US_05_3(self):
        self.assertTrue(self.result.count('US05: Individial @I7@ has death before marriage') == 0)
    def test_US_05_4(self):
        self.assertFalse(self.result.count('US05: Individial @I8@ has death before marriage') > 0)
    def test_US_05_5(self):
        self.assertFalse(self.result.count('US05: Individial @I24@ has death before marriage') > 0)


if __name__ == "__main__":
    
    unittest.main(exit=False)