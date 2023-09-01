import sys
import copy

input = sys.stdin.readline


# 각 빙산마다 접해있는 바닷물의 수에 따라 빙산을 녹임.
def melt_ice():
    ice_to_water = []  # 빙산을 녹였는데 그 빙산이 물이 되어버렸을 경우에 그 위치를 담을 리스트

    for c in range(len(ice)):
        x, y = ice[c][0], ice[c][1]

        # 빙산이 아니라면 아래의 코드(1)에 바닷물로 취급해주기 때문에, 빙산이였다가 바닷물이 되지 않은 빙산만 녹여준다.
        if water_cnt[x][y] != 0:
            # 만약 빙산에 위치에 바다에 접해있는 수가 더 크면 그 자리는 마이너스 값이 되므로 0인 바닷물로 만들어준다.
            if water_cnt[x][y] > board[x][y]:
                board[x][y] = 0
            else:  # 그렇지 않다면 바닷물의 수 만큼 빙산을 녹여준다.
                board[x][y] -= water_cnt[x][y]

            if board[x][y] == 0:  # 빙산이 바닷물이 되었을 경우, ice_to_water 리스트에 추가
                ice_to_water.append((x, y))

    # 빙산을 녹이다가 바닷물이 된 자리가 있을 경우
    for w in range(len(ice_to_water)):
        x, y = ice_to_water[w][0], ice_to_water[w][1]
        water_cnt[x][y] = 0  # 더이상 빙산이 아니기 때문에 0으로 바닷물로 취급해준다.       ------ (1)
        ice.remove((x, y))

        # # 빙산이 바닷물이 되었을 경우, 그 주위에 있는 빙산에 접해있는 바닷물의 수를 +1 씩 해주어야 한다.
        for t in range(4):
            xx = x + dx[t]
            yy = y + dy[t]
            if 0 <= xx < N and 0 <= yy < M and board[xx][yy] != 0:
                water_cnt[xx][yy] += 1

    # ice 수를 리턴함에 따라서 빙산이 다 녹았는데도, 빙산 덩어리가 2개가 아닌 경우를 판단
    return len(ice)


# 빙산 덩어리의 갯수를 리턴하는 함수
def ice_group():
    queue = []
    visited = copy.deepcopy(board)  # 방문한 자리인지를 판단하기 위한 리스트

    group_cnt = 0  # 빙산 덩어리의 수
    for a in range(N):
        for b in range(M):
            if visited[a][b] != 0:
                group_cnt += 1  # 덩어리 하나가 끝날 때마다 cnt + 1
                queue.append((a, b))

                while queue:
                    x, y = queue.pop()
                    for i in range(4):
                        xx = x + dx[i]
                        yy = y + dy[i]
                        if 0 <= xx < N and 0 <= yy < M and board[xx][yy] != 0 and visited[xx][yy] != 0:
                            visited[xx][yy] = 0
                            queue.append((xx, yy))

    # 빙산의 덩어리 수 리턴
    return group_cnt


N, M = map(int, input().split())
board = []

for i in range(N):
    board.append(list(map(int, input().split())))

ice = []  # ice 의 위치만을 저장할 리스트 : 매번 전체 board 를 탐색하기엔 시간이 너무 많이 걸림.
water_cnt = [[0] * M for _ in range(N)]  # 주위에 바닷물이 접해있는 수
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 제일 처음 빙산이 어디에 있고, 각 빙산자리에 바닷물이 얼마나 접해있는지에 대해 탐색하는 반복문
for i in range(N):
    for j in range(M):
        if board[i][j] != 0:
            cnt = 0
            for k in range(4):
                xx = i + dx[k]
                yy = j + dy[k]
                if 0 <= xx < N and 0 <= yy < M and board[xx][yy] == 0:
                    cnt += 1
            ice.append((i, j))  # 여기서 1의 의미는 빙산이라는 뜻, 0이면 water가 됨.
            water_cnt[i][j] = cnt

# 빙산 덩어리가 두 개 이상일 때까지 반복 !
year = 0

# 0년이여도, 빙산 덩어리가 2개일 수도 있으므로
if ice_group() > 1:
    print(year)

# 아니라면 1년씩 증가해가며 빙산을 바닷물이 접해있는 수마다 빙산을 녹여줌.
else:

    while True:
        # 1년씩 증가
        year += 1

        # 빙산을 다 녹일때까지도 빙산 덩어리가 2개 이상이 안되었을 경우
        if melt_ice() == 0:
            print(0)
            break

        # 빙산 덩어리의 수가 2개 이상일 경우 결과값인 year 출력
        if ice_group() > 1:
            print(year)
            break
