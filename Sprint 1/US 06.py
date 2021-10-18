# YASH KOSAMBIA
# CWID 10475286
from ged4py import GedcomReader
from prettytable import PrettyTable

def marriage_before_divorce(table):  # US04: Marriage Before Divorce
    marry_before_divorce = True
    notes = []
    for fam in families:
        if fam.divorce is not None and fam.marriage is not None:
            if fam.divorce < fam.marriage:
                notes.append("{} and {} have a marriage before their divorce".format(get_individual(fam.husband),
                                                                                     get_individual(fam.wife)))
                notes.append(
                    "Marriage is: {} and divorce is: {}".format(format_date(fam.marriage), format_date(fam.divorce)))
                marry_before_divorce = False

    if marry_before_divorce:
        result = "All marriage and divorce dates are correct."
    else:
        result = "One or more marriage/divorce dates are incorrect."

    table.append(
        ["US04", "Marriage Before Divorce", "\n".join(notes), marry_before_divorce, result])

