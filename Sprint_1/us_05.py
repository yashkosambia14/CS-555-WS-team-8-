from ged4py.model import Individual
from ged4py.parser import GedcomReader

def US_help():
    dead_individuals = {}
    with GedcomReader('GEDCOM_YASH_KOSAMBIA_edit.ged') as parser:
        for count, individual in enumerate(parser.records0('INDI')):
            is_dead = str(individual.sub_tag_value("DEAT/DATE")).split(" ")
            if is_dead[0] != "None":
                dead_individuals[individual.xref_id] = int(is_dead[2])
    return dead_individuals

def US_05():
    dead = US_help()
    errors = []
    with GedcomReader('GEDCOM_YASH_KOSAMBIA_edit.ged') as parser:
        for count, family in enumerate(parser.records0('FAM')):
            if family.sub_tag("WIFE").xref_id in dead:
                cur_id = family.sub_tag("WIFE").xref_id
                marr = str(family.sub_tag_value('MARR/DATE')).split(" ")
                if marr[0] != "None":
                    marr_year = int(marr[2])
                    if dead[cur_id] < marr_year:
                        errors.append('US05: Individial ' + cur_id + ' has death before marriage')
            elif family.sub_tag("HUSB").xref_id in dead:
                cur_id =  family.sub_tag("HUSB").xref_id
                marr = str(family.sub_tag_value('MARR/DATE')).split(" ")
                if marr[0] != "None":
                    marr_year = int(marr[2])
                    if dead[cur_id] < marr_year:
                        errors.append('US05: Individial ' + cur_id + ' has death before marriage')

    return errors
if __name__ == "__main__":
   print(US_05())