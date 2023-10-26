from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
queue = deque()
queue.append([0, 0, 0])  # y, x, cnt
visited = [[0] * M for _ in range(N)]
visited[0][0] = 1
result = int(1e9)

while queue:
    y, x, cnt = queue.popleft()
    if y == N - 1 and x == M - 1:
        result = min(result, cnt)

    for i in range(4):
        yy, xx = y + dy[i], x + dx[i]

        if 0 <= yy < N and 0 <= xx < M and visited[yy][xx] == 0:
            if board[yy][xx] == 0:
                queue.append([yy, xx, cnt + 1])
            elif board[yy][xx] == 2:   #    전설의 명검을 구하게 되면, 제한없이 벽을 뚫을 수 있으므로
                result = min(result, cnt + (N - 1 - yy) + (M - 1 - xx) + 1)

            visited[yy][xx] = 1

if result <= T:
    print(result)
else:
    print("Fail")
