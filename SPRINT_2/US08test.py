from gedcom.element.individual import IndividualElement
from gedcom.parser import Parser
from US08 import birthBeforeMarriage
import unittest

# Path to your `.ged` file
file_path0 = "C:/Users/twang/Desktop/ged/CS 555 Family.ged"
file_path1 = "C:/Users/twang/Desktop/ged/US08_1BeforeMarriage.ged"
file_path2 = "C:/Users/twang/Desktop/ged/US08_1RegularMarriage.ged"
file_path3 = "C:/Users/twang/Desktop/ged/US08_2BeforeMarriage.ged"
file_path4 = "C:/Users/twang/Desktop/ged/US08_2RegularMarriage.ged"

class TestStringMethods(unittest.TestCase):
    # Test cases
    def test0(self):
        self.assertEqual(birthBeforeMarriage(file_path0), "")
    def test1(self):
        self.assertEqual(birthBeforeMarriage(file_path1), "US08: Child born on: 1990 occurs after marriage 2000\n")
    def test2(self):
        self.assertEqual(birthBeforeMarriage(file_path2), "")
    def test3(self):
        self.assertEqual(birthBeforeMarriage(file_path3), "US08: Child born on: 1990 occurs after marriage 2000\nUS08: Child born on: 1970 occurs after marriage 2000\n")
    def test4(self):
        self.assertEqual(birthBeforeMarriage(file_path4), "")
  

if __name__ == '__main__':
    unittest.main()