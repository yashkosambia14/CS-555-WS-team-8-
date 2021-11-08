from gedcom.element.individual import IndividualElement
from gedcom.element.family import FamilyElement
from gedcom.parser import Parser
from datetime import datetime

def remove_every_other(my_list):
    return my_list[::2]

def birthBeforeMarriage(file_path):
    gedcom_parser = Parser()
    gedcom_parser.parse_file(file_path)
    allElements = gedcom_parser.get_element_list()

    combinedList = ""
    marriageList = []
    birthList = []

    for element in allElements:
        if isinstance(element, IndividualElement):
            if element.get_tag() == "INDI":
                marriageYear = gedcom_parser.get_marriage_years(element)
                marriageList += marriageYear
            if element.get_tag() == "INDI" and element.is_child() == True:
                birthYear = element.get_birth_year()
                birthList.append(birthYear)
    
    marriageListFix = remove_every_other(marriageList)
    counter = 0
    for marriage in marriageListFix:
        if marriage > birthList[counter]:
            tempString = "US08: Child born on: " + str(birthList[counter]) + " occurs after marriage " + str(marriage) + "\n"
            combinedList += tempString
        counter += 1    

    tempList = combinedList
    print(combinedList)
    combinedList = ""
    marriageList = []
    marriageListFix = []
    birthList = []
    return tempList
            
if __name__ == '__main__':
    file = "C:/Users/twang/Desktop/ged/US08_1BeforeMarriage.ged"
    birthBeforeMarriage(file)