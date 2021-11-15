# CS555ws - TEAM - 8
from ged4py.parser import GedcomReader
from ged4py.model import Individual
from datetime import date
today = date.today()
d4 = today.strftime("%d-%b-%Y")
today_date = list(d4.split('-'))
current_month = today_date[1]
date_today = today_date[0]
#print(date_today)
month = 'DEC'
birthdays_output = []
names_birthdays = []
names_birthday_month = []

def US_upcoming_birthdays():
    with GedcomReader('GEDCOM_YASH_KOSAMBIA.ged') as parser:
        for count, individual in enumerate(parser.records0('INDI')):

            birthdays = str(individual.sub_tag_value("BIRT/DATE")).split(" ")
            birthdays_output.append(birthdays)
            try:
                birthday_day = birthdays[0]
            except:
                pass
            try:
                birthday_months = birthdays[1]
            except:
                pass
            names = str(individual.name.format())
            names_birthday = {names: birthdays}
            names_birthdays.append(names_birthday)
            #print(names_birthday)
            gg = [birthday_day, birthday_months]
            #print(birthday_months)
            if current_month in birthday_months:
                print('UP-COMING BIRTHDAY FOUND', names_birthday)
            elif month in birthday_months:
                print('UP-COMING BIRTHDAY FOUND', names_birthday)

            else:
                pass


def output():
    print('US_38 LIST ALL UP-COMING BIRTHDAYS\n\n')
    US_upcoming_birthdays()

output()