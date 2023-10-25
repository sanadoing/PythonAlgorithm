import copy
from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
time = 1
cheese_cnt = 0

#   치즈로 둘러싸인 부분은 -> 구멍, (0, 0)은 무조건 치즈조각이 없는 부분이므로 (0, 0)과 이어진 부분은 구멍 X
def hole_find():
    global board
    queue = deque()
    queue.append([0, 0])
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1
    # 구멍이 있다면 그 구멍은 0, 구멍이 아닌 치즈와 접하는 부분은 3
    # 그 다음 치즈를 녹일 때, 3과 접하는 부분의 치즈만 녹이기 위한
    board[0][0] = 3
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            yy, xx = y + dy[i], x + dx[i]
            if 0 <= yy < N and 0 <= xx < M:
                if (board[yy][xx] == 0 or board[yy][xx] == 3) and visited[yy][xx] == 0:
                    queue.append([yy, xx])
                    visited[yy][xx] = 1
                    board[yy][xx] = 3


def cheese_melt():
    global board
    temp_board = copy.deepcopy(board)

    for y in range(1, N - 1):
        for x in range(1, M - 1):
            if board[y][x] == 1:
                for i in range(4):
                    yy = y + dy[i]
                    xx = x + dx[i]
                    #   구멍은 0, 구멍이 아니며 치즈가 없는 부분은 3, 3과 접하는 치즈를 녹임
                    if board[yy][xx] == 3:
                        temp_board[y][x] = 3
                        break
    board = copy.deepcopy(temp_board)

#   치즈가 다 녹기 한시간 전인지를 판단하기 위한 함수
def left_onehour(sy, sx):
    global board, visited2, cheese_cnt
    queue = deque()
    queue.append([sy, sx])
    visited2[sy][sx] = 1
    #   치즈가 다 녹기 한시간 전이라면, 남은 치즈 수를 알기 위한 변수 cheese_cnt
    cheese_cnt += 1
    while queue:
        y, x = queue.popleft()
        cnt = 0
        for i in range(4):
            yy, xx = y + dy[i], x + dx[i]
            if board[yy][xx] == 1:
                if visited2[yy][xx] == 0:
                    visited2[yy][xx] = 1
                    queue.append([yy, xx])
                    cheese_cnt += 1
                cnt += 1

        if cnt == 4:  # 4방향 모두 치즈로 둘러싸인 치즈가 존재한다면, 치즈가 다 녹기 한시간 전이 아님
            return False

    return True


while True:
    flag = True
    visited2 = [[0] * M for _ in range(N)]

    for b in board:
        print(b)
    print()
    print("finding hole")
    hole_find()
    for b in board:
        print(b)
    print()
    #   치즈가 다 녹기 한시간 전인지를 판단하기 위한 코드가 치즈를 녹이기 전에 있는 이유는
    #   처음부터 시간이 1일 때 치즈가 다 녹을 수 있는 경우가 있을 수 있기 때문에 -> 녹이기 전에 판단
    cheese_cnt = 0
    for y in range(N):
        for x in range(M):
            if board[y][x] == 1 and visited2[y][x] == 0:
                if not left_onehour(y, x):
                    flag = False
    if flag:
        print(time)
        print(cheese_cnt)
        break

    print("melting cheese")
    cheese_melt()
    for b in board:
        print(b)
    print()
    visited2 = [[0] * M for _ in range(N)]
    flag = True
    cheese_cnt = 0

    for y in range(N):
        for x in range(M):
            if board[y][x] == 1 and visited2[y][x] == 0:
                if not left_onehour(y, x):
                    flag = False

    if flag:
        print(time + 1)
        print(cheese_cnt)
        break

    time += 1
