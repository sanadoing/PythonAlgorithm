A, B = map(int, input().split())

num = 1
cnt = 1
result = 0
t = False
for i in range(1, max(A, B) + 1):  # 1 ~ 7까지 반복
    if min(A, B) == i:
        t = True

    if t:
        result += num

    if cnt == num:
        cnt = 0
        num += 1

    cnt += 1

print(result)
