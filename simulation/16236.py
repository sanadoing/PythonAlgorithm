from collections import deque

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

N = int(input())
board = []
fish = []  # [size, y, x] board[y][x] 위치에 size 크기의 물고기
shark = []  # [size, y, x, cnt] board[y][x] 위치에 size 크기의 물고기 cnt : 물고기 먹은 수
result = 0  # 엄마 상어의 도움을 요청할 때까지의 시간


def eat_fish():
    global shark
    queue = deque()

    queue.append((shark[1], shark[2], 5))
    visited = [[0] * N for _ in range(N)]
    visited[shark[1]][shark[2]] = 1

    while queue:

        y, x, direction = queue.popleft()
        if 0 < board[y][x] < shark[0]:
            return direction

        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]
            # 먹을 수 있는 물고기 발견하여 그 물고기 방향 리턴

            if 0 <= yy < N and 0 <= xx < N and visited[yy][xx] == 0 and 0 <= board[yy][xx] <= shark[0]:
                visited[yy][xx] = 1
                if direction == 5:
                    queue.append((yy, xx, i))
                else:
                    queue.append((yy, xx, direction))
    return -1


for i in range(N):
    temp_list = list(map(int, input().split()))
    board.append(temp_list)

    for j in range(N):
        if board[i][j] == 9:
            shark = [2, i, j, 0]
            board[i][j] = 0
        elif board[i][j] != 0:
            fish.append([board[i][j], i, j])

fish.sort()

while True:

    # 먹을 물고기가 없거나, board에 있는 가장 크기가 작은 물고기의 크기가 상어보다 같거나 클 때
    if len(fish) == 0 or fish[0][0] >= shark[0]:
        break
    else:
        d = eat_fish()  # 먹을 수 있는 물고기의 위치 방향 구하기
        if d == -1:
            break
        shark_y = shark[1] + dy[d]
        shark_x = shark[2] + dx[d]

        if board[shark_y][shark_x] != 0 and board[shark_y][shark_x] < shark[0]:  # 이동 방향에 먹을 수 있는 물고기 있음
            shark[3] += 1
            fish.remove([board[shark_y][shark_x], shark_y, shark_x])
            board[shark_y][shark_x] = 0
            shark[1], shark[2] = shark_y, shark_x

        else:  # 이동 방향에 물고기 없음
            shark[1], shark[2] = shark_y, shark_x


    if shark[0] == shark[3]:
        shark[0] += 1
        shark[3] = 0
    result += 1
print(result)
