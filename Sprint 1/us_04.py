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


def US_04():
    errors = []
    with GedcomReader('GEDCOM_YASH_KOSAMBIA_edit.ged') as parser:
        for count, family in enumerate(parser.records0("FAM")):
            marr = str(family.sub_tag_value('MARR/DATE')).split(" ")
            div = str(family.sub_tag_value('DIV/DATE')).split(" ")
            print(count)
            if marr[0] != "None" and div[0] != "None":
                marr_month = change_to_int(marr[1])
                marr_date = datetime.datetime(int(marr[2]), marr_month, int(marr[0]))
                div_month = change_to_int(div[1])
                div_date = datetime.datetime(int(div[2]), div_month, int(div[0]))
                if marr_date > div_date:
                    error_str = str("ERROR: " + family.xref_id + " has divorce before marriage")
                    errors.append(error_str)
                    print("ERROR: " + family.xref_id + " has divorce before marriage")
            elif marr[0] == "None" and div[0] != "None":
                error_str = str("ERROR: " + family.xref_id + " has divorce before marriage")
                errors.append(error_str)
                print("ERROR: " + family.xref_id + " has divorce before marriage")

        return errors


