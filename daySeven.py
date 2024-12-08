import getInputData
from itertools import product

from functools import reduce
from operator import mul
data = getInputData.getTodaysData(7)

def format_data(data):
 data_lines = data.splitlines()
 for index, line in enumerate(data_lines):
    newline = line.split(':')
    newline[0] = int(newline[0])
    numbers = newline[1].split(' ')
    for i in range(len(numbers)):
        if(numbers[i] == ''): continue
        if(numbers[i] != '' and i < len(newline)):
         newline[i] = int(numbers[i])
        else: newline.append(int(numbers[i]))
    data_lines[index] = newline
 return data_lines

def checkLine(line):
    targetNumber = line[0]
    testValues = line[1:]
    return(evaluate_all_operations(testValues, targetNumber))


def evaluate_left_to_right(expression):
    tokens = []
    num = ''
    for char in expression:
        if char.isdigit():
            num += char
        else:
            tokens.append(int(num))  
            tokens.append(char)   
            num = ''
    tokens.append(int(num))  
    result = tokens[0]
    i = 1
    while i < len(tokens):
        operator = tokens[i]
        next_number = tokens[i + 1]
        if operator == '+':
            result += next_number
        elif operator == '*':
            result *= next_number
        elif operator == '|':
            result = int(str(result) + str(next_number))
        i += 2
    return result


def evaluate_all_operations(numbers, targetNumber):
    if not numbers:
        return []
    operators_combinations = list(product(['+', '*', '|'], repeat=len(numbers) - 1))
    results = []

    for operators in operators_combinations:
        expression = str(numbers[0])  
        for num, op in zip(numbers[1:], operators):
            expression += op + str(num) 
        results.append((expression))
    possibleanswers = []
    for result in results:
        possibleanswers.append(evaluate_left_to_right(result))
    if(targetNumber in possibleanswers): return True
    return False

def part_one(data):
  total = 0
  dataArray = format_data(data)
  for line in dataArray:
    if(checkLine(line)):
      total += line[0]
  print(total)
    
part_one(data)
