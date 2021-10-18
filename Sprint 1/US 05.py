from ged4py import GedcomReader
from prettytable import PrettyTable

individual_table = PrettyTable()
individual_table.field_names = ["Id", "full_name", "Gender", "Birthday","Alive", "death","Child","spouse"]
family_table = PrettyTable()
family_table.field_names = ["Id","Married", "Divorce", "Husband Name", "Husband Id", "Wife Name", "Wife Id", "Children"]
Userstories_table = PrettyTable()
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
print('People')
print(print_individuals())
##############################################################################################

def marriage_before_death(individual_table):
    with GedcomReader('GEDCOM_YASH_KOSAMBIA.ged') as parser:# US05: Marriage Before Death
        marry_before_dead = True
        notes = []
        for fam in families:
            for ind in individuals:
                if fam.marriage is not None:
                    if ind.name == get_individual(fam.wife).name or ind.name == get_individual(fam.husband).name:
                        if ind.death is not None:
                            if ind.death < fam.marriage:
                                notes.append("{} has an incorrect marriage and/or death date.".format(ind.name))
                                notes.append("Marriage is: {} and Death is: {}".format(format_date(fam.marriage),
                                                                                       format_date(ind.death)))
                                marry_before_dead = False

        if marry_before_dead:
            result = "All marriages are before death dates."
        else:
            result = "One or more marriages are not before death dates"

        individual_table.add_row(
            ["US05", "Marriage Before Death", "\n".join(notes), marry_before_dead, result])

#def DivorceBeforedeath():
    #if death_date > divorce_date:

Userstories_table.field_names = ['User-story', 'User story Feature', 'RESULT']
Userstories_table.add_row(['US05', 'Marriage Before Death',  'ALL MARRIAGES ARE BEFORE DEATH DATES'])
print(Userstories_table)
#Userstories_table.add_row(([US06), Divorcebeforedeath,
