from collections import deque

dy = ['empty', 0, 0, -1, 1]
dx = ['empty', 1, -1, 0, 0]

dice_ud = deque([0, 0, 0, 0])  # [1] : 위, [3] : 아래
dice_lr = deque([0, 0, 0, 0])  # [0] : 왼, [1] : 위, [2] : 오, [3] : 아래

N, M, y, x, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

commend = list(map(int, input().split()))

for c in commend:

    if 0 <= y + dy[c] < N and 0 <= x + dx[c] < M:

        if c == 1:  # 동쪽으로 이동
            dice_lr.appendleft(dice_lr.pop())
            dice_ud[1] = dice_lr[1]
            dice_ud[3] = dice_lr[3]
        elif c == 2:  # 서쪽
            dice_lr.append(dice_lr.popleft())
            dice_ud[1] = dice_lr[1]
            dice_ud[3] = dice_lr[3]
        elif c == 3:  # 북쪽
            dice_ud.append(dice_ud.popleft())
            dice_lr[1] = dice_ud[1]
            dice_lr[3] = dice_ud[3]
        else:  # 남쪽
            dice_ud.appendleft(dice_ud.pop())
            dice_lr[1] = dice_ud[1]
            dice_lr[3] = dice_ud[3]

        # 주사위 이동
        y += dy[c]
        x += dx[c]

        # 이동한 칸에 쓰여있는 수가 0일 경우,
        if board[y][x] == 0:
            board[y][x] = dice_ud[3]
        else:
            dice_ud[3] = board[y][x]
            dice_lr[3] = board[y][x]
            board[y][x] = 0

        # 주사위의 윗 면 출력
        print(dice_ud[1])
