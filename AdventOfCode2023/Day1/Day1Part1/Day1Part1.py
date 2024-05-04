def day1Part1Main(path):
    calibrationValues = []
    with open(path, "r") as file:
        for line in file:
            index = 0
            digitsInLine = []
            for character in line:
                if (character.isdigit()):
                    digitsInLine.append(character)
                index += 1
                if (index == len(line)):  # Last character of the line
                    lineNumber = int(digitsInLine[0] + digitsInLine[len(digitsInLine) - 1])
                    calibrationValues.append(lineNumber)
    sumOfCalibrationValues = sum(calibrationValues)
    return sumOfCalibrationValues