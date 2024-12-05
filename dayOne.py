import csv

list1 = []
list2 = []
totalDifference = 0
similarityScore = 0
frequencyMap = {}
frequencyScore=0

def getLists():

    # Format text to replace spaces with a \tab so it can be read into array
    with (open('data.csv', 'r') as data,
        open('newdata.csv', 'w') as new_data):
        for line in data:
            new_data.write(line.replace('   ', '\t'))

    with open('newdata.csv') as new_data:
        reader=csv.reader(new_data, delimiter='\t')
        for line in reader:
            list1.append(int(line[0]))
            list2.append(int(line[1]))

        list1.sort()
        list2.sort()

getLists()

for i, item in enumerate(list1):
    if(item not in frequencyMap):
        frequencyMap[item] = 0
    totalDifference += (abs(item - (list2[i])))

for i, item in enumerate(list2):
    if(item in frequencyMap):
         frequencyMap[item] += 1

for key, value in frequencyMap.items():
  frequencyScore += (key * value)

print(totalDifference)
print(frequencyScore)



