# Gravity Helper

import csv
with open('day5input.csv', 'rb') as f:
    reader = csv.reader(f)
    intcode = []
    for row in reader:
        intcode.append(row)

intcode = sum(intcode, [])  # un-nest list
intcode = map(int, intcode)  # convert to int

output = []
n = 0
try:
    while n < len(intcode):
        parameter = []
        operator = 0
        if intcode[n] < 100:
            operator = intcode[n]
            if operator <= 2:
                x = intcode[n + 1]  # Indexing
                y = intcode[n + 2]
                z = intcode[n + 3]
                a = intcode[x]
                b = intcode[y]
            else:
                x = intcode[n + 1]
        else:
            intcode[n]
            parameter = [int(d) for d in str(intcode[n])]
            operator = parameter[-1]
            if len(parameter) == 3:
                x = intcode[n + 1]  # Indexing
                y = intcode[n + 2]
                z = intcode[n + 3]
                a = intcode[n + 1]
                if operator <= 2:
                    b = intcode[y]
            elif len(parameter) == 4:
                x = intcode[n + 1]  # Indexing
                y = intcode[n + 2]
                z = intcode[n + 3]
                if parameter[1] == 1:
                    a = intcode[n + 1]
                else:
                    a = intcode[x]
                b = intcode[n + 2]
            elif len(parameter) == 5:
                x = intcode[n + 1]  # Indexing
                y = intcode[n + 2]
                z = intcode[n + 3]
                if parameter[1] == 1:
                    b = intcode[n + 2]
                else:
                    b = intcode[y]
                if parameter[2] == 1:
                    a = intcode[n + 1]
                else:
                    a = intcode[x]
        if operator == 1:
            intcode[z] = a + b
            n = n + 4
        elif operator == 2:
            intcode[z] = a * b
            n = n + 4
        elif operator == 3:
            "intinput = int(raw_input())"
            intinput = 1
            intcode[x] = intinput
            n = n + 2
        elif operator == 4:
            if len(parameter) > 1:
                output.append(a)
            else:
                output.append(intcode[x])
            n = n + 2
        elif intcode[n] == 99:
            print "99 found, Program exiting"
            break
        else:
            print n
            print "fix your code"
            break
except IndexError:
    print n

print output
