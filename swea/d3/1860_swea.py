T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    time = list(map(int, input().split()))
    time.sort()
    bread = [0] * (time[-1] + 1)
    for i in range(1, time[-1] + 1):
        if i % M == 0:
            bread[i] += K
        bread[i] += bread[i - 1]
    eat = 0
    result = 'Impossible'
    before = -1
    for i in range(len(time)):
        if before != time[i]:
            bread[time[i]] -= eat
        before = time[i]
        if bread[time[i]] > 0:
            eat += 1
            bread[time[i]] -= 1
        else:
            break
    else:
        result = 'Possible'
    print(f'#{test_case} {result}')
