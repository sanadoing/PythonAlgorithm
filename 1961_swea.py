T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    board_90 = [[0] * N for _ in range(N)]
    board_180 = [[0] * N for _ in range(N)]
    board_270 = [[0] * N for _ in range(N)]

    for y in range(N):
        for x in range(N):
            board_90[y][x] = board[N - (x + 1)][y]
    for y in range(N):
        for x in range(N):
            board_180[y][x] = board_90[N - (x + 1)][y]
    for y in range(N):
        for x in range(N):
            board_270[y][x] = board_180[N - (x + 1)][y]

    print(f'#{test_case}')
    for i in range(N):
        print(''.join(map(str, board_90[i])), end=' ')
        print(''.join(map(str, board_180[i])), end=' ')
        print(''.join(map(str, board_270[i])), end=' ')
        print()

