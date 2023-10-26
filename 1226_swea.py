from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

T = 10


def BFS(sy, sx):
    visited = [[0] * 16 for _ in range(16)]
    visited[sy][sx] = 1
    queue = deque()
    queue.append([sy, sx])

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            yy, xx = y + dy[i], x + dx[i]
            if 0 <= yy < 16 and 0 <= xx < 16:
                if visited[yy][xx] == 0:
                    if board[yy][xx] == 0:
                        visited[yy][xx] = 1
                        queue.append([yy, xx])
                    elif board[yy][xx] == 3:
                        return 1
    return 0


for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input())) for _ in range(16)]
    result = BFS(1, 1)
    print(f'#{test_case} {result}')
