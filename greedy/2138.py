def change(first, target):
    first_copy = first[:]
    cnt = 0
    for i in range(1, N):

        if first_copy[i - 1] == target[i - 1]:
            continue

        cnt += 1
        for j in range(i - 1, i + 2):
            if j < N:
                first_copy[j] = 1 - first_copy[j]

    if first_copy == target:
        return cnt
    else:
        return 1e9


N = int(input())
first = list(map(int, input()))
target = list(map(int, input()))

# 0번째 전구 끈 경우
res = change(first, target)

# 0번째 전구 킨 경우
first[0] = 1 - first[0]
first[1] = 1 - first[1]

res = min(res, change(first, target) + 1)

if res != 1e9:
    print(res)
else:
    print(-1)
