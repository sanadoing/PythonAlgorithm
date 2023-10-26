
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

T = int(input())


def move(y, x, cnt, string):
    global numbers
    if cnt == 6:
        numbers.append(string)
    else:
        for i in range(4):
            yy, xx = y + dy[i], x + dx[i]
            if 0 <= yy < 4 and 0 <= xx < 4:
                move(yy, xx, cnt + 1, string + str(board[yy][xx]))


for test_case in range(1, T + 1):

    board = [list(map(int, input().split())) for _ in range(4)]
    numbers = []
    for y in range(4):
        for x in range(4):
            move(y, x, 0, str(board[y][x]))

    print(f'#{test_case} {len(set(numbers))}')
