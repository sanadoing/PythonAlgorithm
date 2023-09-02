N = int(input())
num = list(map(int, input().split()))
result = 0

for i in range(N):
    cnt = 0
    for j in range(1, num[i] + 1):
        if cnt > 2:


            break
        if num[i] % j == 0:
            cnt += 1

    if cnt == 2:
        result += 1

print(result)
