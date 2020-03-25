# Gravity Helper

import csv
with open('day2input.csv', 'rb') as f:
    reader = csv.reader(f)
    intcode = []
    for row in reader:
        intcode.append(row)

intcode = sum(intcode, [])  # un-nest list
"intcode[1] = 82"
"intcode[2] = 98"
intcode = map(int, intcode)  # convert to int

n = 0
while n < len(intcode):
    x = intcode[n + 1] # Indexing
    y = intcode[n + 2]
    z = intcode[n + 3]
    if intcode[n] == 1:
        intcode[z] = intcode[x] + intcode[y]
    elif intcode[n] == 2:
        intcode[z] = intcode[x] * intcode[y]
    elif intcode[n] == 99:
        print "99 found, Program exiting"
        break
    else:
        print "fix your code!"
        break
    n = n+4

print intcode
