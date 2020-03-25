x = range(147981, 691423)
code = []

"convert to string and then indivdual integers"
for x in x:
    code.append([int(d) for d in str(x)])

numpass = 0
for x in code:
    "print x"

    a = 0
    seqpass = False

    b = 0
    j = 1
    first = True
    doubpass = False

    "loop through all numbers"
    for i, y in enumerate(x):

        "check if larger"
        if i > 0:
            if x[i] >= x[i-1]:
                a = a + 1
                if a == (len(x)-1):
                    seqpass = True

        "Check double"
        if 0 <= i < len(x):
            if i == 0:  # First digit
                z = x[0]
            elif 0 < i < (len(x) - 1):  # Middle section
                if x[i] == z:
                    j = j + 1
                else:
                    if j == 2:
                        b = b + 1
                    z = x[i]
                    j = 1
            else:  # Last Digit
                if x[i] == z:
                    if j == 1:
                        b = b + 1
                else:
                    if j == 2:
                        b = b + 1
    if b > 0:
        doubpass = True

    "Check if both criteria passed"
    if seqpass and doubpass:
        numpass = numpass + 1

print numpass

"""
Set number for groups
Check if  larger than other possible groups
"""