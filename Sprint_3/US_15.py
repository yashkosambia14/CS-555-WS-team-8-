from ged4py.date import DateValueSimple
from ged4py.parser import GedcomReader

def US_15_get_fams():
    fam_obj = {}
    with GedcomReader('Sprint_3\gedcom\export-BloodTree.ged') as parser:
        for count, family in enumerate(parser.records0('FAM')):
            fam_obj[family.xref_id] = []
            for i, indi in enumerate(family.sub_records):
                if indi.tag == "CHIL":
                    fam_obj[family.xref_id].append(indi.value)
        return fam_obj

def US_15():
    print ("User Story 15")
    result = []
    fams = US_15_get_fams()
    for i, fam in enumerate(fams):
        if len(fams[fam]) > 15:
            result.append(fam + 'has more than 15 siblings')
            print(fam + 'has more than 15 siblings')
            

    if len(result) > 0:
        return result
    else:
        return ["All Families have fewer than 15 siblings"]


if __name__ == "__main__":
   print(US_15())