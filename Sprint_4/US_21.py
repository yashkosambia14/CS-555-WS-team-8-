from ged4py.parser import GedcomReader

def US_21_get_fams():
    fam_obj = {}
    with GedcomReader('Sprint_4\gedcom\export-BloodTree.ged') as parser:
        for count, family in enumerate(parser.records0('FAM')):
            fam_obj[family.xref_id] = []
            for i, indi in enumerate(family.sub_records):
                if indi.tag == "HUSB":
                    fam_obj[family.xref_id].append(["HUSB", indi.value])
                elif indi.tag == "WIFE":
                    fam_obj[family.xref_id].append(["WIFE", indi.value])
        return fam_obj

def check_gender(role, person):
    with GedcomReader('Sprint_4\gedcom\export-BloodTree.ged') as parser:
        for count, indi in enumerate(parser.records0('INDI')):
            if indi.xref_id == person:
                if indi.sub_tag_value("SEX") == "M" and role == "HUSB":
                    return True
                elif indi.sub_tag_value("SEX") == "F" and role == "WIFE":
                    return True
                else:
                    return False

def US_21():
    print ("User Story 21")
    result = []
    fams = US_21_get_fams()
    for i, fam in enumerate(fams):
        for i, tuple in enumerate(fams[fam]):
            if check_gender(tuple[0], tuple[1]) == False:
                result.append("Error: " + tuple[0] + ' has incorrect gender role in family ' + fam)
                print(tuple[0] + ' has incorrect gender role in family ' + fam)
            

    if len(result) > 0:
        return result
    else:
        return ["All Families have correct gender roles"]


if __name__ == "__main__":
   print(US_21())