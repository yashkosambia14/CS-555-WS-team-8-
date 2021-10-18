from gedcom.element.individual import IndividualElement
from gedcom.element.element import Element
from gedcom.parser import Parser
from datetime import datetime

file_path = "C:/Users/twang/Downloads/ged/hw05-2.ged"
gedcom_parser = Parser()
gedcom_parser.parse_file(file_path)
allElements = gedcom_parser.get_element_list()

currentYear = datetime.now().year
combinedList = ""
actualYear = 0

def listIndividualAges(allElements):
    for element in allElements:
        if isinstance(element, IndividualElement):
            global actualYear
            birthYear = element.get_birth_year()
            if(element.is_deceased() == True):
                deathYear = element.get_death_year()
                actualYear = deathYear - birthYear
            else:
                actualYear = currentYear - birthYear
            
        if element.get_tag() == "NAME":
            global name
            global combinedList

            name = element.get_value()
            individualString = name + " is " + str(actualYear) + " years old.\n"
            combinedList += individualString
            individualString = ""

    tempList = combinedList
    print(combinedList)
    combinedList = ""
    return tempList


if __name__ == '__main__':
    listIndividualAges(allElements)