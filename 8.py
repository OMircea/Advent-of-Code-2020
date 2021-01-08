with open("8.txt") as fp:
    instructions = [line.strip() for line in fp.readlines()]
with open("8.txt") as fp:
    lines = fp.read().split('\n')

acc, visited, contor, contorN = 0, [], -1, -1

v = []
for index, val in enumerate(lines):
    instr, modif = val.split(' ')
    v.append([instr, modif])

#part 1
def incercare(v, index, delete = None):
    global acc
    global visited
    global contor
    if index in visited:
        print(acc)
        return

    visited.append(index)
    if 'nop' in v[index][0]:
        incercare(v, index+1)
    if 'acc' in v[index][0]:
        acc += int(v[index][1])
        incercare(v, index + 1)
    if 'jmp' in v[index][0]:
        incercare(v, index + int(v[index][1]), delete)

incercare(v, 0)


def miscari(lines, poz, trb):
    global acc
    global visited
    global contor
    cnt = 0

    for line in lines:
        instr, val = line.split(' ')
        val = int(val)


        if cnt == poz:
            if visited[poz] == 1 or poz > len(lines)-1:
                acc, visited, contor = 0, [0 for i in range(0, len(lines))], -1
                return

            if 'nop' in instr:
                visited[poz] += 1
                poz += 1
                #miscari(lines, poz, trb)
            if 'acc' in instr:
                acc += val
                visited[poz] += 1
                poz += 1

                #miscari(lines, poz, trb)

            if 'jmp' in instr:
                contor+=1
                visited[poz] += 1
                if contor == trb:
                    poz+=1
                    #miscari(lines, poz, trb)

                else:
                    poz+=val
                    miscari(lines, poz, trb)

        cnt += 1
        print(acc)


#part 2

jumps = [i for i in visited if 'jmp' == v[i][0]]
nops = [i for i in visited if 'nop' == v[i][0]]

checking = True
for n in jumps:
    acc = 0
    i = 0
    seen = []

    while checking:
        if i == len(lines):
            print(acc)
            #checking = False  optionala
            break
        if i in seen:
            break

        seen.append(i)
        if i == n:
            i += 1
            continue

        instr = instructions[i].split()
        if instr[0] == 'nop':
            i += 1
            continue
        if instr[0] == 'acc':
            i += 1
            acc += int(instr[1])
            continue
        if instr[0] == 'jmp':
            i += int(instr[1])
            continue

#print(jumps)
