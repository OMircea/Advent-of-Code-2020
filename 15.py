from collections import defaultdict
with open("15.txt") as fp:
    lines = fp.read().split("\n")



x = []
for line in lines:
    x = line.split(",")
xx=[]
for elem in x:
    xx.append(int(elem))
x = xx

print(x)

def day15(elem):
    dict = { k : i+1 for i, k in enumerate(x)}
    last = x[-1]

    for i in range(len(x) + 1, elem + 1):
        if last in dict:
            current = i - 1 - dict[last]
        else:
            current = 0
        dict[last] = i - 1
        last = current

    print(last)

day15(2020)
day15(30000000)