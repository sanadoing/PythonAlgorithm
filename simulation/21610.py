import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cloud = []
result = 0

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]


def cloud_find(idx):
    global cloud
    temp_cloud = []
    if idx == 0:  # 맨 처음 구름은 처음 정해진 4개의 구름
        cloud = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]
    else:  # 맨 처음이 아닌 구름은 그 전 구름이 아니면서 바구니의 물의 양이 2가 넘는 바구니의 위치
        for i in range(N):
            for j in range(N):
                if board[i][j] < 2 or (i, j) in cloud:
                    continue
                board[i][j] -= 2
                temp_cloud.append((i, j))
        cloud = temp_cloud


def cloud_move(d, s):
    global cloud
    xx, yy = dx[d - 1] * s, dy[d - 1] * s

    for x, y in cloud:
        #   board의 위 아래 끝과 왼쪽 오른 쪽 끝이 각각 이어져 있기 때문에 나머지를 이용하여 위치를 바꿈.
        x = (x + xx) % N
        y = (y + yy) % N
        #   구름이 있는 위치에 물의 양 + 1
        board[x][y] += 1



# def cloud_to_water():
#     global cloud
#     for c in range(len(cloud)):
#         board[cloud[c][0]][cloud[c][1]] += 1


def four_direction():
    for x, y in cloud:
        cnt = 0
        for i in range(1, 5):
            xx = x + dx[i * 2 - 1]
            yy = y + dy[i * 2 - 1]
            if 0 <= xx < N and 0 <= yy < N and board[xx][yy] != 0:
                cnt += 1
        board[x][y] += cnt


for idx in range(M):
    d, s = map(int, input().split())

    cloud_find(idx)  # 구름 탐색
    cloud_move(d, s)  # 주어진 방향과 수대로 구름 이동하고, 구름이 있는 칸에 물의 양 + 1하고, 4방향 대각선에 물이 있는 만큼 물 증가
    # cloud_to_water()
    four_direction()  # 구름이 있던 자리의 4개의 대각선 방향에 물이 있는 바구니 수만큼 구름이 있는 바구니의 물을 증가

cloud_find(M)

for i in range(N):
    result += sum(board[i])

print(result)
