
with open("12.txt") as fp:
    lines = fp.read().split("\n")


#with open("teste.txt") as fp:
#    lines = fp.read().split('\n')

'''
v = []
mut = []
for line in lines:
    v.append(line[0])
    mut.append(line[1:])




poz_init = [0, 0]
poz = [0, 0]
currOrientation = 'E'


for i in range(0, len(v)):

    if v[i] in 'NSEW':
        val = v[i]
        if val is 'N':
            poz[1] += int(mut[i])
        if val is 'S':
            poz[1] -= int(mut[i])
        if val is 'E':
            poz[0] += int(mut[i])
        if val is 'W':
            poz[0] -= int(mut[i])



    if v[i] is 'F':
        val = currOrientation[-1]
        #print(val)
        if val is 'N':
            poz[1] += int(mut[i])
        if val is 'S':
            poz[1] -= int(mut[i])
        if val is 'E':
            poz[0] += int(mut[i])
        if val is 'W':
            poz[0] -= int(mut[i])

    if v[i] is 'L   ':
        #print(v[i], mut[i])
        #print(currOrientation)

        valaux = currOrientation[-1]
        grade = int(mut[i])
        #print("=")
        #print(valaux, grade)
        if valaux == 'W' and grade == 90:
            currOrientation += 'S'
            continue
        if valaux == 'W' and grade == 180:
            currOrientation += 'E'
            continue
        if valaux == 'W' and grade == 270:
            currOrientation += 'N'
            continue

        if valaux == 'E' and grade == 90:
            currOrientation += 'N'
            continue
        if valaux == 'E' and grade == 180:
            currOrientation += 'W'
            continue
        if valaux == 'E' and grade == 270:
            currOrientation += 'S'
            continue

        if valaux == 'N' and grade == 90:
            currOrientation += 'W'
            continue
        if valaux == 'N' and grade == 180:
            currOrientation += 'S'
            continue
        if valaux == 'N' and grade == 270:
            currOrientation += 'E'
            continue

        if valaux == 'S' and grade == 90:
            currOrientation += 'E'
            continue
        if valaux == 'S' and grade == 180:
            currOrientation += 'N'
            continue
        if valaux == 'S' and grade == 270:
            currOrientation += 'W'
            continue
        #print(currOrientation)
        #print("======================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================")
        #continue


    if v[i] is 'R':
        #print(v[i], mut[i])
        #print(currOrientation)

        valaux = currOrientation[-1]
        grade = int(mut[i])
        #print("=")
        #print(valaux, grade)
        if valaux == 'W' and grade == 90:
            currOrientation += 'N'
            continue
        if valaux == 'W' and grade == 180:
            currOrientation += 'E'
            continue
        if valaux == 'W' and grade == 270:
            currOrientation += 'S'
            continue

        if valaux == 'E' and grade == 90:
            currOrientation += 'S'
            continue
        if valaux == 'E' and grade == 180:
            currOrientation += 'W'
            continue
        if valaux == 'E' and grade == 270:
            currOrientation += 'N'
            continue

        if valaux == 'N' and grade == 90:
            currOrientation += 'E'
            continue
        if valaux == 'N' and grade == 180:
            currOrientation += 'S'
            continue
        if valaux == 'N' and grade == 270:
            currOrientation += 'W'
            continue

        if valaux == 'S' and grade == 90:
            currOrientation += 'W'
            continue
        if valaux == 'S' and grade == 180:
            currOrientation += 'N'
            continue
        if valaux == 'S' and grade == 270:
            currOrientation += 'S'
            continue
        #print(currOrientation)
        #print("======================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================")
        #continue

    print(poz)




print(poz)
print(currOrientation)

print(abs(poz[0])+abs(poz[1]))

print(abs(poz[0])+abs(poz[1]))

'''
import numpy as np


def partea1():
    SHIP = np.array([0, 0, 0, 0])
    CURR_POSITION = np.array([0, 1, 0, 0])
    CARD = {'N': 0, 'E': 1, 'S': 2, 'W': 3}

    for line in lines:
        act = line[0]
        cat = int(line[1:])

        if act == 'F':
            SHIP += CURR_POSITION * cat
        if act == 'L':
            CURR_POSITION = np.roll(CURR_POSITION, -(cat//90))
        if act == 'R':
            CURR_POSITION = np.roll(CURR_POSITION, (cat//90))
        if act in 'NSEW':
            SHIP[CARD[act]]+=cat

    print(abs(SHIP[1]-SHIP[3]) + abs(SHIP[2]-SHIP[0]))


def partea2():
    SHIP = np.array([0, 0, 0, 0])
    WAYPOINT = np.array([1, 10, 0, 0])
    CARD = {'N': 0, 'E': 1, 'S': 2, 'W': 3}

    for line in lines:
        act = line[0]
        cat = int(line[1:])

        if act == 'F':
            SHIP += WAYPOINT * cat
        elif act == 'L':
            WAYPOINT = np.roll(WAYPOINT, -(cat//90))
        elif act == 'R':
            WAYPOINT = np.roll(WAYPOINT, (cat//90))
        else:
            v = ([0, 0, 0, 0])
            v[CARD[act]] += cat

            WAYPOINT += v

    print(abs(SHIP[1]-SHIP[3]) + abs(SHIP[2]-SHIP[0]))

print("===")
partea1()
print("===")
partea2()
