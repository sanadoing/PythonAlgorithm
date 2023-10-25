import copy

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

R, C, T = map(int, input().split())
board = []
cleaner = []
result = 0

for i in range(R):
    temp_board = list(map(int, input().split()))
    board.append(temp_board)
    for j in range(C):
        if board[i][j] == -1:
            # 공기 청정기 위치 저장
            cleaner.append([i, j])

# 미세먼지 확산
def dust_spread():
    global board
    tboard = copy.deepcopy(board)
    for y in range(R):
        for x in range(C):
            # 공기청정기도 아니면서, 미세먼지인 경우 확산
            if board[y][x] != 0 and board[y][x] != -1:
                cnt = 0
                dust = board[y][x] // 5
                for i in range(4):
                    yy = y + dy[i]
                    xx = x + dx[i]
                    if 0 <= yy < R and 0 <= xx < C and board[yy][xx] != -1:
                        cnt += 1
                        tboard[yy][xx] += dust

                tboard[y][x] -= board[y][x] // 5 * cnt

    board = copy.deepcopy(tboard)

# 공기 청정기 작동
def cleaner_activate():
    global board, R, C
    tboard = copy.deepcopy(board)

    # 반 시계 방향 작동
    cleaner1 = cleaner[0]
    # 공기청정기에서 바람 나오는 부분
    tboard[cleaner1[0]][cleaner1[1] + 1] = 0
    # 가로 이동 (-> 방향 가로)
    tboard[cleaner1[0]][cleaner1[1] + 2:] = board[cleaner1[0]][cleaner1[1] + 1:-1]
    # 세로 이동 (위로 가는 방향 세로)
    for i in range(cleaner1[0]):
        tboard[i][C - 1] = board[i + 1][C - 1]
    # 가로 이동 (<- 방향 가로)
    if board[0][0] != -1:
        tboard[0][:C - 1] = board[0][1:C]
        # 세로 이동 (아래로 가는 방향 세로)
        for i in range(1, cleaner1[0]):
            tboard[i][0] = board[i - 1][0]
    else:
        tboard[0][1:C - 1] = board[0][2:C]



    # 시계 방향 작동
    cleaner2 = cleaner[1]
    # 공기청정기에서 바람 나오는 부분
    tboard[cleaner2[0]][cleaner2[1] + 1] = 0
    # 가로 이동 (-> 방향 가로)
    tboard[cleaner2[0]][cleaner2[1] + 2:] = board[cleaner2[0]][cleaner2[1] + 1:-1]
    # 세로 이동 (아래로 가는 방향 세로)
    for i in range(cleaner2[0] + 1, R):
        tboard[i][C - 1] = board[i - 1][C - 1]
    # 가로 이동 (<- 방향 가로)
    if board[R - 1][0] != -1:
        tboard[R - 1][0:-1] = board[R - 1][1:]
        # 세로 이동 (위로 가는 방향 세로)
        for i in range(cleaner2[0] + 1, R - 1):
            tboard[i][0] = board[i + 1][0]
    else:
        tboard[R - 1][1:-1] = board[R - 1][2:]

    board = copy.deepcopy(tboard)


for _ in range(T):
    dust_spread()
    cleaner_activate()

# 남은 미세먼지 총량 구하기
for i in range(R):
    for j in range(C):
        if board[i][j] != 0:
            result += board[i][j]

# 공기청정기를 제외한 미세먼지 총량
print(result + 2)
