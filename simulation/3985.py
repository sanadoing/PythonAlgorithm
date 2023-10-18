L = int(input())
N = int(input())

cake = [0] * (L + 1)
exp_result, rea_result = 0, 0
exp_max, rea_max = -int(1e9), -int(1e9)

for num in range(1, N + 1):
    s, e = map(int, input().split())
    cnt = 0
    for i in range(s, e + 1):
        if cake[i] == 0:
            cake[i] = num
            cnt += 1

    if exp_max < (e - s + 1):
        exp_result = num
        exp_max = (e - s + 1)

    if rea_max < cnt:
        rea_result = num
        rea_max = cnt

print(exp_result)
print(rea_result)
