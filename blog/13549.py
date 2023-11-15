from collections import deque

N, K = map(int, input().split())

visited = [0] * 100001

queue = deque()
queue.append([N, 0])
visited[N] = 1

while queue:
    n, cnt = queue.popleft()
    if n == K:
        print(cnt)
        break
    if 0 <= n - 1 <= 100000 and visited[n - 1] == 0:
        queue.append([n - 1, cnt + 1])
        visited[n - 1] = 1
    if 0 <= n * 2 <= 100000 and visited[n * 2] == 0:
        queue.append([n * 2, cnt])
        visited[n * 2] = 1
    if 0 <= n + 1 <= 100000 and visited[n + 1] == 0:
        queue.append([n + 1, cnt + 1])
        visited[n + 1] = 1
