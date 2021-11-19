import unittest
from .US_16 import US_16

class TEST_US_16(unittest.TestCase):
    result = US_16()
    print('US16: ')
    print(result)
    def test_US_16_1(self):
        desired_output = ['ERROR: @I4@ has family name different from Husband name in family: @F1@']
        self.assertEqual(self.result, desired_output)
    def test_US_16_2(self):
        self.assertTrue(self.result.count('ERROR: @I4@ has family name different from Husband name in family: @F1@') > 0)
    def test_US_16_3(self):
        self.assertTrue(self.result.count('ERROR: @I3@ has family name different from Husband name in family: @F1@') == 0)
    def test_US_16_4(self):
        self.assertFalse(self.result.count('ERROR: @I6@ has family name different from Husband name in family: @F2@') > 0)
    def test_US_16_5(self):
        self.assertFalse(self.result.count('ERROR: @I8@ has family name different from Husband name in family: @F3@') > 0)


if __name__ == "__main__":
    unittest.main(exit=False)