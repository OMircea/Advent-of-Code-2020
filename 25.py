card_pk, door_pk = 14082811, 5249543

x, cnt, loop_size_card, loop_size_door, ok1, ok2 = 1, 0, 0, 0, 0, 0
while not ok1 or not ok2:
    cnt += 1
    x = 7*x
    x = x % 20201227

    if x == card_pk:
        loop_size_card = cnt
        ok1 += 1
    if x == door_pk:
        loop_size_door = cnt
        ok2 += 1

print(loop_size_card, loop_size_door)


x, cnt = 1, 0
while cnt < loop_size_door:
    x *= card_pk
    x = x % 20201227
    cnt += 1

print(x)

