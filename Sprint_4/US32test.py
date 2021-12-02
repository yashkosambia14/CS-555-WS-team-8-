from .US32 import listMultipleBirths
import unittest

# Path to your `.ged` file
file_path0 = r"Sprint_4\gedcom\CS 555 Family.ged"
file_path1 = r"Sprint_4\gedcom\US32_Empty.ged"
file_path2 = r"Sprint_4\gedcom\US32_1Twin.ged"
file_path3 = r"Sprint_4\gedcom\US32_1Triplet.ged"
file_path4 = r"Sprint_4\gedcom\US32_2Twin.ged"

class Test_US_32(unittest.TestCase):
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
        self.assertEqual(listMultipleBirths(file_path4), "US32: Individuals were born at the same on: ['3 JAN 2000', '6 MAR 0111']")
  

if __name__ == '__main__':
    unittest.main()