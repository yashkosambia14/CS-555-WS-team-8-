from gedcom.element.individual import IndividualElement
from gedcom.parser import Parser
from US27 import listIndividualAges
import unittest

# Path to your `.ged` file
file_path0 = "C:/Users/twang/Desktop/ged/hw05-1.ged"
file_path1 = "C:/Users/twang/Desktop/ged/hw05-2.ged"
file_path2 = "C:/Users/twang/Desktop/ged/hw05-3.ged"
file_path3 = "C:/Users/twang/Desktop/ged/hw05-4.ged"
file_path4 = "C:/Users/twang/Desktop/ged/hw05-5.ged"

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
        self.assertEqual(listIndividualAges(allElements0), "Kevin James is 0 years old.\n")
    def test1(self):
        self.assertEqual(listIndividualAges(allElements1), "Kevin /James/ is 0 years old.\nTom /James/ is 2 years old.\nMicheal /James/ is 3 years old.\n")
    def test2(self):
        self.assertEqual(listIndividualAges(allElements2), "Kevin /James/ is 0 years old.\nTom /James/ is 2 years old.\nMicheal /James/ is 3 years old.\nJerry /James/ is 5 years old.\nMike /James/ is 4 years old.\n")
    def test3(self):
        self.assertEqual(listIndividualAges(allElements3), "Kevin /James/ is 0 years old.\nTom /James/ is 2 years old.\nMicheal /James/ is 3 years old.\nJerry /James/ is 5 years old.\nMike /James/ is 4 years old.\nHarry /James/ is 7 years old.\nJukebox /James/ is 6 years old.\n")
    def test4(self):
        self.assertEqual(listIndividualAges(allElements4), "Kevin /James/ is 0 years old.\nTom /James/ is 2 years old.\nMicheal /James/ is 3 years old.\nJerry /James/ is 5 years old.\nMike /James/ is 4 years old.\nHarry /James/ is 7 years old.\nJukebox /James/ is 6 years old.\nGiga /James/ is 9 years old.\nMega /James/ is 8 years old.\n")
  

if __name__ == '__main__':
    unittest.main()