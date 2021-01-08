from collections import Counter
with open("11.txt") as fp:
    lines = fp.read().split('\n')
print(lines)

#with open("teste.txt") as fp:
#    lines = fp.read().split('\n')


for line in lines:
    nr_coloane = len(line)
nr_linii = len(lines)

print(nr_linii)
print(nr_coloane)


v = [[0 for x in range(nr_coloane)] for y in range(nr_linii)]
for i in range(0, nr_linii):
    for j in range(0, nr_coloane):
        if lines[i][j] is 'L':
            v[i][j] = 0
        if lines[i][j] is '#':
            v[i][j] = 1
        if lines[i][j] is '.':
            v[i][j] = 7


print(v)

def valid(i, j):
    if i >= 0 and j >= 0 and i < nr_linii and j < nr_coloane:
        return True
    return False


def getOccupiedNeighbors(v, i, j):
    suma = 0
    poz = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    for e1, e2 in poz:
        done = 0
        i_new = i
        j_new = j
        while not done:
            i_new+=e1
            j_new+=e2
            if not valid(i_new, j_new):
                done = 1
                break
            if v[i_new][j_new] is 1:
                done = 1
                suma+=1
            if v[i_new][j_new] is 0:
                done = 1
    return suma


def getOccupiedNeighbors2(v, i, j):
    suma = 0
    poz = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    for e1, e2 in poz:
        done = 0
        i_new = i
        j_new = j
        while not done:
            i_new += e1
            j_new += e2
            if not valid(i_new, j_new):
                done = 1
            else:
                if v[i_new][j_new] is 1:
                    suma += 1
                    done = 1
                if v[i_new][j_new] is 0:
                    done = 1
    return suma


def numberOfOccupiedSeats(v):
    nr = 0
    for i in range(0, nr_linii):
        for j in range(0, nr_coloane):
            if v[i][j] is 1:
                nr+=1
    return nr


transf = [[0 for x in range(nr_coloane)] for y in range(nr_linii)]

while transf != v:

    for i in range(0, nr_linii):
        for j in range(0, nr_coloane):
            if v[i][j] == 7:
                transf[i][j] = 7
            if getOccupiedNeighbors(v, i, j) == 0 and v[i][j] is 0:
                transf[i][j] = 1
            if getOccupiedNeighbors(v, i, j) > 0 and v[i][j] is 0:
                transf[i][j] = 0
            if getOccupiedNeighbors(v, i, j) >= 5 and v[i][j] is 1:
                transf[i][j] = 0
            if getOccupiedNeighbors(v, i, j) < 5 and v[i][j] is 1:
                transf[i][j] = 1

    if v == transf:
        break
    else:
        print(transf)
        v = transf
        transf = [[0 for x in range(nr_coloane)] for y in range(nr_linii)]


print(numberOfOccupiedSeats(v))