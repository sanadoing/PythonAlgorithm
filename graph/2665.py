from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

n = int(input())
board = []
for _ in range(n):
    temp = list(map(int, input()))
    board.append(temp)

queue = deque([])
visited = [[-1] * n for _ in range(n)]
visited[0][0] = 0
queue.append([0, 0])

while queue:
    y, x = queue.popleft()
    if y == n - 1 and x == n - 1:
        print(visited[y][x])
        break
    for i in range(4):
        yy, xx = y + dy[i], x + dx[i]
        if 0 <= yy < n and 0 <= xx < n and visited[yy][xx] == -1:
            if board[yy][xx] == 1:
                queue.appendleft([yy, xx])
                visited[yy][xx] = visited[y][x]
            else:
                queue.append([yy, xx])
                visited[yy][xx] = visited[y][x] + 1
