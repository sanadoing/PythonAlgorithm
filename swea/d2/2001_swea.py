T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    result = -1
    for x in range(N - M + 1):
        y = 0
        while y + M != N + 1:
            temp = 0
            for i in range(M):
                temp += sum(board[y + i][x:x + M])
            y += 1
            result = max(result, temp)

    print(f'#{test_case} {result}')
