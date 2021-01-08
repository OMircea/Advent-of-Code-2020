from itertools import combinations
import math

with open("10.txt") as fp:
    lines = fp.read().split('\n')
    v = [int(line) for line in lines]
k = 0
vect_k=[]
v.sort()
v.insert(0, 0)
v.append(v[len(v)-1]+3)
print(v)
sum1, sum3, comb = 0, 0, 1

for i in range(0, len(v)-1):
    if v[i+1] - v[i] is 1:
        sum1 += 1

    elif v[i + 1] - v[i] is 3:
        sum3 += 1
        vect_k.append(i+1-k)
        k = i+1

print(sum1*sum3)

def nr(n):
    arr = [i for i in range(1, n+1)]
    elem = math.ceil((len(arr)-1) / 3)
    r = [i for i in range(1, len(arr)+1)]
    suma, liste_posibile = 0, []
    for i in r:
        liste_posibile.append(list(combinations(arr, i)))

    for i in range(0, len(r)):
        for j in range(0, len(liste_posibile[i])):
            print(len(liste_posibile[i][j]))
            e1 = liste_posibile[i][j][0]
            e2 = liste_posibile[i][j][len(liste_posibile[i][j])-1]
            if e1 is 1 and e2 is len(r) and len(liste_posibile[i][j]) >= elem+1:
                print(liste_posibile[i][j])
                suma += 1

    return suma

print(vect_k)
vect_k.sort()
print(vect_k)

dict = {3:2, 4:4, 5:7}
comb = 1
for elem in vect_k:
    print(elem)
    if elem > 2:
        comb *= nr(elem)
        #comb*=dict[elem]
print(comb)

'''
from collections import defaultdict
combinations = defaultdict(int, {0: 1})
print(combinations[0])


from collections import defaultdict
from pathlib import Path


with (Path(__file__).parent / "10.txt").open() as fin:
    adapters = list(map(int, map(str.strip, fin)))

adapters.sort()
adapters.append(adapters[-1] + 3)
combinations = defaultdict(int, {0: 1})
print(combinations)
for adapter in adapters:
    #print(adapter)
    combinations[adapter] = sum(combinations[adapter - i - 1] for i in range(3))

print(combinations)

print(f"total number of distinct ways to arrange the adapters: {combinations[adapters[-1]]}")
'''
