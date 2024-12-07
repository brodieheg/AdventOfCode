import getInputData

data = getInputData.getTodaysData(4)
lines = data.splitlines()
print(lines)
XMAS = ['X', 'M', 'A', 'S']
XMASCount = 0
MasCount = 0

def correctNextLetter(possibleDirections, currentLetter, lineIndex, letterIndex):
    # fine index of currentLetter in XMAS, check each cardinal direction
    if(currentLetter == 'S'): global XMASCount; XMASCount += 1; return
    north = None if (lineIndex == 0 or 'north' not in possibleDirections) else lines[lineIndex - 1][letterIndex]
    south = None if (lineIndex == len(lines) - 1 or 'south' not in possibleDirections) else lines[lineIndex + 1][letterIndex]
    east = None if (letterIndex == len(lines[lineIndex]) - 1 or 'east' not in possibleDirections) else lines[lineIndex][letterIndex + 1]
    west = None if (letterIndex == 0 or 'west' not in possibleDirections) else lines[lineIndex][letterIndex - 1]
    northEast = None if (lineIndex == 0 or letterIndex == len(lines[lineIndex]) - 1 or 'northEast' not in possibleDirections) else lines[lineIndex - 1][letterIndex + 1]
    southEast = None if (lineIndex == len(lines) - 1 or letterIndex == len(lines[lineIndex]) - 1 or 'southEast' not in possibleDirections) else lines[lineIndex + 1][letterIndex + 1]
    northWest = None if (lineIndex == 0 or letterIndex == 0 or 'northWest' not in possibleDirections) else lines[lineIndex - 1][letterIndex - 1]
    southWest = None if (lineIndex == len(lines) - 1 or letterIndex == 0 or 'southWest' not in possibleDirections) else lines[lineIndex + 1][letterIndex - 1]

    currentLetterXMASIndex = XMAS.index(currentLetter)
    nextLetter = XMAS[currentLetterXMASIndex + 1]
    if(north == nextLetter): 
        correctNextLetter(['north'], nextLetter, lineIndex - 1, letterIndex)
    if south == nextLetter: 
        correctNextLetter(['south'], nextLetter, lineIndex + 1, letterIndex)
    if east == nextLetter: 
        correctNextLetter(['east'], nextLetter, lineIndex, letterIndex + 1)
    if west == nextLetter: 
        correctNextLetter(['west'], nextLetter, lineIndex, letterIndex - 1)
    if northEast == nextLetter:
        correctNextLetter(['northEast'], nextLetter, lineIndex - 1, letterIndex + 1)
    if southEast == nextLetter:
        correctNextLetter(['southEast'], nextLetter, lineIndex + 1, letterIndex + 1)
    if northWest == nextLetter:
        correctNextLetter(['northWest'], nextLetter, lineIndex - 1, letterIndex - 1)
    if southWest == nextLetter:
        correctNextLetter(['southWest'], nextLetter, lineIndex + 1, letterIndex - 1)

    return

def findMas(aIndex, lineIndex):
    northEast = None if (lineIndex == 0 or aIndex == len(lines[lineIndex]) - 1) else lines[lineIndex - 1][aIndex + 1]
    southEast = None if (lineIndex == len(lines) - 1 or aIndex == len(lines[lineIndex]) - 1) else lines[lineIndex + 1][aIndex + 1]
    northWest = None if (lineIndex == 0 or aIndex == 0) else lines[lineIndex - 1][aIndex - 1]
    southWest = None if (lineIndex == len(lines) - 1 or aIndex == 0) else lines[lineIndex + 1][aIndex - 1]
    mas = 0
    global MasCount
    if(northEast == 'M' and southWest == 'S'):
        mas += 1
    if(northEast == 'S' and southWest == 'M'):
        mas += 1
    if(northWest == 'M' and southEast == 'S'):
        mas += 1
    if(northWest =='S' and southEast == 'M'):
        mas += 1
    if mas == 2: MasCount += 1
     
        


def partOne():
    for lineIndex, line in enumerate(lines):
        for letterIndex, letter in enumerate(line):
         if(letter == 'X'):
            correctNextLetter(['north', 'south', 'east', 'west', 'northEast', 'northWest', 'southEast', 'southWest'], letter, lineIndex, letterIndex)
    print(XMASCount)

def partTwo():
    for lineIndex, line in enumerate(lines):
        for letterIndex, letter in enumerate(line):
         if(letter == 'A'):
            findMas(letterIndex, lineIndex)
    print(MasCount)

partTwo()