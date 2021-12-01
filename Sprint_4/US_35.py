from ged4py.parser import GedcomReader
from ged4py.model import Individual
from datetime import date
print("\n\nUser Story 35 List Recent Births\n\n")

today = date.today()
d4 = today.strftime("%d-%b-%Y")
today_date = list(d4.split('-'))
current_month = today_date[1]
date_today = today_date[0]
year_today = today_date[2]
#print('current month', current_month.capitalize())

month_year_today = [current_month, year_today]
#print(month_year)
# Global variables

birthdays = []
def US_35():
    with GedcomReader('GEDCOM_YASH_KOSAMBIA.ged') as parser:
        for count, individual in enumerate(parser.records0('INDI')):

            birthday = str(individual.sub_tag_value("BIRT/DATE")).split(" ")
            names = str(individual.name.format())

            birthdays.append([names, birthday])
            iter_name_birth = [names, birthday]
            try:
                m = birthday[1]
                y = birthday[2]
            except:
                pass

            if current_month == m.capitalize():
                if year_today == y:
                    print('Recent Birth Found:', iter_name_birth)

            else:
                print('No recent Births Found', iter_name_birth)


US_35()
