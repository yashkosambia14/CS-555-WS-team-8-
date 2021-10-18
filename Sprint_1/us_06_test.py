import unittest
from .us_06 import US_06

class TEST_US_06(unittest.TestCase):
    result = US_06()
    def test_US_06_1(self):
        desired_output = ['US06: Individial @I16@ has death before divorce']
        self.assertEqual(self.result, desired_output)
    def test_US_06_2(self):
        self.assertTrue(self.result.count('US06: Individial @I16@ has death before divorce') > 0)
    def test_US_06_3(self):
        self.assertTrue(self.result.count('US06: Individial @I7@ has death before divorce') == 0)
    def test_US_06_4(self):
        self.assertFalse(self.result.count('US06: Individial @I8@ has death before divorce') > 0)
    def test_US_06_5(self):
        self.assertFalse(self.result.count('US06: Individial @I24@ has death before divorce') > 0)


if __name__ == "__main__":
    unittest.main(exit=False)