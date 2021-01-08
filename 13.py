from functools import reduce
with open("13.txt") as fp:
    lines = fp.read().split("\n")


time_to_wait = int(lines[0])
busses = [elem for elem in lines[1].split(",") if elem != 'x']
for i in range(0, len(busses)):
    busses[i] = int(busses[i])


def partea1():
    for i in range(time_to_wait, time_to_wait+max(busses)+2):
        for elem in busses:
            if i % elem == 0:
                return (i-time_to_wait) * elem


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


def chinese_remainder(n, a):

    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def partea2():

    busses2 = [[int(bus), t] for t, bus in enumerate(lines[1].split(",")) if bus != 'x']
    n = [a1 for a1, a2 in busses2]
    a = [a1-a2 for a1, a2 in busses2]
    return chinese_remainder(n, a)

print("Partea 1:", partea1())
print("Partea 2:", partea2())

