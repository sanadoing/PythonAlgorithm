import sys
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

mx, mn = -sys.maxsize, sys.maxsize

for i in range(N):
    mx = max(mx, max(board[i]))  # board에 있는 값 중 최댓값 저장
    mn = min(mn, min(board[i]))  # board에 있는 값 중 최솟값 저장

result = 0

for h in range(0, mx + 1):  # 최소 높이에서 최대 높이까지 탐색
    visited = [[0] * N for _ in range(N)]  # 방문한 지역
    cnt = 0  # 높이에 따라 물에 안젖은 지역 갯수
    for i in range(N):

        for j in range(N):
            if visited[i][j] == 0 and board[i][j] > h:
                visited[i][j] = 1

                queue = deque()
                queue.append((i, j))
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        xx = x + dx[k]
                        yy = y + dy[k]
                        if 0 <= xx < N and 0 <= yy < N and visited[xx][yy] == 0 and board[xx][yy] > h:
                            visited[xx][yy] = 1
                            queue.append((xx, yy))

                cnt += 1

    result = max(cnt, result)

print(result)
