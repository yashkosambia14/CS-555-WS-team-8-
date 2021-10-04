# CS 555 Project 03
# Thomas Wang, Yash Kosambia, Patrick Pondo

from ged4py import GedcomReader

def print_individuals():
    with GedcomReader('export-BloodTree.ged') as parser:
        for i, indi in enumerate(parser.records0("INDI")):
            id = indi.xref_id 
            name_item = indi.sub_tag_value('NAME') 
            full_name = name_item[0] + ' ' +name_item[1] 
            bday = indi.sub_tag_value('BIRT/DATE' )
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
            
            print(str(id) + "  " + str(full_name) + "  " + str(gender) + "  " + str(bday) + "  " + str(alive) + "  " + str(dead_date) + "  " + str(child_rec) + "  " + str(spouse_rec))

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
            print(str(id) + " " + str(married) + " " + str(divorced) + " " + str(husband_name) + " " + str(husband_id) + " " + str(wife_name) + " " + str(wife_id) + " " + str(list(children)) )

if __name__ == "__main__":
    # print_individuals()
    print_families()
