import copy

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
dyx = [[0, 1], [1, 0], [1, 1]]

N = int(input())
board = [[0] * 101 for _ in range(101)]
result = 0


def go_dragon(sx, sy, d, g):
    global board
    stack = [d]
    board[sy][sx] = 1
    temp_stack = []

    y, x = sy, sx

    for _ in range(g + 1):

        while stack:
            td = stack.pop()
            y += dy[td]
            x += dx[td]
            board[y][x] = 1

            temp_stack.append((td + 1) % 4)

        stack = copy.deepcopy(temp_stack)


for _ in range(N):
    x, y, d, g = map(int, input().split())
    go_dragon(x, y, d, g)

for y in range(100):
    for x in range(100):
        if board[y][x] == 1:
            cnt = 0
            for i in range(3):
                yy, xx = y + dyx[i][0], x + dyx[i][1]
                if 0 <= yy <= 100 and 0 <= xx <= 100:
                    if board[yy][xx] == 1:
                        cnt += 1
            if cnt == 3:
                result += 1

print(result)
