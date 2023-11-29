from collections import deque, defaultdict

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

R, C = map(int, input().split())
lake = []
swan = []
distance = [[int(1e9)] * C for _ in range(R)]
visited = [[False] * C for _ in range(R)]

for i in range(R):
    temp = list(input())
    lake.append(temp)
    for j in range(C):
        if temp[j] == 'L':
            swan.append([i, j])


def meet(y, x):
    global visited
    queue = deque([])
    queue.append([y, x])
    distance[y][x] = 0
    visited = [[False] * C for _ in range(R)]
    visited[y][x] = True

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            yy, xx = y + dy[i], x + dx[i]
            if 0 <= yy < R and 0 <= xx < C and visited[yy][xx] == False:
                visited[yy][xx] = True
                if lake[yy][xx] == '.':
                    distance[yy][xx] = min(distance[y][x], distance[yy][xx])
                    queue.appendleft([yy, xx])
                elif lake[yy][xx] == 'X':
                    distance[yy][xx] = min(distance[y][x] + 1, distance[yy][xx])
                    queue.append([yy, xx])
                else:
                    return


meet(swan[0][0], swan[0][1])
meet(swan[1][0], swan[1][1])

queue = deque([])
queue.append([swan[0][0], swan[0][1]])
visited = [[False] * C for _ in range(R)]
visited[swan[0][0]][swan[0][1]] = True
result = -1

for d in distance:
    print(d)
while queue:
    y, x = queue.popleft()

    for i in range(4):
        yy, xx = y + dy[i], x + dx[i]
        if 0 <= yy < R and 0 <= xx < C and visited[yy][xx] == False:
            visited[yy][xx] = True
            for v in visited:
                print(v)
            print()
            if lake[yy][xx] == 'L':
                print(result)
                exit(0)
            if distance[yy][xx] - distance[y][x] == 0:
                result = max(result, distance[yy][xx])
                queue.appendleft([yy, xx])
            if abs(distance[yy][xx] - distance[y][x]) == 1:
                queue.append([yy, xx])
