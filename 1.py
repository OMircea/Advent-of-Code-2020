file = open("1.txt", "r")
x = file.read()
x = x.split()

def inmultire(x):
    for elem1 in x:
        for elem2 in x:
            for elem3 in x:
                if (int(elem1) + int(elem2) + int(elem3)) == 2020:
                    return int(elem1) * int(elem2) * int(elem3)

from time import time

start = time()
print(inmultire(x))
end = time()

print(end-start)




'''
# Open the input file
inputfile = open('1.txt', 'r')

# Parse lines to array of numbers
lines = inputfile.readlines()
entries = [int(x.strip()) for x in lines]

def part1(entries):
    rests = set()
    print(type(rests))

    for x in entries:
        rest = 2020 - x
        if rest in rests:
            return rest * x
        else:
            rests.add(x)

print(part1(entries))
'''