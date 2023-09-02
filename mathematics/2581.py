M = int(input())
N = int(input())
min_num = 0
sum_num = 0

for num in range(M, N + 1):
    cnt = 0
    for i in range(1, num + 1):
        if cnt > 2:
            break
        if num % i == 0:
            cnt += 1

    if cnt == 2:
        sum_num += num
        if min_num == 0:
            min_num = num

if sum_num == 0:
    print(-1)
else:
    print(sum_num)
    print(min_num)
