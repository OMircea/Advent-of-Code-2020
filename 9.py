from collections import deque
with open("9.txt") as fp:
    lines = fp.read().split('\n')
    v = [int(line) for line in lines]

queue = deque()
for poz, elem in enumerate(v):
    if poz < 25:
        queue.append(elem)
    else:
        ok = 0
        for nr1 in queue:
            for nr2 in queue:
                if nr1 + nr2 == elem and nr1 != nr2:
                    ok += 1
                    continue
        if not ok:
            print(elem, poz)
            break
        queue.append(elem)
        queue.popleft()

left, right = 0, 0
suma = v[left]

while suma != v[poz]:

    if suma < v[poz]:
        right += 1
        suma += v[right]

    elif suma > v[poz]:
        suma -= v[left]
        left += 1

y = [v[i] for i in range(left, right)]
print(max(y)+min(y))


