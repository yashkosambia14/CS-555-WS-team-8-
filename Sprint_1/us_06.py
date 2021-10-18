from ged4py.model import Individual
from ged4py.parser import GedcomReader

def US_help():
    dead_individuals = {}
    with GedcomReader('Sprint_1\gedcom\GEDCOM_YASH_KOSAMBIA_edit.ged') as parser:
        for count, individual in enumerate(parser.records0('INDI')):
            is_dead = str(individual.sub_tag_value("DEAT/DATE")).split(" ")
            if is_dead[0] != "None":
                dead_individuals[individual.xref_id] = int(is_dead[2])
    return dead_individuals

def US_06():
    print ("User Story 06")
    dead = US_help()
    errors = []
    with GedcomReader('Sprint_1\gedcom\GEDCOM_YASH_KOSAMBIA_edit.ged') as parser:
        for count, family in enumerate(parser.records0('FAM')):
            if family.sub_tag("WIFE").xref_id in dead:
                cur_id = family.sub_tag("WIFE").xref_id
                div = str(family.sub_tag_value('DIV/DATE')).split(" ")
                if div[0] != "None":
                    div_year = int(div[2])
                    if dead[cur_id] < div_year:
                        print('US06: Individial ' + cur_id + ' has death before divorce')
                        errors.append('US06: Individial ' + cur_id + ' has death before divorce')
            elif family.sub_tag("HUSB").xref_id in dead:
                cur_id =  family.sub_tag("HUSB").xref_id
                div = str(family.sub_tag_value('DIV/DATE')).split(" ")
                if div[0] != "None":
                    div_year = int(div[2])
                    if dead[cur_id] < div_year:
                        print('US06: Individial ' + cur_id + ' has death before divorce')
                        errors.append('US06: Individial ' + cur_id + ' has death before divorce')

    return errors
if __name__ == "__main__":
   print(US_06())