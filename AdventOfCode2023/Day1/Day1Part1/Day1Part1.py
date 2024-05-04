def day1Part1Main(path):
    numbersList = []
    with open(path, "r") as file:
        for line in file:
            lineNumber = getNumberFromLine(line)
            numbersList.append(lineNumber)
    sumOfAllNumbers = sum(numbersList)
    return sumOfAllNumbers

def getNumberFromLine(line):
    digitsInLine = []
    for character in line:
        if (character.isdigit()):
            digitsInLine.append(character)
    lineNumber = int(digitsInLine[0] + digitsInLine[len(digitsInLine) - 1])
    return lineNumber