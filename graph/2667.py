from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def BFS(i, j):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = 1
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0 <= xx < N and 0 <= yy < N and board[xx][yy] == 1 and visited[xx][yy] == 0:
                visited[xx][yy] = 1
                cnt += 1
                queue.append((xx, yy))

    return cnt

N = int(input())
board = [list(map(int, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

group_cnt = 0
result = []

for i in range(N):
    for j in range(N):

        if board[i][j] == 1 and visited[i][j] == 0:
            group_cnt += 1
            result.append(BFS(i, j))


print(group_cnt)
result.sort()
for r in result:
    print(r)

