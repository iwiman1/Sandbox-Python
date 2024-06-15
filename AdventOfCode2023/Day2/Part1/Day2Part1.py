def day2Part1Main(path):
    with open(path, "r") as file:
        gameId = 0
        impossibleGameIds = []
        for line in file:
            gameId += 1
            alreadyImpossibleGameId = False
            line = line.replace("\n", "")
            allReveals = line.split(": ")[1]  # For example: "1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"
            listOfReveals = allReveals.split("; ")  # ["1 blue, 2 green", "3 green, 4 blue, 1 red", "1 green, 1 blue"]
            for reveal in listOfReveals:  # "1 blue, 2 green"
                if (alreadyImpossibleGameId):
                    break
                eachColor = reveal.split(", ")  # ["1 blue", "2 green"]
                for color in eachColor:  # "1 blue"
                    cubeColor = color.split(" ")[1]
                    numberOfCubes = color.split(" ")[0]
                    if (isImpossible(cubeColor, int(numberOfCubes))):
                        impossibleGameIds.append(gameId)
                        alreadyImpossibleGameId = True
                        break
    return sum(impossibleGameIds)

def isImpossible(color, numberOfCubes):
    return numberOfCubes > maxNumberOfCubes[color]

maxNumberOfCubes = {"red": 12, "green": 13, "blue": 14}