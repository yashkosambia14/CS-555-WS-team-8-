from gedcom.element.individual import IndividualElement
from gedcom.parser import Parser

def birthBeforeMarriage(file_path):
    gedcom_parser = Parser()
    gedcom_parser.parse_file(file_path)
    allElements = gedcom_parser.get_element_list()

    combinedList = ""

    for element in allElements:
        if isinstance(element, IndividualElement):
            birthYear = element.get_birth_year()
            marriageTemp = gedcom_parser.get_marriages(element)
            if not marriageTemp:
                pass
            else:
                marriageTemp1 = marriageTemp[0]
                marriageTemp2 = marriageTemp1[0]
                marriageYear = marriageTemp2[-4:]

                if birthYear > int(marriageYear):
                    individualString = "US02: Individual born on " + str(birthYear) + " occurs after marriage date on " + marriageYear + "\n"
                    combinedList += individualString

    tempList = combinedList
    print(combinedList)
    combinedList = ""
    return tempList
            
if __name__ == '__main__':
    file = "C:/Users/twang/Desktop/ged/US02_BothOver.ged"
    birthBeforeMarriage(file)