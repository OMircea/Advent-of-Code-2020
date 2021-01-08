with open("19.txt") as f:
    rules, test = f.read().split("\n\n")


rules = rules.split('\n')
reguli = {}
print(rules)
for elem in rules:
    elem = elem.split(": ")
    #print(elem)
    sub = elem[1]
    if "|" in sub:
        sub = sub.split(" | ")
    else:
        sub = [sub]
    for i in range(len(sub)):
        sub[i] = sub[i].split(" ")

    reguli[elem[0]] = sub
print(reguli)


print("sdaS")
def part1(reguli, nr):
    sir = []
    if reguli[nr][0][0] == '"a"':
        return ["a"]
    if reguli[nr][0][0] == '"b"':
        return ["b"]

    for elem in reguli[nr]:
        if len(elem) is 1:
            sir += part1(reguli, elem[0])

        else:
            p1 = part1(reguli, elem[0])
            p2 = part1(reguli, elem[1])
            for x in p1:
                for y in p2:
                    sir += [x+y]
            #sir += [x+y for x in p1 for y in p2]
    print(sir, nr)
    return sir


poss = part1(reguli, '0')
for i, elem in enumerate(poss):
    print(i, elem)
print("ajunge aici")
count = 0
test = test.split('\n')
for de_test in test:
    print(de_test)
    if de_test in poss:
        count += 1



print("ajunge aici")
print(count)
