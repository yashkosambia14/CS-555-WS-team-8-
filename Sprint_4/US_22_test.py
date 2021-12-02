import unittest
import US_22

class TEST_US_22(unittest.TestCase):
    result = US_22.US_22()
    print('US22: ')
    print(result)
    def test_US_22_1(self):
        desired_output = ["No duplicates found"]
        self.assertEqual(self.result, desired_output)
    def test_US_22_2(self):
        self.assertTrue(self.result.count('@I4@ is a duplicate value') < 1)
    def test_US_22_3(self):
        self.assertTrue(self.result.count('@I3@ is a duplicate value') == 0)
    def test_US_22_4(self):
        self.assertFalse(self.result.count('@I6@ is a duplicate value') > 0)
    def test_US_22_5(self):
        self.assertFalse(self.result.count('@F2@ is a duplicate value') > 0)


if __name__ == "__main__":
    unittest.main(exit=False)