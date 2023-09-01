from collections import deque


def DFS(start):

    for i in range(1, N + 1):
        if board[start][i] == 1 and visted[i] == 0:
            visted[i] = 1
            result.append(i)
            DFS(i)
    else:
        return


def BFS(start):
    queue = deque()
    queue.append(start)
    result.append(start)

    while queue:
        x = queue.popleft()

        for i in range(1, N + 1):

            if board[x][i] == 1 and visted[i] == 0:
                result.append(i)
                visted[i] = 1
                queue.append(i)

    print(' '.join(map(str, result)))


N, M, V = map(int, input().split())
board = [[0] * (N + 1) for _ in range(N + 1)]
result = []

for _ in range(M):
    x, y = map(int, input().split())
    board[x][y], board[y][x] = 1, 1

visted = [0] * (N + 1)
visted[V] = 1
result.append(V)
DFS(V)
print(' '.join(map(str, result)))

visted = [0] * (N + 1)
visted[V] = 1
result.clear()
BFS(V)
