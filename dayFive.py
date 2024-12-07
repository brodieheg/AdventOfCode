import getInputData
import numpy as np
data = getInputData.getTodaysData(5)
import math

firstDigit = data.index(',') - 2
orderRulesString = data[:firstDigit-1]
listsString = data[firstDigit:]
lists = listsString.splitlines()
orderRules= orderRulesString.splitlines()
for index, list in enumerate(lists):
    lists[index] = [int(x) for x in list.split(',')] 

orderRulesMap = {}
orderRulesList = []
for orderRule in orderRules:
    ruleArray = []
    firstNumber = int(orderRule[0] + orderRule[1])
    secondNumber = int(orderRule[3] + orderRule[4])
    ruleArray.append(firstNumber)
    ruleArray.append(secondNumber)
    orderRulesList.append(ruleArray)
    if(firstNumber in orderRulesMap): orderRulesMap[firstNumber] = [*orderRulesMap[firstNumber], secondNumber]
    else: orderRulesMap[firstNumber] = [secondNumber]

print(orderRulesList)

def checkRule(firstNumber, secondNumber):
    orderRule = orderRulesMap[firstNumber]
    if(secondNumber in orderRule): return True
    else:return False

invalidLists = []
middleTotal = 0
middleInvalidTotal = 0

def listIsValid(list):
    global invalidLists
    for i in range(len(list) - 1):
        if(checkRule(list[i], list[i+1]) == True): continue
        invalidLists.append(list)
        return False
    return True

def reorderList(list, rules):
    changed = True
    while changed:
        changed = False
        for A, B in rules:
            if A in list and B in list:
                idx_a = list.index(A)
                idx_b = list.index(B)
                if idx_b < idx_a:
                    list[idx_a], list[idx_b] = list[idx_b], list[idx_a]
                    changed = True
    return list


for list in lists:
    if(listIsValid(list) == True): middleTotal += list[math.floor(len(list) / 2)]

for list in invalidLists:
    orderedList = reorderList(list, orderRulesList)
    middleInvalidTotal += list[math.floor(len(list) / 2)]


print(middleInvalidTotal)

