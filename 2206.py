from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]
queue = deque()
queue.append([0, 0, 1, 1])  # y, x, cnt, 벽 부쉴 수 있는 횟수
visited = [[0] * M for _ in range(N)]
visited[0][0] = 1
result = int(1e9)

while queue:
    y, x, cnt, broke = queue.popleft()

    if y == N-1 and x == M-1:
        result = min(result, cnt)

    for i in range(4):
        yy, xx = y + dy[i], x + dx[i]
        if 0 <= yy < N and 0 <= xx < M and visited[yy][xx] == 0:
            if board[yy][xx] == 0:
                queue.append([yy, xx, cnt+1, broke])
            elif board[yy][xx] == 1 and broke > 0:
                queue.append([yy, xx, cnt + 1, broke - 1])
            visited[yy][xx] = 1
    print(queue)

if result == int(1e9):
    print(-1)
else:
    print(result)