T = int(input())


def DFS(c):
    global result
    if c == 0:
        temp = ''.join(N)
        result = max(result, int(temp))
    else:
        for i in range(len(N)):
            for j in range(i+1, len(N)):
                N[i], N[j] = N[j], N[i]
                temp = ''.join(N)
                if check.get((temp, c - 1), 1):
                    check[(temp, c-1)] = 0
                    DFS(c-1)
                N[i], N[j] = N[j], N[i]

for test_case in range(1, T + 1):
    N, cnt = input().split()
    cnt = int(cnt)
    N = list(N)
    result = -1
    check = dict()
    DFS(cnt)
    print(f'#{test_case} {result}')
