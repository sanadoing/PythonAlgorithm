from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

N, M = map(int, input().split())
board = []
visited = [[0] * M for _ in range(N)]
result = [[0] * M for _ in range(N)]
queue = deque()
sy, sx = 0, 0
for i in range(N):
    temp = list(map(int, input().split()))
    if 2 in temp:
        sy, sx = i, temp.index(2)
    board.append(temp)

queue.append([sy, sx])
visited[sy][sx] = 1
while queue:
    y, x = queue.popleft()
    for i in range(4):
        yy, xx = y + dy[i], x + dx[i]
        if 0 <= yy < N and 0 <= xx < M and visited[yy][xx] == 0:

            if board[yy][xx] == 1:
                visited[yy][xx] = 1
                result[yy][xx] = result[y][x] + 1
                queue.append([yy, xx])
            else:
                visited[yy][xx] = 1

for y in range(N):
    for x in range(M):
        if visited[y][x] == 0:
            if board[y][x] == 0:
                result[y][x] = 0
            else:
                result[y][x] = -1


for r in result:
    print(' '.join(map(str, r)))
