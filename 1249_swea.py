from collections import deque

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

T = int(input())


def BFS(n, visited, time, board):
    global result
    queue = deque()
    queue.append([0, 0])
    visited[0][0] = 1
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            yy, xx = y + dy[i], x + dx[i]
            if 0 <= yy < n and 0 <= xx < n:
                if visited[yy][xx] == 0:
                    visited[yy][xx] = 1
                    time[yy][xx] = time[y][x] + board[yy][xx]
                    queue.append([yy, xx])
                else:
                    if time[yy][xx] > time[y][x] + board[yy][xx]:
                        time[yy][xx] = time[y][x] + board[yy][xx]
                        queue.append([yy, xx])


for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    time = [[0] * N for _ in range(N)]

    BFS(N, visited, time, board)

    print(f'#{test_case} {time[N - 1][N - 1]}')
