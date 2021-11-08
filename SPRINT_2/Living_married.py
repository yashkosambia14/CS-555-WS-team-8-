#CS555 - TEAM 8 - YASH KOSAMBIA
import copy

#from prettytable import PrettyTable
from ged4py.parser import GedcomReader
from ged4py.model import Individual

#preetyoutput = PrettyTable()
k = {}
b = {}
married_people = []
#preetyoutput.field_names = ['LIVING PEOPLE']
living_married_output = []


def US_help():
    dead_individuals = {}
    with GedcomReader('GEDCOM_YASH_KOSAMBIA.ged') as parser:
        for count, individual in enumerate(parser.records0('INDI')):
            # print(count, individual)
            is_dead = str(individual.sub_tag_value("DEAT/DATE")).split(" ")
            # print(is_dead)
            if is_dead[0] != "None":
                dead_individuals[individual.xref_id] = int(is_dead[0])
    return dead_individuals


with GedcomReader('GEDCOM_YASH_KOSAMBIA.ged') as parser:
    dead = US_help()
    # print(dead)
    living_married = []
    for i, fam in enumerate(parser.records0('FAM')):
        if fam.sub_tag("WIFE").xref_id not in dead:
            cur_id = fam.sub_tag("WIFE").xref_id
            living_married.append(cur_id)
        elif fam.sub_tag("HUSB").xref_id not in dead:
            cur_id = fam.sub_tag("HUSB").xref_id
            living_married.append(cur_id)
    # print(living_married)
    for i, indi in enumerate(parser.records0('INDI')):
        if indi.xref_id in living_married:
            living_married_output.append(indi.name.format())
print('\n\nLiving Married US 31 \n\n', living_married_output)



