from US02 import birthBeforeMarriage
import unittest

# Path to your `.ged` file
file_path0 = "C:/Users/twang/Desktop/ged/CS 555 Family.ged"
file_path1 = "C:/Users/twang/Desktop/ged/US02_Normal.ged"
file_path2 = "C:/Users/twang/Desktop/ged/US02_MaleOver.ged"
file_path3 = "C:/Users/twang/Desktop/ged/US02_FemaleOver.ged"
file_path4 = "C:/Users/twang/Desktop/ged/US02_BothOver.ged"

class TestStringMethods(unittest.TestCase):
    # Test cases
    def test0(self):
        self.assertEqual(birthBeforeMarriage(file_path0), "")
    def test1(self):
        self.assertEqual(birthBeforeMarriage(file_path1), "")
    def test2(self):
        self.assertEqual(birthBeforeMarriage(file_path2), "US02: Individual born on 2010 occurs after marriage date on 2000\n")
    def test3(self):
        self.assertEqual(birthBeforeMarriage(file_path3), "US02: Individual born on 2010 occurs after marriage date on 2000\n")
    def test4(self):
        self.assertEqual(birthBeforeMarriage(file_path4), "US02: Individual born on 2010 occurs after marriage date on 2000\nUS02: Individual born on 2010 occurs after marriage date on 2000\n")
  

if __name__ == '__main__':
    unittest.main()