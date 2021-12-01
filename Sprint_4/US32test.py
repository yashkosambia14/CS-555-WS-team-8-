from US32 import listMultipleBirths
import unittest

# Path to your `.ged` file
file_path0 = "C:/Users/twang/Desktop/ged/CS 555 Family.ged"
file_path1 = "C:/Users/twang/Desktop/ged/US32_Empty.ged"
file_path2 = "C:/Users/twang/Desktop/ged/US32_1Twin.ged"
file_path3 = "C:/Users/twang/Desktop/ged/US32_1Triplet.ged"
file_path4 = "C:/Users/twang/Desktop/ged/US32_2Twin.ged"

class TestStringMethods(unittest.TestCase):
    # Test cases
    def test0(self):
        self.assertEqual(listMultipleBirths(file_path0), "US32: Individuals were born at the same on: []")
    def test1(self):
        self.assertEqual(listMultipleBirths(file_path1), "US32: Individuals were born at the same on: []")
    def test2(self):
        self.assertEqual(listMultipleBirths(file_path2), "US32: Individuals were born at the same on: ['3 JAN 2000']")
    def test3(self):
        self.assertEqual(listMultipleBirths(file_path3), "US32: Individuals were born at the same on: ['3 JAN 2000']")
    def test4(self):
        self.assertEqual(listMultipleBirths(file_path4), "US32: Individuals were born at the same on: ['6 MAR 0111', '3 JAN 2000']")
  

if __name__ == '__main__':
    unittest.main()