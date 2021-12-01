from gedcom.element.individual import IndividualElement
from gedcom.parser import Parser

def returnDuplicates(listOfElems):
    x=set(listOfElems)
    dup=[]
    for c in x:
        if(listOfElems.count(c)>1):
            dup.append((c))
    return dup

def listMultipleBirths(file_path):
    gedcom_parser = Parser()
    gedcom_parser.parse_file(file_path)
    allElements = gedcom_parser.get_element_list()

    birthList = []

    for element in allElements:
        if isinstance(element, IndividualElement):
            if element.is_child() == True:
                birthDataTuple = element.get_birth_data()
                birthData = birthDataTuple[0]
                birthList.append(birthData)

    dupStatus = returnDuplicates(birthList)
    errorLine = "US32: Individuals were born at the same on: " + str(dupStatus)
    print(errorLine)
    return errorLine
            
if __name__ == '__main__':
    file = "C:/Users/twang/Desktop/ged/US32_Empty.ged"
    listMultipleBirths(file)