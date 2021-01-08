with open("5.txt") as fp:
    lines = fp.readlines()


def find(numar, mic, mare, indice):
    mici = ["F", "L"]
    indici = [6, 9]
    if indice in indici:
        return mic if numar[indice] in mici else mare

    aux = int((mare-mic)/2)
    return find(numar, mic, mic+aux, indice+1) if numar[indice] in mici else find(numar, mare-aux, mare, indice+1)


vect = []
for line in lines:
    vect.append(find(line, 0, 127, 0) * 8 + find(line, 0, 7, 7))

#part one
print(max(vect))

#part two
vect.sort()
for i in range(0, len(vect)-1):
    if vect[i+1] != vect[i] + 1:
        print(vect[i]+1)
