# CS555ws - TEAM - 8
from ged4py.parser import GedcomReader
from ged4py.model import Individual
from datetime import date
today = date.today()
d4 = today.strftime("%d-%b-%Y")
today_date = list(d4.split('-'))
print("LIST OF AlL MARRIAGES\n\n")

marriage_output = []
all_Marriages_family = []
names = []
current_month = today_date[1]

def all_anniversaries():
    with GedcomReader('GEDCOM_YASH_KOSAMBIA.ged') as parser:
        for count, family in enumerate(parser.records0('FAM')):
            marriage_date = str(family.sub_tag_value("MARR/DATE")).split(" ")
            marriage_output.append(marriage_date)
            family_id = str(family.sub_tag('HUSB').xref_id).split(' ')

            Marriages_family = ['Family Id: ', family_id, 'Marriage date: ', marriage_date]
            print(Marriages_family)
            all_Marriages_family.append(Marriages_family)
            current_month = today_date[1]
            #print('FAMILY AND MARRIAGE DATE', Marriages_family)
            if current_month in marriage_date:
                print('\nUP-COMING ANNIVERSARY\n')
            else:
                print('\nNO UP-COMING ANNIVERSARY FOUND\n')





all_anniversaries()
#print(all_Marriages_family)

