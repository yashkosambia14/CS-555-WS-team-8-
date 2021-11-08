from gedcom.element.individual import IndividualElement
from gedcom.element.element import Element
from gedcom.parser import Parser
from datetime import datetime

file_path = r"SPRINT_2\gedcom\US07_2DeadOver.ged"
gedcom_parser = Parser()
gedcom_parser.parse_file(file_path)
allElements = gedcom_parser.get_element_list()

currentYear = datetime.now().year
combinedList = ""

def lessThan150(allElements):
    print ("User Story 7")
    for element in allElements:
        if isinstance(element, IndividualElement):
            global combinedList
            birthYear = element.get_birth_year()
            deathYear = element.get_death_year()
            birthData = element.get_birth_data()
            deathData = element.get_death_data()      
            birthComp = abs(birthYear - currentYear)

            if (deathYear > 0):
                deathComp = abs(deathYear - birthYear)
                if(150 < deathComp):
                    tempString = "US07: More than 150 years old at death - Birth Date " + birthData[0] + " Death Date " + deathData[0] + "\n"
                    combinedList += tempString
            elif(150 < birthComp):
                tempString = "US07: More than 150 years old: - Birth Date " + birthData[0] + "\n"
                combinedList += tempString

    tempList = combinedList
    print(combinedList)
    combinedList = ""
    return tempList
            
if __name__ == '__main__':
    lessThan150(allElements)