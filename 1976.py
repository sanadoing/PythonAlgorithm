N = int(input())
M = int(input())
board = []
enabled = []
for y in range(N):
    l = list(map(int, input().split()))
    board.append(l)
    for x in range(N):
        if board[y][x] == 1:
            enabled.append([y, x])
            enabled.append([x, y])
