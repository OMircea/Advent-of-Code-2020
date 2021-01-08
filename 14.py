from collections import defaultdict
import itertools
with open("14.txt") as fp:
    lines = fp.read().split("\n")

d = defaultdict()

for line in lines:
    if 'mask' in line:
        mask = line.replace("mask = ", "")
    else:
        nr = [int(s) for s in line.replace("[", " ").replace("]", " ").split() if s.isdigit()]
        x = '{0:036b}'.format(nr[0])
        schimbare = ''
        for i in range(0, len(mask)):
            if mask[i] == 'X' or mask[i] == '1':
                schimbare += mask[i]
            else:
                schimbare += x[i]

        lst = list(itertools.product(['0', '1'], repeat=schimbare.count('X')))

        for item in lst:
            new_schimbare = ''
            j = 0
            for i in range(0, len(mask)):
                if schimbare[i] == 'X':
                    new_schimbare += item[j]
                    j += 1
                else:
                    new_schimbare += schimbare[i]

            d[int(new_schimbare, 2)] = nr[1]

print(sum(d.values()))
