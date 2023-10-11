import sys

input = sys.stdin.readline

dx8 = [0, -1, -1, -1, 0, 1, 1, 1]
dy8 = [-1, -1, 0, 1, 1, 1, 0, -1]

dx4 = [-1, -1, 1, 1]
dy4 = [-1, 1, 1, -1]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
moves = [list(map(int, input().split())) for _ in range(M)]

clouds = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]
result = 0

for d, s in moves:

    moved_clouds = []
    for x, y in clouds:

        #   board의 위 아래 끝과 왼쪽 오른 쪽 끝이 각각 이어져 있기 때문에 나머지를 이용하여 위치를 바꿈.
        nx = (x + dx8[d - 1] * s) % N
        ny = (y + dy8[d - 1] * s) % N
        #   구름이 있는 위치에 물의 양 + 1
        board[nx][ny] += 1
        moved_clouds.append((nx, ny))

    for x, y in moved_clouds:
        cnt = 0
        for i in range(4):
            xx = x + dx4[i]
            yy = y + dy4[i]
            if xx < 0 or N <= xx or yy < 0 or N <= yy:
                continue
            elif board[xx][yy] > 0:
                cnt += 1
        board[x][y] += cnt


    temp_clouds = []
    for i in range(N):
        for j in range(N):
            if board[i][j] < 2 or (i, j) in moved_clouds:
                continue
            board[i][j] -= 2
            temp_clouds.append((i, j))
    clouds = temp_clouds


for i in range(N):
    result += sum(board[i])

print(result)