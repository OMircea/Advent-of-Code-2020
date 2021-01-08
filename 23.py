with open("23.txt") as f:
    numbers = f.read().split()

lista = [int(elem) for elem in list(str(numbers)) if elem.isdigit()]

cc = 0

for i in range(10, 1000000):
    lista.append(i)

for _ in range(10000000):
    print(_)
    c1, c2, c3 = lista[(cc+1)%len(lista)], lista[(cc+2)%len(lista)], lista[(cc+3)%len(lista)]
    merg_la = lista[cc] - 1
    index_merg_la = lista[cc]

    lista.remove(c1)
    lista.remove(c2)
    lista.remove(c3)

    while merg_la not in lista:
        if merg_la > 1:
            merg_la -= 1
        else:
            merg_la = 9

    lista.insert(lista.index(merg_la) + 1, c3)
    lista.insert(lista.index(merg_la) + 1, c2)
    lista.insert(lista.index(merg_la) + 1, c1)

    cc = (lista.index(index_merg_la) + 1) % len(lista)

print(lista)