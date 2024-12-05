import getInputData
import re
data = getInputData.getTodaysData(3)

pattern = 'mul\((\d{1,3}),(\d{1,3})\)'
values = []


matches = re.findall(pattern, data)
if(matches): 
    for match in matches:
       value = int(match[0]) * int(match[1])
       values.append(value)

print(sum(values))