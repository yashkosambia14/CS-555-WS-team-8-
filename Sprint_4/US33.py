from gedcom.element.individual import IndividualElement
from gedcom.parser import Parser
from datetime import datetime

def listOrphans(file_path):
    gedcom_parser = Parser()
    gedcom_parser.parse_file(file_path)
    allElements = gedcom_parser.get_element_list()
    currentYear = datetime.now().year

    orphanList = ""

    for element in allElements:
        if isinstance(element, IndividualElement):
            birthYear = element.get_birth_year()
            age = currentYear - birthYear

            if(age < 18):
                familyElements = gedcom_parser.get_parents(element)
                mother = False
                father = False
                # print(element.get_name())
                for individuals in familyElements:
                    gender = individuals.get_gender()
                    deathStatus = individuals.is_deceased()
                    
                    if gender == "F" and deathStatus == True:
                        father = True
                    if gender == "M" and deathStatus == True:
                        mother = True
                    if mother == True and father == True:
                        orphanList += element.get_pointer() + " "

    errorLine = "US33: Orphaned Individuals are: " + orphanList
    print(errorLine)
    return errorLine
            
if __name__ == '__main__':
    file = "C:/Users/twang/Desktop/ged/CS 555 Family.ged"
    listOrphans(file)