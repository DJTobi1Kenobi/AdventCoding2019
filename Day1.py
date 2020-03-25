# Rocket Problem
def fuelreq(mass):

    return int(mass/3)-2


f = open('day1input', 'r')
modlist= f.read().splitlines()
f.close()
modnum = len(modlist)

modmass = 0
totfuelmassreq=0

i=0
while i < modnum:
    modmass = modmass + fuelreq(int(modlist[i]))
    fuelmass = fuelreq(fuelreq(int(modlist[i])))
    fuelmassreq = fuelmass
    while fuelmass > 0:
        fuelmass = fuelreq(fuelmass)
        if fuelmass > 0:
            fuelmassreq = fuelmassreq + fuelmass
    totfuelmassreq = totfuelmassreq + fuelmassreq
    i = i+1

print "Total Fuel Required is: " +str(modmass + totfuelmassreq)