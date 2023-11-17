T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    multi = []
    for i in range(N):
        for j in range(i + 1, N):
            multi.append(numbers[i] * numbers[j])
    multi.sort()
    for i in range(len(multi) - 1, -1, -1):
        now = str(multi[i])
        for i in range(len(now) - 1):
            if now[i] > now[i + 1]:
                break
        else:
            print(f'#{test_case} {now}')
            break
    else:
        print(f'#{test_case} -1')
