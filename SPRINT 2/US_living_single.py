from ged4py.model import Individual
from ged4py.parser import GedcomReader

living = []
living_married = []
living_single = []
living_single_output = []


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


with GedcomReader("GEDCOM_YASH_KOSAMBIA.ged") as parser:
    for i, indi in enumerate(parser.records0("INDI")):
        living_curid = indi.xref_id
        living.append(living_curid)
    #print(living)

    dead = US_help()
    for i, fam in enumerate(parser.records0('FAM')):
        if fam.sub_tag("WIFE").xref_id not in dead:
            cur_id = fam.sub_tag("WIFE").xref_id
            living_married.append(cur_id)
        elif fam.sub_tag("HUSB").xref_id not in dead:
            cur_id = fam.sub_tag("HUSB").xref_id
            living_married.append(cur_id)
#print(living_married)
#print(living)

for i in living:
    if i not in living_married:
        living_single.append(i)
#print(living_single)

with GedcomReader('GEDCOM_YASH_KOSAMBIA.ged') as parser:
    for i, indi in enumerate(parser.records0('INDI')):
        if indi.xref_id in living_single:
            living_single_output.append(indi.name.format())

print('\n\nLIVING SINGLES\n\n', living_single_output)


'IF IMPORTING THE FILE DOES NOT IMPORTS DUE TO LIB, I HAVE TESTS HERE TO CHECK RUNNING TESTS'

''''''

import unittest

class TestStringMethods(unittest.TestCase):
    def test_living_singles_testcase1(self):
        result = ''
        expected_output = 'YASH JAYESH KOSAMBIA'
        if expected_output in living_single_output:
            result = expected_output
        self.assertEqual(result, expected_output)

    def test_living_singles_testcase2(self):
        result2 = ''
        expected_output2 = 'MANILAL MARKER'
        if expected_output2 in living_single_output:
            result2 = expected_output2
        self.assertEqual(result2, expected_output2)

    def test_living_singles_testcase3(self):
        result3 = ''
        expected_output3 = 'ANIL KOSAMBIA'
        if expected_output3 in living_single_output:
            result3 = expected_output3
        self.assertEqual(result3, expected_output3)

    def test_living_singles_testcase4(self):
        result4 = ''
        expected_output4 = 'MANILAL MARKER'
        if expected_output4 in living_single_output:
            result4 = expected_output4
        self.assertEqual(result4, expected_output4)

    def test_living_singles_testcase5(self):
        result5 = ''
        expected_output5 = 'MANILAL MARKER'
        if expected_output5 in living_single_output:
            result5 = expected_output5
        self.assertEqual(result5, expected_output5)

if __name__ == '__main__':
    unittest.main()

