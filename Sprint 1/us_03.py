import unittest
import datetime
from ged4py.parser import GedcomReader

def change_to_int(month):
    if month == "JAN":
        return 1
    elif month == "FEB":
        return 2
    elif month == "MAR":
        return 3
    elif month == "APR":
        return 4
    elif month == "MAY":
        return 5
    elif month == "JUN":
        return 6
    elif month == "JUL":
        return 7
    elif month == "AUG":
        return 8
    elif month == "SEP":
        return 9
    elif month == "OCT":
        return 10
    elif month == "NOV":
        return 11
    else:
        return 12


def US_03():
    errors = []
    with GedcomReader('GEDCOM_YASH_KOSAMBIA.ged') as parser:
        for count, individual in enumerate(parser.records0("INDI")):
            birth = str(individual.sub_tag_value('BIRT/DATE')).split(" ")
            death = str(individual.sub_tag_value('DEAT/DATE')).split(" ")
            if birth[0] != "None" and death[0] != "None":
                birth_month = change_to_int(birth[1])
                birth_date = datetime.datetime(int(birth[2]), birth_month, int(birth[0]))
                death_month = change_to_int(death[1])
                death_date = datetime.datetime(int(death[2]), death_month, int(death[0]))
                if birth_date > death_date:
                    error_str = str("ERROR: " + individual.xref_id + " has death before birth")
                    errors.append(error_str)
                    print(error_str)
            elif birth[0] == "None" and death[0] != "None":
                error_str = str("ERROR: " + individual.xref_id + " has death before birth")
                errors.append(error_str)
                print("ERROR: " + individual.xref_id + " has death before birth")
        return errors

class TEST_US_03(unittest.TestCase):
    result = US_03()
    def test_US_03_1(self):
        desired_output = ['ERROR: @I6@ has death before birth']
        self.assertEqual(self.result, desired_output)
    def test_US_03_2(self):
        self.assertTrue(self.result.count('ERROR: @I6@ has death before birth') > 0)
    def test_US_03_3(self):
        self.assertFalse(self.result.count('ERROR: @I2@ has death before birth') > 0)
    def test_US_03_4(self):
        self.assertFalse(self.result.count('ERROR: @I4@ has death before birth') > 0)
    def test_US_03_5(self):
        self.assertFalse(self.result.count('ERROR: @I11@ has death before birth') > 0)


if __name__ == "__main__":
    unittest.main(exit=False)
