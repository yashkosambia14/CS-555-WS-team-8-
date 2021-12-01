from US33 import listOrphans
import unittest

# Path to your `.ged` file
file_path0 = "C:/Users/twang/Desktop/ged/CS 555 Family.ged"
file_path1 = "C:/Users/twang/Desktop/ged/US33_Nothing.ged"
file_path2 = "C:/Users/twang/Desktop/ged/US33_1Orphan.ged"
file_path3 = "C:/Users/twang/Desktop/ged/US33_1Orphan1Adult.ged"
file_path4 = "C:/Users/twang/Desktop/ged/US33_2Orphan.ged"

class TestStringMethods(unittest.TestCase):
    # Test cases
    def test0(self):
        self.assertEqual(listOrphans(file_path0), "US33: Orphaned Individuals are: ")
    def test1(self):
        self.assertEqual(listOrphans(file_path1), "US33: Orphaned Individuals are: ")
    def test2(self):
        self.assertEqual(listOrphans(file_path2), "US33: Orphaned Individuals are: @I3@ ")
    def test3(self):
        self.assertEqual(listOrphans(file_path3), "US33: Orphaned Individuals are: @I3@ ")
    def test4(self):
        self.assertEqual(listOrphans(file_path4), "US33: Orphaned Individuals are: @I3@ @I4@ ")
  

if __name__ == '__main__':
    unittest.main()