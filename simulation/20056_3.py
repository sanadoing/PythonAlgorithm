dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())
fireballs = []
board = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    _r, _c, _m, _s, _d = map(int, input().split())
    fireballs.append([_r + 1, _c + 1, _m, _s, _d])

for _ in range(K):

    while fireballs:
        _r, _c, _m, _s, _d = fireballs.pop()

        nr = (_r + dy[_d] * _s) % N
        nc = (_c + dx[_d] * _s) % N

        board[nr][nc].append([_m, _s, _d])

    for y in range(N):
        for x in range(N):
            if len(board[y][x]) > 1:
                sum_m, sum_s, cnt_even, cnt_odd, cnt = 0, 0, 0, 0, len(board[y][x])
                while board[y][x]:
                    _m, _s, _d = board[y][x].pop()
                    sum_m += _m
                    sum_s += _s
                    if _d % 2 == 0:
                        cnt_even += 1
                    else:
                        cnt_odd += 1

                if cnt == cnt_even or cnt == cnt_odd:
                    new_d = [0, 2, 4, 6]
                else:
                    new_d = [1, 3, 5, 7]

                if sum_m // 5 > 0:
                    for d in new_d:
                        fireballs.append([y, x, sum_m//5, sum_s//cnt, d])

            if len(board[y][x]) == 1:
                fireballs.append([y, x] + board[y][x].pop())


print(sum(f[2] for f in fireballs))
