from collections import deque
from copy import deepcopy

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]
R, C = map(int, input().split())
lake = []
swan = []
result = 0

visited = [[0] * C for _ in range(R)]


def meeting():
    global result, visited
    queue = deque([swan[0]])
    visited = [[0] * C for _ in range(R)]
    visited[swan[0][0]][swan[0][1]] = 1
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            yy, xx = y + dy[i], x + dx[i]
            if 0 <= yy < R and 0 <= xx < C and visited[yy][xx] == 0:
                if lake[yy][xx] == '.':
                    visited[yy][xx] = 1
                    queue.append([yy, xx])
                elif lake[yy][xx] == 'L':
                    print(result)
                    exit(0)


def melting_ice():
    global lake, visited
    visited = [[0] * C for _ in range(R)]

    for y in range(R):
        for x in range(C):
            if lake[y][x] == '.' and visited[y][x] == 0:
                queue = deque([[y, x]])
                visited[y][x] = 1
                while queue:
                    ny, nx = queue.popleft()
                    for i in range(4):
                        yy, xx = ny + dy[i], nx + dx[i]
                        if 0 <= yy < R and 0 <= xx < C and visited[yy][xx] == 0:
                            visited[yy][xx] = 1
                            if lake[yy][xx] == 'X':
                                lake[yy][xx] = '.'
                            elif lake[yy][xx] == '.':
                                queue.append([yy, xx])


for i in range(R):
    temp = list(input())
    lake.append(temp)
    for j in range(C):
        if temp[j] == 'L':
            swan.append([i, j])

while True:
    meeting()
    melting_ice()
    result += 1
