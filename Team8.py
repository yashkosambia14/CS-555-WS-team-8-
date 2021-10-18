# CS 555 Project 03
# Thomas Wang, Yash Kosambia, Patrick Pondo

from ged4py import GedcomReader
from prettytable import PrettyTable
import unittest
from Sprint_1.US01test import *
from Sprint_1.US27test import *
from Sprint_1.us_03_test import *
from Sprint_1.us_04_test import *
# from Sprint_1.us_05_test import *
# from Sprint_1.us_06_test import *


individual_table = PrettyTable()
individual_table.field_names = ["Id", "full_name", "Gender", "Birthday","Alive", "death","Child","spouse"]
family_table = PrettyTable()
family_table.field_names = ["Id","Married", "Divorce", "Husband Name", "Husband Id", "Wife Name", "Wife Id", "Children"]



def print_individuals():
    with GedcomReader('GEDCOM_YASH_KOSAMBIA.ged') as parser:
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
    with GedcomReader('GEDCOM_YASH_KOSAMBIA.ged') as parser:
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
    unittest.main(exit=False)
    print("Individuals")
    print(print_individuals())
    print("Families")
    print(print_families())
    
"""
OUTPUT :
Individuals
+-------+----------------------+--------+-------------+-------+-------------+-------+--------+
|   Id  |      full_name       | Gender |   Birthday  | Alive |    death    | Child | spouse |
+-------+----------------------+--------+-------------+-------+-------------+-------+--------+
|  @I1@ | YASH JAYESH KOSAMBIA |   M    | 14 JUN 1995 |  True |     None    |  @F1@ |  None  |
|  @I2@ |   JAYESH KOSAMBIA    |   M    | 18 MAR 1963 |  True |     None    |  @F3@ |  @F1@  |
|  @I3@ |     ALKA MARKER      |   F    | 28 SEP 1968 | False |  2 JAN 2013 |  @F4@ |  @F1@  |
|  @I4@ |    MANILAL MARKER    |   M    | 10 FEB 1920 |  True |     None    |  None |  @F4@  |
|  @I5@ |     KAMLA MARKER     |   F    | 12 OCT 1921 |  True |     None    |  None |  @F4@  |
|  @I6@ |  PREMCHAND KOSAMBIA  |   M    |  8 JUN 1922 | False |  7 AUG 1995 |  @F5@ |  @F3@  |
|  @I7@ | PARVATIBEN KOSAMBIA  |   F    |  8 MAR 1921 |  True |     None    |  None |  @F3@  |
|  @I8@ |   PRADIP KOSAMBIA    |   M    | 21 MAY 1960 |  True |     None    |  @F3@ |  @F7@  |
|  @I9@ |   BHAVIKA KOSAMBIA   |   F    |  1 APR 1997 |  True |     None    |  @F1@ |  None  |
| @I10@ |   KANCHAN KOSAMBIA   |   F    |  7 APR 1964 |  True |     None    |  None |  @F7@  |
| @I11@ |     MEENA PARMAR     |   F    |  6 JUL 1970 |  True |     None    |  None |  @F8@  |
| @I12@ |    JAYESH MARKER     |   M    |  7 MAY 1970 |  True |     None    |  @F4@ |  None  |
| @I13@ |    RAJU KOSAMBIA     |   M    |  4 JUN 1987 |  True |     None    |  @F8@ |  None  |
| @I14@ |    HEER KOSAMBIA     |   M    |  5 MAY 2001 |  True |     None    |  @F7@ |  None  |
| @I15@ |    DAVID KOSAMBIA    |   M    |  6 JUN 1840 | False | 17 SEP 1928 |  @F9@ |  @F5@  |
| @I16@ |   SHEELA KOSAMBIA    |   F    |  4 AUG 1840 | False | 28 JUL 1945 |  None |  @F5@  |
| @I17@ |    ANIL KOSAMBIA     |   M    |  7 OCT 1972 |  True |     None    |  @F3@ | @F10@  |
| @I18@ |    MAHEK KOSAMBIA    |   F    |  7 JUN 2005 |  True |     None    | @F10@ |  None  |
| @I19@ |     HARSA PATEL      |   F    |  5 DEC 1981 |  True |     None    |  None | @F10@  |
| @I20@ |   YASHVI KOSAMBIA    |   F    | 10 APR 2004 |  True |     None    | @F11@ |  None  |
| @I21@ |    DIVYA KOSAMBIA    |   F    | 10 OCT 1968 |  True |     None    |  None | @F11@  |
| @I22@ |   RAMESH KOSAMBIA    |   M    | 11 APR 1818 | False | 25 NOV 1888 |  None |  @F9@  |
| @I23@ |   KAVITA KOSAMBIA    |   F    |  5 AUG 1821 | False | 13 NOV 1890 |  None |  @F9@  |
| @I24@ |    RAMESH PANCHAL    |   M    |     None    |  True |     None    |  None |  @F6@  |
| @I25@ |  SARASWATI Dumasiya  |   F    |  7 JAN 1973 |  True |     None    |  None |  @F2@  |
| @I26@ |   VASUDEV KOSAMBIA   |   M    | 15 APR 2019 |  True |     None    |  @F2@ |  None  |
| @I27@ |    KIRIT PANCHAL     |   M    |  6 FEB 2001 |  True |     None    |  @F6@ |  None  |
+-------+----------------------+--------+-------------+-------+-------------+-------+--------+
Families
+-------+-------------+------------+--------------------+------------+---------------------+---------+---------------------------+
|   Id  |   Married   |  Divorce   |    Husband Name    | Husband Id |      Wife Name      | Wife Id |          Children         |
+-------+-------------+------------+--------------------+------------+---------------------+---------+---------------------------+
|  @F1@ | 14 FEB 1992 |    None    |  JAYESH KOSAMBIA   |    @I2@    |     ALKA MARKER     |   @I3@  |      ['@I1@', '@I9@']     |
|  @F2@ | 25 MAR 2018 |    None    |  JAYESH KOSAMBIA   |    @I2@    |  SARASWATI Dumasiya |  @I25@  |         ['@I26@']         |
|  @F3@ |     None    |    None    | PREMCHAND KOSAMBIA |    @I6@    | PARVATIBEN KOSAMBIA |   @I7@  | ['@I2@', '@I8@', '@I17@'] |
|  @F4@ | 10 MAY 1942 |    None    |   MANILAL MARKER   |    @I4@    |     KAMLA MARKER    |   @I5@  |     ['@I3@', '@I12@']     |
|  @F5@ |     None    |    None    |   DAVID KOSAMBIA   |   @I15@    |   SHEELA KOSAMBIA   |  @I16@  |          ['@I6@']         |
|  @F6@ | 26 APR 1998 |    None    |   RAMESH PANCHAL   |   @I24@    | PARVATIBEN KOSAMBIA |   @I7@  |         ['@I27@']         |
|  @F7@ | 14 JUL 1989 |    None    |  PRADIP KOSAMBIA   |    @I8@    |   KANCHAN KOSAMBIA  |  @I10@  |         ['@I14@']         |
|  @F8@ | 11 FEB 1986 | 9 JAN 1988 |  PRADIP KOSAMBIA   |    @I8@    |     MEENA PARMAR    |  @I11@  |         ['@I13@']         |
|  @F9@ |     None    |    None    |  RAMESH KOSAMBIA   |   @I22@    |   KAVITA KOSAMBIA   |  @I23@  |         ['@I15@']         |
| @F10@ |     None    |    None    |   ANIL KOSAMBIA    |   @I17@    |     HARSA PATEL     |  @I19@  |         ['@I18@']         |
| @F11@ |  4 FEB 1999 |    None    |   ANIL KOSAMBIA    |   @I17@    |    DIVYA KOSAMBIA   |  @I21@  |         ['@I20@']         |
+-------+-------------+------------+--------------------+------------+---------------------+---------+---------------------------+
    """
