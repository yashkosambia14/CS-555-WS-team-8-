from US14 import multipleBirths
import unittest

# Path to your `.ged` file
file_path0 = "C:/Users/twang/Desktop/ged/CS 555 Family.ged"
file_path1 = "C:/Users/twang/Desktop/ged/US14_1FamOver.ged"
file_path2 = "C:/Users/twang/Desktop/ged/US14_1FamFine.ged"
file_path3 = "C:/Users/twang/Desktop/ged/US14_1FamOver1FamFine.ged"
file_path4 = "C:/Users/twang/Desktop/ged/US14_2FamOver.ged"

class TestStringMethods(unittest.TestCase):
    # Test cases
    def test0(self):
        self.assertEqual(multipleBirths(file_path0), "US14: The following years have more than 5 siblings born at the same time: []")
    def test1(self):
        self.assertEqual(multipleBirths(file_path1), "US14: The following years have more than 5 siblings born at the same time: ['1 JAN 2000']")
    def test2(self):
        self.assertEqual(multipleBirths(file_path2), "US14: The following years have more than 5 siblings born at the same time: []")
    def test3(self):
        self.assertEqual(multipleBirths(file_path3), "US14: The following years have more than 5 siblings born at the same time: ['1 JAN 2000']")
    def test4(self):
        self.assertEqual(multipleBirths(file_path4), "US14: The following years have more than 5 siblings born at the same time: ['1 JAN 2010', '1 JAN 2000']")
  

if __name__ == '__main__':
    unittest.main()