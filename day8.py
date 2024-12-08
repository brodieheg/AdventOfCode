import getInputData
import math

data = getInputData.getTodaysData(8)
data_lines = data.splitlines()
map_of_frequencies = {}
list_of_antinodes = []

    
for line_index, line in enumerate(data_lines):
    for char_index, char in enumerate(line):
        if(char != '.'):
            coordinates = [line_index, char_index]
            list_of_coordinates = []
            if char not in map_of_frequencies: 
                list_of_coordinates.append(coordinates)
                map_of_frequencies[char] = list_of_coordinates
            else: map_of_frequencies[char].append(coordinates)

def findAntiNodes(coordinate1, coordinate2):
    x1, y1 = coordinate1
    x2, y2 = coordinate2
    distanceX = x2 - x1
    distanceY = y2 - y1
    altDistanceX = x1 - x2
    altDistanceY = y1 - y2
    newX = x2 + distanceX
    newY = y2 + distanceY
    altNewX = x1 + altDistanceX
    altNewY = y1 + altDistanceY
    possibleNode1 = [newX, newY]
    possibleNode2 = [altNewX, altNewY]
    if(check_if_in_bounds(possibleNode1)) and (possibleNode1 not in list_of_antinodes): list_of_antinodes.append(possibleNode1)
    if(check_if_in_bounds(possibleNode2)) and (possibleNode2 not in list_of_antinodes): list_of_antinodes.append(possibleNode2)


def check_if_in_bounds(coordinates):
        lineIndex = coordinates[0]
        charIndex = coordinates[1]
        if(lineIndex < 0 or lineIndex > len(data_lines) - 1): return False
        if(charIndex < 0 or charIndex > len(data_lines[lineIndex]) - 1): return False
        return True



for frequency, coordinates in map_of_frequencies.items():
    for i in range(len(coordinates)):
        remainingCoordinates = coordinates[(i+1):]
        for index in range(len(remainingCoordinates)):
            findAntiNodes(coordinates[i], remainingCoordinates[index])

print(len(list_of_antinodes))