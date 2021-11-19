import unittest
from .US_15 import US_15

class TEST_US_15(unittest.TestCase):
    result = US_15()
    print('US15: ')
    print(result)
    def test_US_15_1(self):
        desired_output = ['All Families have fewer than 15 siblings']
        self.assertEqual(self.result, desired_output)
    def test_US_15_2(self):
        self.assertTrue(self.result.count('All Families have fewer than 15 siblings') > 0)
    def test_US_15_3(self):
        self.assertTrue(self.result.count('@F2@ has more than 15 siblings') == 0)
    def test_US_15_4(self):
        self.assertFalse(self.result.count('@F3@ has more than 15 siblings') > 0)
    def test_US_15_5(self):
        self.assertFalse(self.result.count('@F1@ has more than 15 siblings') > 0)


if __name__ == "__main__":
    unittest.main(exit=False)