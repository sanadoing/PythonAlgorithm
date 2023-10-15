from collections import deque

# 북 동 남 서
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

dice_ud = deque([2, 1, 5, 6])  # 뒤, 윗면, 앞, 밑면
dice_rl = deque([4, 1, 3, 6])  # 왼, 윗면, 오, 밑면

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dice_y, dice_x = 0, 0
dice_d = 1  # 주사위 맨 처음 방향 : 동쪽
result = 0


def BFS(y, x, number):
    global board

    visited = [[0] * M for _ in range(N)]
    queue = deque()
    queue.append([y, x])
    cnt = 0
    visited[y][x] = 1
    while queue:
        y, x = queue.popleft()
        cnt += 1
        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]
            if 0 <= yy < N and 0 <= xx < M and visited[yy][xx] == 0 and board[yy][xx] == number:
                visited[yy][xx] = 1
                queue.append([yy, xx])
    return cnt * number


def move_dice(dice_d):
    global result, dice_rl, dice_ud

    if dice_d == 0:  # 이동 방향이 북일 경우
        dice_ud.append(dice_ud.popleft())
        dice_rl[1] = dice_ud[1]
        dice_rl[3] = dice_ud[3]
    elif dice_d == 1:  # 이동 방향이 동일 경우
        dice_rl.appendleft(dice_rl.pop())
        dice_ud[1] = dice_rl[1]
        dice_ud[3] = dice_rl[3]
    elif dice_d == 2:  # 이동 방향이 남일 경우
        dice_ud.appendleft(dice_ud.pop())
        dice_rl[1] = dice_ud[1]
        dice_rl[3] = dice_ud[3]
    else:  # 이동 방향이 서일 경우
        dice_rl.append(dice_rl.popleft())
        dice_ud[1] = dice_rl[1]
        dice_ud[3] = dice_rl[3]


for i in range(K):

    ny = dice_y + dy[dice_d]
    nx = dice_x + dx[dice_d]

    # # 이동 방향에 칸 없다면 이동 방향 반대로
    if ny < 0 or nx < 0 or ny >= N or nx >= M:
        dice_d = (dice_d - 2) % 4
        ny = dice_y + dy[dice_d]
        nx = dice_x + dx[dice_d]

    dice_y, dice_x = ny, nx

    move_dice(dice_d)
    A = dice_ud[3]
    B = board[dice_y][dice_x]
    result += BFS(dice_y, dice_x, B)

    if A > B:
        dice_d = (dice_d + 1) % 4
    elif A < B:
        dice_d = (dice_d - 1) % 4
    else:
        dice_d = dice_d

print(result)
