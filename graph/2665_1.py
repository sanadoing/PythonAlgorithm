from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

n = int(input())
board = [list(map(int, input())) for _ in range(n)]
visited = [[-1] * n for _ in range(n)]
queue = deque()
queue.append([0, 0])
visited[0][0] = 0
while queue:
    y, x = queue.popleft()
    if y == n - 1 and x == n - 1:
        print(visited[y][x])
        break
    for i in range(4):
        yy, xx = y + dy[i], x + dx[i]
        if 0 <= yy < n and 0 <= xx < n and visited[yy][xx] == -1:
            if board[yy][xx] == 1:
                visited[yy][xx] = visited[y][x]
                queue.appendleft([yy, xx])
            else:
                visited[yy][xx] = visited[y][x] + 1
                queue.append([yy, xx])
