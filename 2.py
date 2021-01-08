with open("2.txt") as fp:
    lines = fp.readlines()

cnt = 0
cnt2 = 0
for line in lines:
    line = line.split(":")
    line[0] = line[0].split()
    line[0][0] = line[0][0].split("-")
    min = int(line[0][0][0])
    max = int(line[0][0][1]) + 1

    valori = range(min, max)
    if line[1].count(line[0][1]) in valori:
        cnt+=1

    vect = []
    poz=1
    line[1] = line[1].strip()
    for char in line[1]:
        if char == line[0][1]:
            vect.append(poz)
        poz+=1

    max-=1
    if min in vect or max in vect:
        if min in vect and max in vect:
            pass
        else:
            cnt2+=1

print(cnt)
print(cnt2)
