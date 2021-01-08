from collections import defaultdict
with open("16.txt") as fp:
    lines = fp.read().split("\n")

i = 0
valu = []

for line in lines:
    if 'your ticket' in line:
        break
    else:
        line = line.split(' ')
        for elem in line:
            nr = [int(s) for s in elem.split("-") if s.isdigit()]
            valu.append(nr)


d = defaultdict(int)
for lista in valu:
    if sum(lista) != 0:
        for i in range(lista[0], lista[1] + 1):
            d[i] += 1

i = 0
for line in lines:
    i += 1
    if 'nearby' in line:
        start = i
stop = i


suma = 0
lista_tot = []
for j in range(start, stop):
    numere = lines[j].split(',')
    lista_tot.append(numere)
    '''
    for elem in numere:
        if int(elem) not in d.keys():
            lista_tot.remove(numere)
            continue
    '''

d = defaultdict(list)
for elem in lista_tot:
    for val, elem_mic in enumerate(elem):
        d[val].append(int(elem_mic))


rng = []
for line in lines:
    if line is '\n':
        break
    else:
        taiat = line.split('-')
        if len(taiat) > 1:
            taiat2 = taiat[1].split('or')
            rng.append([int(taiat2[0]), int(taiat2[1])])

d_possible = defaultdict(int)
for k, v in d.items():
    possible = [i for i in range(0, 20)]
    for element in v:
        i = 0

        for i in range(0, 20):
            cnt = 0
            for it in range(rng[i][0]+1, rng[i][1]):
                if it == element:
                    cnt += 1
            if cnt > 0:
                possible.remove(i)
        d_possible[k] = possible


d_final = defaultdict(int)
x = []

for k, v in d_possible.items():
    x.append(v)

i = 0
nev = 1
vizitate = []
while 1:
    if nev == len(x):
        break
    else:
        if len(x[i]) == nev:
            for j in range(0, len(x[i])):
                if x[i][j] not in vizitate:
                    vizitate.append(x[i][j])
                    d_final[i] = x[i][j]
                    nev += 1
        i += 1
    if len(vizitate) != 20 and i is 20:
        i = 0

important = []
for k, v in d_final.items():
    if v < 6:
        important.append(k)

for i, line in enumerate(lines):
    if i == 22:
        dorit = [elem for elem in line.split(',')]
        break

m = 1
for elem in important:
    m *= int(dorit[elem])
print(m)
