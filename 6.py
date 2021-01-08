with open("6.txt") as fp:
    lines = fp.read().split('\n')


def checkDict(d, n):
    s=0
    for key in d:
        if d[key] is n:
            s+=1
    return s


def part_one_and_two():

    suma, suma2, n= 0, 0, 0
    s = set()
    d = {}
    for line in lines:
        if line is '':
            suma+=len(s)
            suma2+=checkDict(d, n)
            s.clear()
            d.clear()
            n=0
        else:
            for elem in line:
                s.add(elem)
                if elem not in d.keys():
                    d[elem] = 1
                else:
                    d[elem]+= 1
            n+=1
    suma+=len(s)
    suma2+=checkDict(d, n)
    return suma, suma2


print(part_one_and_two())
