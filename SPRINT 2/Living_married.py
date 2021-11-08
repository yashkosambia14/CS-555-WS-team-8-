#CS555 - TEAM 8 - YASH KOSAMBIA
import copy

import self as self
#from prettytable import PrettyTable
from ged4py.parser import GedcomReader
from ged4py.model import Individual

#preetyoutput = PrettyTable()
k = {}
b = {}
married_people = []
#preetyoutput.field_names = ['LIVING PEOPLE']
living_married_output = []


def US_help():
    dead_individuals = {}
    with GedcomReader('GEDCOM_YASH_KOSAMBIA.ged') as parser:
        for count, individual in enumerate(parser.records0('INDI')):
            # print(count, individual)
            is_dead = str(individual.sub_tag_value("DEAT/DATE")).split(" ")
            # print(is_dead)
            if is_dead[0] != "None":
                dead_individuals[individual.xref_id] = int(is_dead[0])
    return dead_individuals


with GedcomReader('GEDCOM_YASH_KOSAMBIA.ged') as parser:
    dead = US_help()
    # print(dead)
    living_married = []
    for i, fam in enumerate(parser.records0('FAM')):
        if fam.sub_tag("WIFE").xref_id not in dead:
            cur_id = fam.sub_tag("WIFE").xref_id
            living_married.append(cur_id)
        elif fam.sub_tag("HUSB").xref_id not in dead:
            cur_id = fam.sub_tag("HUSB").xref_id
            living_married.append(cur_id)
    # print(living_married)
    for i, indi in enumerate(parser.records0('INDI')):
        if indi.xref_id in living_married:
            living_married_output.append(indi.name.format())
print('\n\nLiving Married \n\n', living_married_output)






'IF INCASE IMPORTING DOES NOT WORK FOR SEPERATE TEST FILE DUE TO LIB, TESTCASES ARE HERE'


import unittest

#print(living_married_out)
class TestStringMethods(unittest.TestCase):
    def test_living_married_testcase1(self):
        result = ''
        expected_output = 'JAYESH KOSAMBIA'
        if expected_output in living_married_output:
            result = expected_output
        self.assertEqual(result, expected_output)

    def test_living_married_testcase2(self):
        result2 = ''
        expected_output2 = 'KAMLA MARKER'
        if expected_output2 in living_married_output:
            result2 = expected_output2
        self.assertEqual(result2, expected_output2)

    def test_living_married_testcase3(self):
        result3 = ''
        expected_output3 = 'PARVATIBEN KOSAMBIA'
        if expected_output3 in living_married_output:
            result3 = expected_output3
        self.assertEqual(result3, expected_output3)

    def test_living_married_testcase4(self):
        result4 = ''
        expected_output4 = 'DIVYA KOSAMBIA'
        if expected_output4 in living_married_output:
            result4 = expected_output4
        self.assertEqual(result4, expected_output4)

    def test_living_married_testcase(self):
        result5 = ''
        expected_output5 = 'MEENA PARMAR'
        if expected_output5 in living_married_output:
            result5 = expected_output5
        self.assertEqual(result5, expected_output5)

    #def test_living_married(self):
        #self.asserIn('JAYESH KOSAMBIA', )

if __name__ == '__main__':
    unittest.main()







































