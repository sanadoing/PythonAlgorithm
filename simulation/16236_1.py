import sys
from collections import deque

input = sys.stdin.readline

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

N = int(input())
board = []
shark_y, shark_x, shark_size, shark_cnt = 0, 0, 2, 0  # [size, y, x, cnt] board[y][x] 위치에 size 크기의 물고기 cnt : 물고기 먹은 수
result = 0  # 엄마 상어의 도움을 요청할 때까지의 시간

for y in range(N):
    temp_list = list(map(int, input().split()))
    board.append(temp_list)

    for x in range(N):
        if board[y][x] == 9:
            shark_y, shark_x = y, x


def eat_fish():
    global shark_y, shark_x, shark_size, shark_cnt
    distance = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    queue = deque()
    queue.append((shark_y, shark_x))
    visited[shark_y][shark_x] = 1
    temp = []

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            yy, xx = y + dy[i], x + dx[i]
            if 0 <= yy < N and 0 <= xx < N and visited[yy][xx] == 0:
                if board[yy][xx] <= shark_size:
                    queue.append((yy, xx))
                    visited[yy][xx] = 1
                    distance[yy][xx] = distance[y][x] + 1
                    if board[yy][xx] < shark_size and board[yy][xx] != 0:
                        temp.append((y, x, distance[y][x]))

    return sorted(temp, key=lambda x: (-x[2], -x[0], -x[1]))


while True:
    fish = eat_fish()

    if len(fish) == 0:
        break

    n_y, n_x, n_d = fish.pop()
    result += n_d
    board[n_y][n_x], board[shark_y][shark_x] = 0, 0

    shark_y, shark_x = n_y, n_x
    shark_cnt += 1

    if shark_cnt == shark_size:
        shark_size += 1
        shark_cnt = 0

print(result)
