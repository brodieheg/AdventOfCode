import getInputData
import numpy as np
inputData = getInputData.getTodaysData(2)

class CheckSafe:

   def __init__(self, safety=False) -> None:
      if (safety == True): self.safety = True
      else: self.safety = False

   def checkSafeIncreasing(self, array): 
      difference = 0
      unsafeCount = 0
      for index, number in enumerate(array):
        if(index==0): continue
        difference = (number - array[(index - 1)])
        if(difference > 3 or difference < 1): unsafeCount += 1

      if (self.safety and unsafeCount < 2): 
        if(unsafeCount > 0):
         print(array)
        return True
      elif (unsafeCount == 0): return True
      return False
   def checkSafeDecreasing(self, array): 
      difference = 0
      unsafeCount = 0
      for index, number in enumerate(array):
        if(index==0): continue
        difference = (array[(index - 1)] - number)
        if(difference > 3 or difference < 1): unsafeCount += 1

      if (self.safety and unsafeCount < 2): 
        if(unsafeCount > 0):
         print(array)
        return True
      elif (unsafeCount == 0): return True
      return False


def makeNestedArray(data):
    nestedArray = []
    dataLines = data.splitlines()
    for line in dataLines:
     lineList = list(map(int, line.split()))
     nestedArray.append(lineList)
    return nestedArray

nestedArray = makeNestedArray(inputData)
numSafeRows = 0

safeRowChecker = CheckSafe(True)
for row in nestedArray:
   diffs = np.diff(row)
   averageDiff = np.average(diffs)
   
   if(averageDiff > 0):
    #   Increasing Number path
        if(safeRowChecker.checkSafeIncreasing(row) == True):
           numSafeRows += 1

   else:
     #   Decreasing Number path
     if(safeRowChecker.checkSafeDecreasing(row) == True):
           numSafeRows += 1

print(numSafeRows)
              
