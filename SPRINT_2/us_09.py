from ged4py.date import DateValueSimple
from ged4py.parser import GedcomReader
import datetime
from gedcom import __file__


DATES = {
    'JAN': 1,
    'FEB': 2,
    'MAR': 3,
    'APR': 4,
    'MAY': 5,
    'JUN': 6,
    'JUL': 7,
    'AUG': 8,
    'SEP': 9,
    'OCT': 10,
    'NOV': 11,
    'DEC': 12,
}

def US_09_get_fams():
    fam_obj = {}
    with GedcomReader('SPRINT_2\gedcom\export-BloodTree.ged') as parser:
        for count, family in enumerate(parser.records0('FAM')):
            fam_obj[family.xref_id] = {}
            fam_obj[family.xref_id]['Children'] = []
            child_count = 1
            for i, indi in enumerate(family.sub_records):
                if indi.tag == "WIFE":
                    fam_obj[family.xref_id]['Wife'] = indi.value
                elif indi.tag == "HUSB":
                    fam_obj[family.xref_id]['Husband'] = indi.value
                elif indi.tag == "CHIL":
                    fam_obj[family.xref_id]['Children'].append(indi.value)
                    child_count += 1
                elif indi.tag == "MARR":
                    for i, record in enumerate(indi.sub_records):
                        if record.tag == 'DATE':
                            date = str(record.value).split(" ")
                            new_date = datetime.datetime(int(date[2]), DATES[date[1]], int(date[0]))
                            fam_obj[family.xref_id]['Married'] = new_date

        return fam_obj

def US_09():
    print ("User Story 09")
    result = []
    fams = US_09_get_fams()
    with GedcomReader('SPRINT_2\gedcom\export-BloodTree.ged') as parser:
        for count, indi in enumerate(parser.records0('INDI')):
            if indi.sub_tag('FAMC'):
                fam_id = indi.sub_tag('FAMC').xref_id
                if indi.xref_id in fams[fam_id]['Children']:
                    if 'Married' in fams[fam_id]:
                        bday = str(indi.sub_tag_value('BIRT/DATE')).split(' ')
                        birthdate = datetime.datetime(int(bday[2]), DATES[bday[1]], int(bday[0]))
                        marr = fams[fam_id]['Married']
                        if birthdate <= marr:
                            result.append(indi.xref_id + " was born before parents marriage Family ID: " + fam_id)

    print(result)
    return result




if __name__ == "__main__":
   print(US_09())