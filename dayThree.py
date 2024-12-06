import getInputData
import re
data = getInputData.getTodaysData(3)

mul = '(?P<mul>mul\((\d{1,3}),(\d{1,3})\))'
do = '(?P<do>do\(\))'
dont = '(?P<dont>don\'t\(\))'
pattern = mul + '|' + do + '|' + dont
print(pattern)

values = []

matches = re.findall(pattern, data)
enabled = True
print(matches)
if(matches): 
    for match in matches:
       if(match[4]): enabled = False
       if(match[3]): enabled = True
       if(enabled and match[1] and match[2]):
        value = int(match[1]) * int(match[2])
        values.append(value)
print(sum(values))