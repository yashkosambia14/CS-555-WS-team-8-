from ged4py.date import DateValueSimple
from ged4py.parser import GedcomReader
import datetime


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

def US_10_get_fams():
    fam_obj = {}
    with GedcomReader('SPRINT_2\gedcom\export-BloodTree.ged') as parser:
        for count, family in enumerate(parser.records0('FAM')):
            fam_obj[family.xref_id] = {}
            for i, indi in enumerate(family.sub_records):
                if indi.tag == "WIFE":
                    fam_obj[family.xref_id]['Wife'] = indi.value
                elif indi.tag == "HUSB":
                    fam_obj[family.xref_id]['Husband'] = indi.value
                elif indi.tag == "MARR":
                    for i, record in enumerate(indi.sub_records):
                        if record.tag == 'DATE':
                            date = str(record.value).split(" ")
                            new_date = datetime.datetime(int(date[2]), DATES[date[1]], int(date[0]))
                            fam_obj[family.xref_id]['Married'] = new_date

        return fam_obj

def US_10():
    print ("User Story 10")
    result = []
    fams = US_10_get_fams()
    with GedcomReader('SPRINT_2\gedcom\export-BloodTree.ged') as parser:
        for count, indi in enumerate(parser.records0('INDI')):
            if indi.sub_tag('FAMS'):
                fam_id = indi.sub_tag('FAMS').xref_id
                if indi.xref_id == fams[fam_id]['Husband'] or  indi.xref_id == fams[fam_id]['Wife']:
                    if 'Married' in fams[fam_id]:
                        bday = str(indi.sub_tag_value('BIRT/DATE')).split(' ')
                        birthdate = datetime.datetime(int(bday[2]), DATES[bday[1]], int(bday[0]))
                        marr = fams[fam_id]['Married']
                        years_at_marr = int(((marr - birthdate).days)/365)
                        if years_at_marr < 14:
                            result.append(indi.xref_id + " was married before age 14, Age: " + str(years_at_marr))

    print(result)
    return result


if __name__ == "__main__":
   print(US_10())