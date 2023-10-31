dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]


def DFS(sy, sx):
    global board, c
    for i in range(4):
        yy, xx = sy + dy[i], sx + dx[i]
        if 0 <= yy < N and 0 <= xx < N:
            if board[yy][xx] == board[sy][sx] + 1:
                c += 1
                DFS(yy, xx)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    cnt, result = 0, []
    for y in range(N):
        for x in range(N):
            c = 1
            DFS(y, x)
            if cnt < c:
                cnt = c
                result = [[board[y][x], cnt]]
            elif cnt == c:
                result.append([board[y][x], cnt])
    result.sort()
    print(f'#{test_case} {result[0][0]} {result[0][1]}')
