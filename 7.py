from collections import defaultdict
with open("7.txt") as fp:
    lines = fp.read().split('\n')


def part_one(d, search_list, final):
    if not search_list:
        return

    new_list = []
    for elem in search_list:
        for par, val in d.items():
            final += [par for valori in val if elem in valori and par not in final]
            new_list = [par for valori in val if elem in valori and par not in final]
    part_one(d, new_list, final)
    return len(final)


def part_two(d, for_search, total):
    if 'no other' in for_search:
        return

    for par, val in d.items():
        for valori in val:
            if valori[0].isdigit() and for_search in par:
                tmp = part_two(d, valori[2:-5], 0)
                total+= int(valori[0])+int(valori[0])*tmp
    return total


d = defaultdict(list)
search = []
for line in lines:
    parent, children = line.split(' bags contain ')
    for c in children.strip(',.').split(', '):
        d[parent].append(c)
        if 'shiny gold' in c:
            search.append(parent)


print(part_one(d, search, search))
print(part_two(d, 'shiny gold', 0))

'''
from collections import defaultdict, deque
import re

with open("7.txt") as f:
    lines = [x.strip() for x in f.readlines()]


class Child:
    def __init__(self, color, count):
        self.color = color
        self.count = count


contained_in = defaultdict(list)
contains = defaultdict(list)

for line in lines:
    children = re.findall(r"(\d) (\w+ \w+)", line)
    parent = " ".join(line.split()[:2])
    for count, color in children:
        contained_in[color].append(parent)
        contains[parent].append(Child(color, int(count)))


def bfs(color):
    color_contains = set()
    q = deque([color])
    while q:
        u = q.popleft()
        for v in contained_in[u]:
            if v not in color_contains:
                #print(color_contains)
                color_contains.add(v)
                q.append(v)
    return color_contains


def get_weight(color):
    w = 0
    for child in contains[color]:
        w += child.count * (1 + get_weight(child.color))
    return w

import time
st = time.time()
print("Part 1:", len(bfs("shiny gold")))
sf = time.time()
print(sf-st)
print("Part 2:", get_weight("shiny gold"))

'''