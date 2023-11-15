dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    if N == 1:
        result = farm[0][0]
    else:
        result = 0
        for i in range(N // 2 + 1):
            result += sum(farm[i][N // 2 - i:N // 2 + i + 1])
        for i in range(1, N // 2 + 1):
            result += sum(farm[N // 2 + i][0 + i:N - i])
    print(f'#{test_case} {result}')
