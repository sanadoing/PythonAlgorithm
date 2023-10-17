from collections import deque
from copy import deepcopy

N = int(input())
input_board = [list(map(int, input().split())) for _ in range(N)]
result = 0


def move(direction, board):
    # top
    if direction == 0:

        for x in range(N):
            not_zero = []
            for y in range(N):

                # 세로로 한줄씩 읽어가며 0이 아닌 값을 not_zero 리스트에 넣어줍니다.
                if board[y][x] != 0:
                    not_zero.append(board[y][x])

            idx = 0
            not_zero = deque(not_zero)

            while not_zero:     #   0이 아닌 값이 있다면 합쳐줘야할 값이 있으므로,
                if len(not_zero) == 1:
                    board[idx][x] = not_zero.popleft()

                else:
                    #   합쳐지는 수는 2개 이므로 두 개를 popleft합니다.
                    a, b = not_zero.popleft(), not_zero.popleft()
                    #   만약 그 두개의 수가 같다면
                    if a == b:
                        #    board에 업데이트를 해줍니다.
                        board[idx][x] = a + b
                    else:   # 만약 그 두 개의 수가 다르다면
                        #   두 개의 수 중 앞에 있는 값은 다른 수와 합쳐질 기회가 없으므로 앞의 수만 board에 업데이트를 해줍니다.
                        board[idx][x] = a
                        #   두 개의 수 중 뒤의 수는 그 다음 수와 합칠 기회가 있으므로 다시 넣어줍니다.
                        not_zero.appendleft(b)
                #   업데이트할 board의 idx값을 + 1 해줍니다.
                idx += 1

            #   가능한 모든 값을 합치고, 또 합쳐지지 못한 수도 다 board에 업데이트가 되었으므로,
            #   그 뒤의 값은 0으로 채워줍니다.
            for y in range(idx, N):
                board[y][x] = 0

    # down
    elif direction == 1:

        for x in range(N):
            not_zero = []
            for y in range(N - 1, -1, -1):
                if board[y][x] != 0:
                    not_zero.append(board[y][x])

            idx = N - 1
            not_zero = deque(not_zero)

            while not_zero:
                if len(not_zero) == 1:
                    board[idx][x] = not_zero.popleft()

                else:
                    a, b = not_zero.popleft(), not_zero.popleft()
                    if a == b:
                        board[idx][x] = a + b
                    else:
                        board[idx][x] = a
                        not_zero.appendleft(b)
                idx -= 1

            for y in range(idx, -1, -1):
                board[y][x] = 0

    # left
    elif direction == 2:

        for x in range(N):
            not_zero = []
            for y in range(N):
                if board[x][y] != 0:
                    not_zero.append(board[x][y])

            idx = 0
            not_zero = deque(not_zero)

            while not_zero:
                if len(not_zero) == 1:
                    board[x][idx] = not_zero.popleft()

                else:
                    a, b = not_zero.popleft(), not_zero.popleft()
                    if a == b:
                        board[x][idx] = a + b
                    else:
                        board[x][idx] = a
                        not_zero.appendleft(b)
                idx += 1

            for y in range(idx, N):
                board[x][y] = 0

    # right
    else:
        for x in range(N):
            not_zero = []
            for y in range(N - 1, -1, -1):
                if board[x][y] != 0:
                    not_zero.append(board[x][y])

            idx = N - 1
            not_zero = deque(not_zero)

            while not_zero:
                if len(not_zero) == 1:
                    board[x][idx] = not_zero.popleft()

                else:
                    a, b = not_zero.popleft(), not_zero.popleft()
                    if a == b:
                        board[x][idx] = a + b
                    else:
                        board[x][idx] = a
                        not_zero.appendleft(b)
                idx -= 1

            for y in range(idx, -1, -1):
                board[x][y] = 0
    return board


def DFS(board, cnt):
    global result

    #   board를 움직일 수 있는 건 최대 5번 이므로, cnt = 5일 때, return 해줍니다.
    if cnt == 5:
        for i in range(N):
            for j in range(N):
                result = max(result, board[i][j])
        return

    #   위, 아래, 왼쪽, 오른쪽 4방향 움직일 수 있기 때문에
    for i in range(4):
        #   각각 처음 board를 바꾸면 안되기 때문에, deepcopy를 사용하여 리스트를 복사하여 줍니다.
        temp_board = move(i, deepcopy(board))
        DFS(temp_board, cnt + 1)


DFS(input_board, 0)
print(result)

