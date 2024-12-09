import getInputData
data = getInputData.getTodaysData(9)
fileSizeMap = {}
dotSizeMap = {}

def formatData(data):
    formatedData = []
    for i in range(len(data)):
        digit = int(data[i])
        even = False
        if(i % 2 == 0): even = True
        if(even):
            for index in range(digit):
                idNumber = int(i / 2)
                formatedData.append(idNumber)
                fileSizeMap[idNumber] = digit
        else: 
            for index in range(digit):
                dotSizeMap[len(formatedData) - 1] = digit
                formatedData.append('.')
    return formatedData

formatedData = formatData(data)
lastIndex = len(formatedData) - 1

# Part One:
# while '.' in formatedData:
#     if formatedData.index('.') == len(formatedData) - 1:
#         formatedData.pop(-1)
#         continue
#     formatedData[formatedData.index('.')] = formatedData.pop(-1)
# sum = 0

# for index in range(len(formatedData)):
#     sum += (index * formatedData[index])
# Starting part two ---
dotIndexes = dotSizeMap.keys()
dotSizes = dotSizeMap.values()
fileIDs = fileSizeMap.keys()

def first(the_iterable, condition = lambda x: True):
    for i in the_iterable:
        if condition(i):
            return i

dotCounter = 0
for i in reversed(range(len(fileIDs))):
    fileId = fileIDs[i]
    size = fileSizeMap[fileId]
    leftMostPosition = dotSizes.index(first(dotSizes, lambda i: i >= size))
    print(dotIndexes[leftMostPosition])



print(formatedData)



