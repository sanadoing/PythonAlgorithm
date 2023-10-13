dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    board = [[0] * N for _ in range(N)]
    cnt = N * N
    idx_y, idx_x = 0, 0
    direction = 0  # dx, dy의 idx 값
    number = 1
    while cnt:

        board[idx_y][idx_x] = number


        while idx_y + dy[direction] < 0 or idx_y + dy[direction] >= N or idx_x + dx[direction] < 0 or idx_x + dx[
            direction] >= N or board[idx_y + dy[direction]][idx_x + dx[direction]] != 0:
            if cnt == 1:
                break
            direction = (direction + 1) % 4

        idx_x += dx[direction]
        idx_y += dy[direction]

        number += 1
        cnt -= 1

    print(f'#{test_case}')
    for i in range(N):

        print(' '.join(map(str,board[i])))
