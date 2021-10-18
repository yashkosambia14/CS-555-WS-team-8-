from gedcom.element.individual import IndividualElement
from gedcom.element.element import Element
from gedcom.parser import Parser
from datetime import datetime

file_path = "C:/Users/twang/Desktop/ged/US01_2birth2death.ged"
gedcom_parser = Parser()
gedcom_parser.parse_file(file_path)
allElements = gedcom_parser.get_element_list()

currentYear = datetime.now().year
combinedList = ""

def convertTuple(tup):
    # initialize an empty string
    str = ''
    for item in tup:
        str = str + item + " "
    return str

def beforeCurrentDate(allElements):
    for element in allElements:
        if isinstance(element, IndividualElement):
            global combinedList
            birthYear = element.get_birth_year()
            deathYear = element.get_death_year()
            nameTuple = element.get_name()
            name = convertTuple(nameTuple)
            
            if(currentYear < birthYear):
                tempString = "US01: Birthday of " + name + " occurs in the future\n"
                combinedList += tempString
            if(currentYear < deathYear):
                tempString = "US01: Death of " + name + " occurs in the future\n"
                combinedList += tempString

    tempList = combinedList
    print(combinedList)
    combinedList = ""
    return tempList
            
if __name__ == '__main__':
    beforeCurrentDate(allElements)