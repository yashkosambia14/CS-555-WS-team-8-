from ged4py.date import DateValueSimple
from ged4py.parser import GedcomReader

def get_husband_name(id):
    with GedcomReader('Sprint_3\gedcom\export-BloodTree.ged') as parser:
        for count, indi in enumerate(parser.records0('INDI')):
            if indi.xref_id == id:
                return indi.sub_tag_value('NAME')[1]

def US_16_get_fams():
    fam_obj = {}
    with GedcomReader('Sprint_3\gedcom\export-BloodTree.ged') as parser:
        for count, family in enumerate(parser.records0('FAM')):
            fam_obj[family.xref_id] = {}
            fam_obj[family.xref_id]['Members'] = []
            for i, indi in enumerate(family.sub_records):
                if indi.value != "None":
                    fam_obj[family.xref_id]['Members'].append(indi.value)
                if indi.tag == "HUSB":
                    fam_obj[family.xref_id]['Male_Name'] = get_husband_name(indi.value)

        return fam_obj

def US_16():
    print ("User Story 16")
    result = []
    fams = US_16_get_fams()
    with GedcomReader('Sprint_3\gedcom\export-BloodTree.ged') as parser:
        for i, fam in enumerate(fams):
            for count, indi in enumerate(parser.records0('INDI')):
                if indi.xref_id in fams[fam]['Members'] and indi.sub_tag_value("SEX") == 'M':
                    indi_name = indi.sub_tag_value('NAME')[1]
                    if indi_name != fams[fam]['Male_Name']:
                        result.append('ERROR: ' + indi.xref_id + ' has family name different from Husband name in family: ' + fam)

    if len(result) > 0:
        return result
    else:
        return ["All Males have correct last names"]


if __name__ == "__main__":
   print(US_16())