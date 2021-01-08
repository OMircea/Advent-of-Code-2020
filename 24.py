from collections import defaultdict
with open("24.txt") as f:
    orders = f.read().split()

move = {'e': [2, 0], 'w': [-2, 0], 'nw': [-1, -2], 'sw': [-1, 2], 'ne': [1, -2], 'se': [1, 2]}

def divide(orders):
    diag, vect = ['n', 's'], []
    for order in orders:
        inner_vect = []
        i = 0
        while i < len(order):
            if order[i] in diag:
                inner_vect.append(order[i]+order[i+1])
                i += 2
            else:
                inner_vect.append(order[i])
                i += 1
        vect.append(inner_vect)
    return vect


def part1(vect):

    d = defaultdict()
    for tile in vect:
        x, y = 0, 0
        for inner_move in tile:
            x += move[inner_move][0]
            y += move[inner_move][1]
        tpl = (x, y)
        if tpl not in d or d[tpl] == 0:
            d[tpl] = 1
        else:
            d[tpl] = 0

    return d


vect = divide(orders)
d = part1(vect)
print(sum(d.values()))  # part 1

for day in range(100):
    new_d = defaultdict()
    verificari_ulterioare = []
    for elem in d.keys():
        number_of_one = 0
        x, y = elem[0], elem[1]

        for miscare in move.values():
            x += miscare[0]
            y += miscare[1]
            if (x, y) not in d:
                verificari_ulterioare.append([x, y])
            else:
                if d[(x, y)] == 1:
                    number_of_one += 1
            x -= miscare[0]
            y -= miscare[1]

        tpl, ok = (x, y), 0
        if d[tpl] == 1 and (number_of_one == 0 or number_of_one > 2):
            new_d[tpl] = 0
        elif d[tpl] == 0 and number_of_one == 2:
            new_d[tpl] = 1
        else:
            new_d[tpl] = d[tpl]


    for elem in verificari_ulterioare:
        number_of_one = 0
        x, y = elem[0], elem[1]
        for miscare in move.values():
            x += miscare[0]
            y += miscare[1]
            if (x, y) in d:
                if d[(x, y)] == 1:
                    number_of_one += 1
            x -= miscare[0]
            y -= miscare[1]
        tpl = (x, y)
        if number_of_one == 2:
            new_d[tpl] = 1

    d = new_d

print("day: ", day+1, sum(d.values()))
