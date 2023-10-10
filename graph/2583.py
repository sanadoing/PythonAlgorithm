import sys
sys.setrecursionlimit(100000)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

M, N, K = map(int, input().split())
rec = [list(map(int, input().split())) for _ in range(K)]
graph = [[0] * N for _ in range(N)]
width = []      # 0으로 이루어진 직사각형의 넓이들을 담을 리스트
wid = 0     # 각 직사각형의 넓이를 구하기 위한 임시 변수


def DFS(x, y):  # 0으로 이루어진 하나의 구간을 탐색하기 위한 DFS 함수
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
        # (x_2 - x_1) * (y_2 - y_1)이 직사각형의 넓이 이므로 넓이 만큼 for문을 돌면서 직사각형의 부분(1) 로 표시해줘야 한다.

        graph[x][y] = 1
        x += 1
        if x == x_2:    # 가로 한줄 씩 읽음
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
            #   DFS 함수가 끝났다는 것은 0으로 이루어진 한 구간의 탐색이 끝났다는 것
            width.append(wid)   # 구간의 넓이를 width 함수에 추가해준다.


width.sort()
print(len(width))
print(' '.join(map(str,width)))
