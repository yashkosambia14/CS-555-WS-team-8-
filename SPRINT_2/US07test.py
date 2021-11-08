from gedcom.element.individual import IndividualElement
from gedcom.parser import Parser
from US07 import lessThan150
import unittest

# Path to your `.ged` file
file_path0 = "C:/Users/twang/Desktop/ged/CS 555 Family.ged"
file_path1 = "C:/Users/twang/Desktop/ged/US07_1AliveOver.ged"
file_path2 = "C:/Users/twang/Desktop/ged/US07_1DeadOver.ged"
file_path3 = "C:/Users/twang/Desktop/ged/US07_1AliveOver1DeadOver.ged"
file_path4 = "C:/Users/twang/Desktop/ged/US07_2DeadOver.ged"

# Initialize the parser
gedcom_parser = Parser()

# Parse your file
gedcom_parser.parse_file(file_path0)
allElements0 = gedcom_parser.get_element_list()
gedcom_parser.parse_file(file_path1)
allElements1 = gedcom_parser.get_element_list()
gedcom_parser.parse_file(file_path2)
allElements2 = gedcom_parser.get_element_list()
gedcom_parser.parse_file(file_path3)
allElements3 = gedcom_parser.get_element_list()
gedcom_parser.parse_file(file_path4)
allElements4 = gedcom_parser.get_element_list()

class TestStringMethods(unittest.TestCase):
    # Test cases
    def test0(self):
        self.assertEqual(lessThan150(allElements0), "")
    def test1(self):
        self.assertEqual(lessThan150(allElements1), "US07: More than 150 years old: - Birth Date 5 MAR 1800\n")
    def test2(self):
        self.assertEqual(lessThan150(allElements2), "US07: More than 150 years old at death - Birth Date 5 MAR 1800 Death Date 6 JUN 2000\n")
    def test3(self):
        self.assertEqual(lessThan150(allElements3), "US07: More than 150 years old at death - Birth Date 5 MAR 1800 Death Date 6 JUN 2000\nUS07: More than 150 years old: - Birth Date 6 MAY 1500\n")
    def test4(self):
        self.assertEqual(lessThan150(allElements4), "US07: More than 150 years old at death - Birth Date 5 MAR 1800 Death Date 6 JUN 2000\nUS07: More than 150 years old at death - Birth Date 6 MAY 1500 Death Date 10 FEB 2000\n")
  

if __name__ == '__main__':
    unittest.main()