from collections import deque

# 오 -> 왼 -> 아래
dy = [0, 0, 1]
dx = [1, -1, 0]

T = 10


def go(sy, sx, sd):
    queue = deque()
    queue.append([sy, sx, sd])

    while queue:
        y, x, d = queue.popleft()

        if d == 2:
            for i in range(3):
                yy, xx = y + dy[i], x + dx[i]
                if 0 <= yy < 100 and 0 <= xx < 100:
                    if board[yy][xx] == 1:
                        queue.append([yy, xx, i])
                        break
                    elif board[yy][xx] == 2:
                        return sx
        else:
            for i in range(3):
                if i == d or i == 2:
                    yy, xx = y + dy[i], x + dx[i]
                    if 0 <= yy < 100 and 0 <= xx < 100:
                        if board[yy][xx] == 1:
                            queue.append([yy, xx, i])
                            break
                        elif board[yy][xx] == 2:
                            return sx

    return 0


for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]

    for x in range(100):
        if board[0][x] == 1:
            result = go(0, x, 2)

            if result != 0:  # y, x, direction
                print(f'#{test_case} {result}')
                break
