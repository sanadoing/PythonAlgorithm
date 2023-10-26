N = int(input())

for i in range(1, N + 1):
    now, cnt = i, 0
    while now >= 10:
        temp = now // 10
        if temp % (3 or 6 or 9) == 0:
            cnt += 1
        now = now % 10
    if now % (3 or 6 or 9) == 0 and now != 0:
        cnt += 1
    if cnt == 0:
        print(str(i), end=' ')
    else:
        result = ''
        for c in range(cnt):
            result += '-'
        print(result, end=' ')
