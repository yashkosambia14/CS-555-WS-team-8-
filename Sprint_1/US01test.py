from gedcom.element.individual import IndividualElement
from gedcom.parser import Parser
from .US01 import beforeCurrentDate
import unittest

# Path to your `.ged` file
# file_path0 = "C:/Users/twang/Desktop/ged/CS 555 Family.ged"
file_path1 = "Sprint_1\gedcom\US01_1birth.ged"
file_path2 = "Sprint_1\gedcom\US01_1birth1death.ged"
file_path3 = "Sprint_1\gedcom\US01_1death.ged"
file_path4 = "Sprint_1\gedcom\US01_2birth2death.ged"

# Initialize the parser
gedcom_parser = Parser()

# Parse your file
# gedcom_parser.parse_file(file_path0)
# allElements0 = gedcom_parser.get_element_list()
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
    # def test0(self):
    #     self.assertEqual(beforeCurrentDate(allElements0), "")
    def test1(self):
        self.assertEqual(beforeCurrentDate(allElements1), "US01: Birthday of Two One  occurs in the future\n")
    def test2(self):
        self.assertEqual(beforeCurrentDate(allElements2), "US01: Death of One Two  occurs in the future\n")
    def test3(self):
        self.assertEqual(beforeCurrentDate(allElements3), "US01: Birthday of Two One  occurs in the future\nUS01: Death of One Two  occurs in the future\n")
    def test4(self):
        self.assertEqual(beforeCurrentDate(allElements4), "US01: Birthday of Two One  occurs in the future\nUS01: Death of One Two  occurs in the future\nUS01: Death of Three One  occurs in the future\nUS01: Birthday of Three One  occurs in the future\n")
  

if __name__ == '__main__':
    unittest.main()