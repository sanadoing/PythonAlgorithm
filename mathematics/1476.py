E, S, M = map(int, input().split())

now_e, now_s, now_m = 0, 0, 0
result = 0

while True:

    if now_e == E and now_s == S and now_m == M:
        print(result)
        break

    now_e += 1
    now_s += 1
    now_m += 1

    if now_e == 16:
        now_e = 1
    if now_s == 29:
        now_s = 1
    if now_m == 20:
        now_m = 1

    result += 1
