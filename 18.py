import math
with open("18.txt") as fp:
    lines = fp.read().splitlines()

vect = []
_fin = []
for line in lines:
    x = line.split(' ')
    for elem in x:
        if len(elem) > 1:
            for i in range(0, len(elem)):
                vect.append(elem[i])
        else:
            vect.append(elem)
    _fin.append(vect)
    vect = []


def part1():
    vector_sume = []
    suma = 0
    cnt = 0
    for j in range(0, len(_fin)):
        while '(' in _fin[j] or ')' in _fin[j]:
            for idx, elem in enumerate(_fin[j]):
                if elem is '(':
                    idxS = idx
                if elem is ')':
                    idxF = idx
                    break
            total = 0
            semn = '+'
            for i in range(idxS + 1, idxF):
                if _fin[j][i] is '*' or _fin[j][i] is '+':
                    semn = _fin[j][i]
                    continue
                if semn is '*':
                    total *= int(_fin[j][i])
                if semn is '+':
                    total += int(_fin[j][i])

            _fin[j] = _fin[j][:idxS] + [total] + _fin[j][idxF + 1:]


        semn = '+'
        total = 0
        for i in range(0, len(_fin[j])):
            if _fin[j][i] is '*' or _fin[j][i] is '+':
                semn = _fin[j][i]
                continue
            if semn is '*':
                total *= int(_fin[j][i])
            if semn is '+':
                total += int(_fin[j][i])
        vector_sume.append(total)

    #print(vector_sume)
    return sum(vector_sume)




def part2():
    lista_finala = []
    for j in range(0, len(_fin)):
        while '(' in _fin[j] or ')' in _fin[j]:
            for idx, elem in enumerate(_fin[j]):
                if elem is '(':
                    idxS = idx
                if elem is ')':
                    idxF = idx
                    break
            total = 0
            #semn = '+'
            lista_inmultire = []
            for i in range(idxS + 1, idxF):
                if _fin[j][i] is not '+' and _fin[j][i] is not '*':
                    total += int(_fin[j][i])
                if _fin[j][i] is '+':
                    continue
                if _fin[j][i] is '*':
                    lista_inmultire.append(total)
                    total = 0
                    continue
                if i is idxF - 1:
                    lista_inmultire.append(total)
            #print(lista_inmultire)
            prod = 1
            for elem in lista_inmultire:
                if elem is not 0:
                    prod *= int(elem)
            _fin[j] = _fin[j][:idxS] + [prod] + _fin[j][idxF + 1:]

            #print(lista_inmultire)
        lista_inmultire = []
        total = 0
        #print(_fin[j])
        for i in range(0, len(_fin[j])):
            if _fin[j][i] is not '+' and _fin[j][i] is not '*':
                total += int(_fin[j][i])
            if _fin[j][i] is '+':
                continue
            if _fin[j][i] is '*':
                lista_inmultire.append(total)
                total = 0
                continue
            if i is len(_fin[j])-1:
                lista_inmultire.append(total)
        prod = 1
        for elem in lista_inmultire:
            if elem is not 0:
                prod *= int(elem)
        lista_finala.append(prod)

    return sum(lista_finala)

print(part1())
#print(part2())

with open("18.txt", "r") as f:
    lines22 = [i.replace(" ", "") for i in f.read().strip().splitlines()]

print(lines22)




