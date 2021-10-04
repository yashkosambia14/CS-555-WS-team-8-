# CS 555 Project 03
# Thomas Wang, Yash Kosambia, Patrick Pondo

from ged4py import GedcomReader
from prettytable import PrettyTable

individual_table = PrettyTable()
individual_table.field_names = ["Id", "full_name", "Gender", "Birthday","Alive", "death","Child","spouse"]
family_table = PrettyTable()
family_table.field_names = ["Id","Married", "Divorce", "Husband Name", "Husband Id", "Wife Name", "Wife Id", "Children"]



def print_individuals():
    with GedcomReader('export-BloodTree.ged') as parser:
        for i, indi in enumerate(parser.records0("INDI")):
            id = indi.xref_id
            name_item = indi.sub_tag_value('NAME')
            full_name = name_item[0] + ' ' + name_item[1]
            bday = indi.sub_tag_value('BIRT/DATE')
            gender = indi.sub_tag_value('SEX')

            child_rec = indi.sub_tag('FAMC')
            if child_rec:
                child_rec = child_rec.xref_id

            spouse_rec = indi.sub_tag('FAMS')
            if spouse_rec:
                spouse_rec = spouse_rec.xref_id

            dead_date = indi.sub_tag_value("DEAT/DATE")
            if dead_date:
                alive = 'False'
            else:
                alive = 'True'

            individual_table.add_row([str(id), str(full_name) , str(gender) ,str(bday), str(alive), str(dead_date), str(child_rec), str(spouse_rec)])
    return individual_table



def get_id(record):
    return record.xref_id


def print_families():
    with GedcomReader('export-BloodTree.ged') as parser:
        for i, fam in enumerate(parser.records0("FAM")):
            id = fam.xref_id
            married = fam.sub_tag_value('MARR/DATE')
            divorced = fam.sub_tag_value('DIV/DATE')

            husband_item = fam.sub_tag("HUSB").sub_tag_value('NAME')
            husband_name = husband_item[0] + ' ' + husband_item[1]
            husband_id = fam.sub_tag('HUSB').xref_id

            wife_item = fam.sub_tag("WIFE").sub_tag_value('NAME')
            wife_name = wife_item[0] + ' ' + wife_item[1]
            wife_id = fam.sub_tag('WIFE').xref_id

            children_records = fam.sub_tags('CHIL')
            children = map(get_id, children_records)
            family_table.add_row([str(id), str(married),str(divorced),str(husband_name), str(husband_id), str(wife_name), str(wife_id), str(list(children))])
    return family_table




if __name__ == "__main__":
    print("Individuals")
    print(print_individuals())
    print("Families")
    print(print_families())
    
    
"""
OUTPUT :
Individuals
+------------------------+---------------+--------+-------------------+-------+------------+------------------------+------------------------+
|           Id           |   full_name   | Gender |      Birthday     | Alive |   death    |         Child          |         spouse         |
+------------------------+---------------+--------+-------------------+-------+------------+------------------------+------------------------+
| @I6000000178651056825@ | Patrick Pondo |   M    | ABOUT 15 AUG 1996 |  True |    None    | @F6000000178649813884@ |          None          |
| @I6000000178649813881@ |  Jerry Pondo  |   M    |    27 AUG 1963    |  True |    None    | @F6000000178651468826@ | @F6000000178649813884@ |
| @I6000000178650335890@ |   Anna Brown  |   F    | ABOUT 27 DEC 1965 |  True |    None    | @F6000000178651156829@ | @F6000000178649813884@ |
| @I6000000178651509823@ |  Philip Pondo |   M    | ABOUT 15 AUG 1996 |  True |    None    | @F6000000178649813884@ |          None          |
| @I6000000178650732886@ |  Eliza Pondo  |   F    | ABOUT 17 SEP 2002 |  True |    None    | @F6000000178649813884@ |          None          |
| @I6000000178650633899@ |   Mary Pondo  |   F    | ABOUT 21 MAY 1940 | False |    1997    |          None          | @F6000000178651468826@ |
| @I6000000178651468821@ | Michael Pondo |   M    |    27 AUG 1937    | False | ABOUT 2007 |          None          | @F6000000178651468826@ |
| @I6000000178651156824@ |   Dan Brown   |   M    |  ABOUT 1 JAN 1932 | False | ABOUT 1970 |          None          | @F6000000178651156829@ |
| @I6000000178651276822@ |   Elle Brown  |   F    |     1 MAR 1937    |  True |    None    |          None          | @F6000000178651423825@ |
| @I6000000178651573833@ |   Beth Brown  |   F    |     5 APR 1961    |  True |    None    | @F6000000178651156829@ |          None          |
| @I6000000178651774821@ |   Adam Brown  |   M    |    27 DEC 1963    |  True |    None    | @F6000000178651156829@ |          None          |
| @I6000000178651423821@ |  Allen Smith  |   M    |  ABOUT 6 FEB 1939 |  True |    None    |          None          | @F6000000178651423825@ |
| @I6000000178651356823@ |  Billy Smith  |   M    | ABOUT 14 JUN 1972 |  True |    None    | @F6000000178651423825@ |          None          |
+------------------------+---------------+--------+-------------------+-------+------------+------------------------+------------------------+
Families
+------------------------+------------------+---------+---------------+------------------------+------------+------------------------+--------------------------------------------------------------------------------+
|           Id           |     Married      | Divorce |  Husband Name |       Husband Id       | Wife Name  |        Wife Id         |                                    Children                                    |
+------------------------+------------------+---------+---------------+------------------------+------------+------------------------+--------------------------------------------------------------------------------+
| @F6000000178649813884@ |       None       |   None  |  Jerry Pondo  | @I6000000178649813881@ | Anna Brown | @I6000000178650335890@ | ['@I6000000178651056825@', '@I6000000178651509823@', '@I6000000178650732886@'] |
| @F6000000178651468826@ |   28 OCT 1960    |   None  | Michael Pondo | @I6000000178651468821@ | Mary Pondo | @I6000000178650633899@ |                           ['@I6000000178649813881@']                           |
| @F6000000178651156829@ | ABOUT 5 FEB 1960 |   None  |   Dan Brown   | @I6000000178651156824@ | Elle Brown | @I6000000178651276822@ | ['@I6000000178651573833@', '@I6000000178651774821@', '@I6000000178650335890@'] |
| @F6000000178651423825@ |   10 OCT 1971    |   None  |  Allen Smith  | @I6000000178651423821@ | Elle Brown | @I6000000178651276822@ |                           ['@I6000000178651356823@']                           |
+------------------------+------------------+---------+---------------+------------------------+------------+------------------------+--------------------------------------------------------------------------------+
    """
