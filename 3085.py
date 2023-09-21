dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

N = int(input())
candy = [list(map(str, input())) for _ in range(N)]
max_cnt = 0


def check():
    global max_cnt
    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if candy[i][j - 1] == candy[i][j]:
                cnt += 1
                max_cnt = max(cnt, max_cnt)
            else:
                cnt = 1
        cnt = 1
        for j in range(1, N):
            if candy[j - 1][i] == candy[j][i]:
                cnt += 1
                max_cnt = max(cnt, max_cnt)
            else:
                cnt = 1


for i in range(N):
    for j in range(N):
        if i + 1 < N:
            candy[i][j], candy[i + 1][j] = candy[i + 1][j], candy[i][j]
            check()
            candy[i][j], candy[i + 1][j] = candy[i + 1][j], candy[i][j]

        if j + 1 < N:
            candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]
            check()
            candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]

print(max_cnt)
