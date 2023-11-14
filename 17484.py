from collections import deque

dx = [-1, 0, 1]
N, M = map(int, input().split())
oil = [list(map(int, input().split())) for _ in range(N)]
queue = deque([])
result = int(1e9)
for x in range(M):
    queue.append([0, x, 3, oil[0][x]])

while queue:
    now_y, now_x, d, total = queue.popleft()
    if now_y == N - 1:
        result = min(result, total)
    else:
        for i in range(3):
            yy = now_y + 1
            xx = now_x + dx[i]
            if d == i:
                continue
            else:
                if 0 <= yy < N and 0 <= xx < M:
                    queue.append([yy, xx, i, total + oil[yy][xx]])

print(result)
