import itertools
from collections import deque
with open("22.txt") as f:
    p1, p2 = f.read().split("\n\n")


def extract(p):
    v = deque()
    for line in p.split('\n'):
        if line.isdigit():
            v.append(int(line))
    return v


def check_sum(v):
    total = 0
    for i, elem in enumerate(v):
        total += (len(v)-i) * elem
    return total


def part1(v1, v2):
    while v1 and v2:
        x, y = v1.popleft(), v2.popleft()
        v1.extend([x, y]) if x > y else v2.extend([y, x])
    return check_sum(v1) if v1 else check_sum(v2)


def part2(v1, v2):
    state = []
    while v1 and v2:
        if [list(v1), list(v2)] in state:
            return 0
        else:
            state.append([list(v1), list(v2)])
        x, y = v1.popleft(), v2.popleft()
        if x <= len(v1) and y <= len(v2):
            aux1, aux2 = deque(), deque()
            aux1.extend(list(itertools.islice(v1, 0, x)))
            aux2.extend(list(itertools.islice(v2, 0, y)))
            v2.extend([y, x]) if part2(aux1, aux2) else v1.extend([x, y])
        else:
            v1.extend([x, y]) if x > y else v2.extend([y, x])

    if (not v1 and len(v2) is 50) or (not v2 and len(v1) is 50):
        return check_sum(v1) if v1 else check_sum(v2)

    if (not v1 or not v2) and (len(v1) != 50 and len(v2) != 50):
        return 1 if v2 else 0


v1, v2 = extract(p1), extract(p2)
# print(part1(v1, v2))
print(part2(v1, v2))
