from collections import deque
import copy
import sys
from itertools import combinations

input = sys.stdin.readline


def DFS():
    virus = deque()
    Lab1 = copy.deepcopy(Lab)

    for i in range(N):
        for j in range(M):
            if Lab1[i][j] == 2:
                virus.append((i, j))

    while virus:
        x, y = virus.popleft()
        for i in range(4):
            xx = dx[i] + x
            yy = dy[i] + y
            if 0 <= xx < N and 0 <= yy < M:
                if Lab1[xx][yy] == 0:
                    Lab1[xx][yy] = 2
                    virus.append((xx, yy))
            else:
                continue

    global result
    cnt = 0

    for i in range(N):
        cnt += Lab1[i].count(0)
    result = max(result, cnt)


# def Wall(cnt):
#     if cnt == 3:
#         DFS()
#         return
#     else:
#         for i in range(N):
#             for j in range(M):
#                 if Lab[i][j] == 0:
#                     Lab[i][j] = 1
#                     Wall(cnt + 1)
#                     Lab[i][j] = 0

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
N, M = map(int, input().split())
Lab = [list(map(int, input().split())) for _ in range(N)]
result = 0
# Wall(0)

Lab_Zero = []
for i in range(N):
    for j in range(M):
        if Lab[i][j] == 0:
            Lab_Zero.append((i, j))

for z in combinations(Lab_Zero, 3):
    Lab[z[0][0]][z[0][1]] = 1
    Lab[z[1][0]][z[1][1]] = 1
    Lab[z[2][0]][z[2][1]] = 1
    DFS()
    Lab[z[0][0]][z[0][1]] = 0
    Lab[z[1][0]][z[1][1]] = 0
    Lab[z[2][0]][z[2][1]] = 0

print(result)
