from collections import deque
import sys
input = sys.stdin.readline

dh = [-1, 1]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

M, N, H = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[0] * M for _ in range(N)] for _ in range(H)]

queue = deque()

day = 1  # 토마토가 모두 익기위한 일 수

zero_cnt = 0

for h in range(H):
    for i in range(N):
        for j in range(M):
            if tomato[h][i][j] == 1:
                visited[h][i][j] = day
                queue.append((h, i, j))

            elif tomato[h][i][j] == 0:
                zero_cnt += 1

if zero_cnt == 0:
    print(0)

else:
    while queue:
        h, x, y = queue.popleft()

        for i in range(4):  # 동서남북 네 방향을 탐색
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < N and 0 <= yy < M and visited[h][xx][yy] == 0 and tomato[h][xx][yy] == 0:
                tomato[h][xx][yy] = 1
                visited[h][xx][yy] = visited[h][x][y] + 1
                queue.append((h, xx, yy))

        for i in range(2):  # 마주보는 위 아래층 토마토 박스 탐색
            hh = h + dh[i]
            if 0 <= hh < H and visited[hh][x][y] == 0 and tomato[hh][x][y] == 0:
                tomato[hh][x][y] = 1
                visited[hh][x][y] = visited[h][x][y] + 1
                queue.append((hh, x, y))

    for h in range(H):
        for i in range(N):
            for j in range(M):
                if tomato[h][i][j] == 0:
                    print(-1)
                    exit(0)
                day = max(visited[h][i][j], day)
    else:

        print(day - 1)
