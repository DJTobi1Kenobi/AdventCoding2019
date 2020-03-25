from shapely.geometry import LineString
import csv


def coord():
    if lines[x][y][0] == "U":
        if y == 0:
            dx = 0
            dy = int(lines[x][y][1:])
        else:
            dx = points[y][0]
            dy = points[y][1] + int(lines[x][y][1:])
        points.append([dx, dy])
    elif lines[x][y][0] == "R":
        if y == 0:
            dx = int(lines[x][y][1:])
            dy = 0
        else:
            dx = points[y][0] + int(lines[x][y][1:])
            dy = points[y][1]
        points.append([dx, dy])
    elif lines[x][y][0] == "D":
        if y == 0:
            dx = 0
            dy = -int(lines[x][y][1:])
        else:
            dx = points[y][0]
            dy = points[y][1] - int(lines[x][y][1:])
        points.append([dx, dy])
    elif lines[x][y][0] == "L":
        if y == 0:
            dx = -int(lines[x][y][1:])
            dy = 0
        else:
            dx = points[y][0] - int(lines[x][y][1:])
            dy = points[y][1]
        points.append([dx, dy])


def xycoords(line):
    "Find out points and convert to list"
    m = line.wkt[12:]
    m = m[:(len(m) - 1)]
    m = m.split(", ")

    y = 0
    while y <= (len(m) - 1):
        m[y] = m[y].split(" ")
        m[y][0] = int(m[y][0])
        m[y][1] = int(m[y][1])
        y = y + 1

    return m


with open('day3input.csv', 'rb') as f:
    reader = csv.reader(f)
    lines = []
    for row in reader:
        lines.append(row)

x = 0

while x < 2:
    points = []
    distance = []

    "set start point"
    if x == 1:
        points.append([1, 0])
        distance.append(0)
    else:
        points.append([-1, 0])
        distance.append(0)

    "Set Coordinates by calling coord & calculated distance"
    y = 0
    while y <= (len(lines[x])-1):
        coord()
        dz = distance[y] + int(lines[x][y][1:])
        distance.append(dz)
        y = y + 1

    "Turn into Tuple for Shapely line function"
    y = 0
    while y <= (len(lines[x]) - 1):
        points[y] = tuple(points[y])
        y = y + 1

    "Remove 0,0 intersection by deleting one pair of 0,0"
    "if x == 0:"
    del points[0]
    del distance[0]

    "create Shapely Lines & distances"
    if x == 0:
        line1 = LineString(points)
        distance1 = distance
    else:
        line2 = LineString(points)
        distance2 = distance
    x = x + 1


intersections = line1.intersection(line2)

"""
For Graphical View - Debugging
xs = [point.x for point in intersections]
ys = [point.y for point in intersections]
plt.scatter(xs,ys)
"""

"Determine smallest Manhattan distance"
y = 0
dist = []
while y <= (len(intersections) - 1):
    dist.append(abs(intersections[y].x) + abs(intersections[y].y))
    y = y+1
print(min(dist))

"Concatante Lines and Distances for ease"
line1 = xycoords(line1)
line2 = xycoords(line2)
lineint = xycoords(intersections)

line = [line1, line2]
distance = [distance1, distance2]

"Find Steps to Intersection"
steps = []
for i, z in enumerate(lineint):
    x = 0
    while x < 2:
        y = 0
        while y <= (len(line[x])-2):
            x1 = line[x][y][0]
            x2 = line[x][y+1][0]
            y1 = line[x][y][1]
            y2 = line[x][y+1][1]
            if ((x1 <= z[0] <= x2) or (x2 <= z[0] <= x1)) and ((y1 <= z[1] <= y2) or (y2 <= z[1] <= y1)):
                ds = (abs(x1) - abs(z[0])) + (abs(y1) - abs(z[1]))
                ds = ds + distance[x][y]
                if x == 0:
                    steps.append([ds, 0])
                else:
                    steps[i][x] = ds
                y = y+1
            else:
                y = y+1
        x = x+1

"Find and Print smallest distance"
ds = []
for z in steps:
    ds.append(sum(z))

print(min(ds))

"""
For Reference
x=["R299"]
x[0][0]
x[0][1:]
"""