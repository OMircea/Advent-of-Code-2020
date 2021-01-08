from collections import defaultdict
from itertools import product
with open('17.txt') as f:
    cuburi = set((r, c) for r, line in enumerate(f.read().splitlines()) for c, line2 in enumerate(line) if line2 == '#')

C = 6


def solve(cuburi, dim):
    i, cuburi = 0, set(cub + (0,) * (dim-len(cub)) for cub in cuburi)
    while i < C:
        nCuburi = set()
        vec = defaultdict(int)
        for shift in product((-1, 0, 1), repeat=dim):
            for cub in cuburi:
                if shift != (0, ) * dim:
                    vecin = tuple(x + y for x, y in zip(cub, shift))
                    vec[vecin] += 1

        for k, v in vec.items():
            if k in cuburi and (v == 2 or v == 3):
                nCuburi.add(k)
            elif k not in cuburi and v == 3:
                nCuburi.add(k)
        cuburi = nCuburi
        i += 1
    return len(cuburi)


print(solve(cuburi, 3))
print(solve(cuburi, 4))

