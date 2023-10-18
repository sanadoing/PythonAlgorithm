from collections import deque

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

N = int(input())
board = []
shark_x, shark_y = 0, 0
shark_eat = 0
shark_size = 2
result = 0

for i in range(N):
    temp_board = list(map(int, input().split()))
    board.append(temp_board)
    for j in range(N):
        if board[i][j] == 9:
            shark_y, shark_x = i, j
            board[i][j] = 0


def find_fish():
    global shark_size, shark_y, shark_x
    visited = [[0] * N for _ in range(N)]
    distance = [[0] * N for _ in range(N)]
    can_eat_fish = []
    queue = deque()
    queue.append([shark_y, shark_x])

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]
            if 0 <= yy < N and 0 <= xx < N:
                if visited[yy][xx] == 0 and board[yy][xx] <= shark_size:
                    visited[yy][xx] = 1
                    distance[yy][xx] = distance[y][x] + 1
                    queue.append([yy, xx])

                    if board[yy][xx] < shark_size and board[yy][xx] != 0:
                        can_eat_fish.append([yy, xx, distance[yy][xx]])

    can_eat_fish.sort(key=lambda x: (x[2], x[0], x[1]))

    return can_eat_fish


while True:
    fish_list = find_fish()

    if len(fish_list) == 0:
        break

    shark_y, shark_x, time = fish_list[0]
    shark_eat += 1

    if shark_size == shark_eat:
        shark_size += 1
        shark_eat = 0

    board[shark_y][shark_x] = 0
    result += time

print(result)
