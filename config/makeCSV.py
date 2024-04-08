import csv
import random

data = {}

with open('data.txt', 'r') as file:
    for line in file: 
        i = line.split(", ")
        i[0] = i[0].replace('"', '')
        i[1] = i[1][:-1]
        if not (i[1] in data.keys()):
            data[i[1]] = [i[0]]
        else:
            if i[0] not in data.get(i[1]):
                curr = data.get(i[1])
                curr.append(i[0])

for x in data.keys():
    print(x , ":" , data.get(x))

with open('libData.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    field = ["name", "author","numAvail"]
    numAvaiablePossible = [1,2,3,4]
    writer.writerow(field)
    for curr in data.keys():
        for i in data.get(curr):
            writer.writerow([i, curr, random.choice(numAvaiablePossible)])

with open('authorNames.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    field = ["name"]
    writer.writerow(field)
    for curr in data.keys():
        writer.writerow([curr])
 




