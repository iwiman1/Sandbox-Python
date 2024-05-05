def day1Part2Main(path):
    numbersList = []
    with open(path, "r") as file:
        for line in file:
            lineNumber = getNumberFromLine(line)
            numbersList.append(lineNumber)
    sumOfAllNumbers = sum(numbersList)
    return sumOfAllNumbers

def getNumberFromLine(line):
    digitsInLine = []
    accumulatedCharacters = ""
    for character in line:
        accumulatedCharacters += character
        if (character.isdigit()):
            digitsInLine.append(character)
            accumulatedCharacters = ""
            continue
        (hasDigitAsWord_, digitAsWord) = hasDigitAsWord(accumulatedCharacters)
        if (hasDigitAsWord_):
            digitsInLine.append(wordToNumber[digitAsWord])
            accumulatedCharacters = accumulatedCharacters[-1]  # First character of a new digit could be the last character of the previous one.
    lineNumber = int(digitsInLine[0] + digitsInLine[len(digitsInLine) - 1])
    return lineNumber

def hasDigitAsWord(word):
    hasDigit = False
    digitAsWord = ""
    for key in wordToNumber.keys():
        if (key in word):
            hasDigit = True
            digitAsWord = key
    return (hasDigit, digitAsWord)

wordToNumber = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}