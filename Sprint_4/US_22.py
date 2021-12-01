from ged4py.parser import GedcomReader

def US_22_get_fams():
    fam_list = []
    with GedcomReader('gedcom\export-BloodTree.ged') as parser:
        for count, family in enumerate(parser.records0('FAM')):
            fam_list.append(family.xref_id)

    return fam_list

def US_22_get_individuals(list):
    id_list = list
    with GedcomReader('gedcom\export-BloodTree.ged') as parser:
        for count, indi in enumerate(parser.records0('INDI')):
            id_list.append(indi.xref_id)

    return id_list
            
def US_22_duplicates(list):
    duplicates = []
    setOfElements = set()
    for elem in list:
        if elem in setOfElements:
            duplicates.append(elem)
            print(elem + " is a duplicate value")
        else:
            setOfElements.add(elem)    

    if len(duplicates) > 0:
        return duplicates
    else:
        return "No duplicates found"

def US_22():
    print ("User Story 22")
    fams = US_22_get_fams()
    id_list = US_22_get_individuals(fams)
    dups = US_22_duplicates(id_list)

    return dups


if __name__ == "__main__":
   print(US_22())