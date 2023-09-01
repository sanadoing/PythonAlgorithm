from collections import deque


def BFS(start):
    queue = deque()
    visited = [0] * (n + 1)
    queue.append((start, 0))
    visited[start] = 1

    while queue:
        current, cnt = queue.popleft()
        if current == b:
            return cnt
        for i in range(1, n + 1):
            if family[current][i] == 1 and visited[i] == 0:
                visited[i] = 1
                queue.append((i, cnt + 1))
    else:
        return -1


n = int(input())
a, b = map(int, input().split())
m = int(input())

family = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    family[x][y], family[y][x] = 1, 1

print(BFS(a))
