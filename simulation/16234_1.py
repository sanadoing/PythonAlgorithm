from collections import deque

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
result = 0
visited = [[0] * N for _ in range(N)]


def BFS(s_y, s_x):
    global visited
    team = []
    queue = deque()
    team.append([s_y, s_x])
    queue.append([s_y, s_x])

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            yy, xx = y + dy[i], x + dx[i]
            if 0 <= yy < N and 0 <= xx < N:
                if visited[yy][xx] == 0 and L <= abs(board[y][x] - board[yy][xx]) <= R:
                    visited[yy][xx] = 1
                    queue.append([yy, xx])
                    team.append([yy, xx])

    return team


while True:
    visited = [[0] * N for _ in range(N)]

    flag = False

    for y in range(N):
        for x in range(N):
            if visited[y][x] == 0:

                visited[y][x] = 1
                one_team = BFS(y, x)

                if len(one_team) > 1:
                    flag = True
                    new_number = sum(board[t[0]][t[1]] for t in one_team) // len(one_team)

                    for o in one_team:
                        board[o[0]][o[1]] = new_number

    if not flag:
        print(result)
        break

    result += 1
