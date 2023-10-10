import sys
sys.setrecursionlimit(100000)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

M, N, K = map(int, input().split())
rec = [list(map(int, input().split())) for _ in range(K)]
graph = [[0] * N for _ in range(N)]
width = []
wid = 0


def DFS(x, y):
    global wid
    for d in range(4):
        xx = dx[d] + x
        yy = dy[d] + y
        if 0 <= xx < M and 0 <= yy < N and graph[xx][yy] == 0:
            graph[xx][yy] = 1
            DFS(xx, yy)
            wid += 1


for i in range(K):
    y_1, x_1, y_2, x_2 = rec[i][0], rec[i][1], rec[i][2], rec[i][3]
    x, y = x_1, y_1
    for j in range((x_2 - x_1) * (y_2 - y_1)):
        graph[x][y] = 1
        x += 1
        if x == x_2:
            y += 1
            x = x_1
        if y == y_2:
            break



for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            graph[i][j] = 1
            wid = 1
            DFS(i, j)

            width.append(wid)


width.sort()
print(len(width))
print(' '.join(map(str,width)))
