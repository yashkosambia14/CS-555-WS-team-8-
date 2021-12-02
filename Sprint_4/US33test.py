from .US33 import listOrphans
import unittest

# Path to your `.ged` file
file_path0 = r"Sprint_4\gedcom\CS 555 Family.ged"
file_path1 = r"Sprint_4\gedcom\US33_Nothing.ged"
file_path2 = r"Sprint_4\gedcom\US33_1Orphan.ged"
file_path3 = r"Sprint_4\gedcom\US33_1Orphan1Adult.ged"
file_path4 = r"Sprint_4\gedcom\US33_2Orphan.ged"

class Test_US_33(unittest.TestCase):
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