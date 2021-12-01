from ged4py.parser import GedcomReader
from ged4py.model import Individual
from datetime import date


today = date.today()
d4 = today.strftime("%d-%b-%Y")
today_date = list(d4.split('-'))
current_month = today_date[1]
date_today = today_date[0]
year_today = today_date[2]
print("\n\nUser Story 36 List Recent Deaths\n\n")
# Global variables
deathdays = []


def US_36():
    with GedcomReader('GEDCOM_YASH_KOSAMBIA.ged') as parser:
        for count, individual in enumerate(parser.records0('INDI')):

            deathday = str(individual.sub_tag_value("DEAT/DATE")).split(" ")
            names = str(individual.name.format())
            deathdays.append([names, deathday])
            iter_name_death = [names, deathday]
            #print(deathday)
            mo = ''
            try:
                mo = deathday[1]
                ye = deathday[2]

            except:
                pass

            if current_month == mo.capitalize():
                if year_today == ye:
                    print('Recent Death Found:', iter_name_death)

            else:
                print('No recent Death Found', iter_name_death)



US_36()


