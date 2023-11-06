dy = [0, 0, 1, -1]
dx = [-1, 1, 0, 0]

N = int(input())
board = [list(map(str, input())) for _ in range(N)]
result = [0] * 5


def heart(y, x):
    waist_y, waist_x = 0, 0
    for i in range(3):
        yy, xx = y, x

        while True:
            yy, xx = yy + dy[i], xx + dx[i]

            if 0 <= xx < N and 0 <= yy < N and board[yy][xx] == '*':
                result[i] += 1
                waist_y, waist_x = yy, xx

            else:
                break

    yy, xx = waist_y, waist_x - 1
    while True:
        yy, xx = yy + dy[2], xx + dx[2]
        if 0 <= yy < N and board[yy][xx] == '*':
            result[3] += 1
        else:
            break
    yy, xx = waist_y, waist_x + 1
    while True:
        yy, xx = yy + dy[2], xx + dx[2]
        if 0 <= yy < N and board[yy][xx] == '*':
            result[4] += 1
        else:
            break


for y in range(N):
    for x in range(N):
        cnt = 0
        for i in range(4):
            yy, xx = y + dy[i], x + dx[i]
            if 0 <= yy < N and 0 <= xx < N and board[yy][xx] == '*':
                cnt += 1

        if cnt == 4:
            heart(y, x)
            print(y+1, x+1)
            print(' '.join(map(str, result)))
            exit(0)
