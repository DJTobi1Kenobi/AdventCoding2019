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
        if intcode[n] == 99:
            print "99 found, Program exiting"
            break
        elif intcode[n] < 100:
            operator = intcode[n]
            if operator <= 2 or 4 < operator < 7 or operator >= 7:
                x = intcode[n + 1]  # Indexing
                y = intcode[n + 2]
                z = intcode[n + 3]
                c = intcode[x]
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
                c = intcode[n + 1]
                if operator <= 2 or operator >= 5:
                    b = intcode[y]
            elif len(parameter) == 4:
                x = intcode[n + 1]  # Indexing
                y = intcode[n + 2]
                z = intcode[n + 3]
                if parameter[1] == 1:
                    c = intcode[n + 1]
                else:
                    c = intcode[x]
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
                    c = intcode[n + 1]
                else:
                    c = intcode[x]
                a = intcode[n+3]
        if operator == 1:
            intcode[z] = c + b
            n = n + 4
        elif operator == 2:
            intcode[z] = c * b
            n = n + 4
        elif operator == 3:
            "intinput = int(raw_input())"
            intinput = 5
            intcode[x] = intinput
            n = n + 2
        elif operator == 4:
            if len(parameter) > 1:
                output.append(c)
            else:
                output.append(intcode[x])
            n = n + 2
        elif operator == 5:
            if c > 0:
                if len(parameter) > 1:
                    n = b
                else:
                    n = intcode[y]
            else:
                n = n + 3
        elif operator == 6:
            if c == 0:
                if len(parameter) > 1:
                    n = b
                else:
                    n = intcode[y]
            else:
                n = n + 3
        elif operator == 7:
            if c < b:
                intcode[z] = 1
            else:
                intcode[z] = 0
            n = n + 4
        elif operator == 8:
            if c == b:
                intcode[z] = 1
            else:
                intcode[z] = 0
            n = n + 4
        else:
            print n
            print "fix your code"
            break
except IndexError:
    print n

print output
