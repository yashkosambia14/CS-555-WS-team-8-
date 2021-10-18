# YASH KOSAMBIA
# CWID 10475286
from ged4py import GedcomReader
from prettytable import PrettyTable

def divorce_before_death(table):  # US06: Divorce Before Death
    divorce_before_dead = True
    notes = []
    for fam in families:
        wife_name = get_individual(fam.wife).name
        hubby_name = get_individual(fam.husband).name

        for ind in individuals:
            if fam.divorce is not None:
                if ind.name == wife_name or ind.name == hubby_name:
                    if ind.death is not None and ind.death < fam.divorce:
                        notes.append("{} has an incorrect divorce and/or death date.".format(ind.name))
                        notes.append(
                            "Divorce is: {} and Death is: {}".format(format_date(fam.divorce), format_date(ind.death)))
                        divorce_before_dead = False
    if divorce_before_dead:
        result = "All divorces are before death dates."
    else:
        result = "One or more divorces are not before death dates"

    table.append(
        ["US06", "Divorce Before Death", "\n".join(notes), divorce_before_dead, result])
