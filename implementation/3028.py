move = list(map(str, input()))
ball = 1

for m in move:

    if m == 'A':    # 1 -> 2 / 2 -> 1
        if ball == 1:
            ball = 2
        elif ball == 2:
            ball = 1
    elif m == 'B':  # 2 -> 3 / 3 -> 2
        if ball == 2:
            ball = 3
        elif ball == 3:
            ball = 2
    else:   # 1 -> 3 / 3 -> 1
        if ball == 1:
            ball = 3
        elif ball == 3:
            ball = 1


print(ball)