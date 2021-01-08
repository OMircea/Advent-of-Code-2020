with open("3.txt") as fp:
    lines = fp.readlines()

def check(char):
    if char is '#':
        return 1
    else:
        return 0

def part_two(lines):
    matrix = []
    i=0
    nrch=31
    for line in lines:
        line = line.rstrip()
        matrix.append(line)
        i+=1
    totTree = 1

    lista = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    for dr, jos in lista:
        nrTree = 0
        inc = 0
        poz = 0
        while inc + jos < i:
            inc+=jos
            if poz+dr >= nrch:
                poz = (poz + dr) % nrch
            else:
                poz += dr
            nrTree += check(matrix[inc][poz])
        totTree*=nrTree

    return totTree

print(part_two(lines))


