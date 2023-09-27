N = int(input())
candy = [list(map(str, input())) for _ in range(N)]
result = 0


def mx_search():
    global result

    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if candy[i][j - 1] == candy[i][j]:
                cnt += 1
                result = max(result, cnt)
            else:
                cnt = 1

        cnt = 1
        for j in range(1, N):
            if candy[j - 1][i] == candy[j][i]:
                cnt += 1
                result = max(result, cnt)
            else:
                cnt = 1


for i in range(N):
    for j in range(N):
        if i + 1 < N:
            candy[i][j], candy[i + 1][j] = candy[i + 1][j], candy[i][j]
            mx_search()
            candy[i][j], candy[i + 1][j] = candy[i + 1][j], candy[i][j]
        if j + 1 < N:
            candy[i][j + 1], candy[i][j] = candy[i][j], candy[i][j + 1]
            mx_search()
            candy[i][j + 1], candy[i][j] = candy[i][j], candy[i][j + 1]

print(result)
