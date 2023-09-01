from collections import deque
import sys
input = sys.stdin.readline

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

if __name__ == "__main__":

    M, N = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(N)]

    queue = deque()
    result = 0

    for i in range(N):
        for j in range(M):
            if box[i][j] == 1:
                queue.append((i, j, 0))

    if len(queue) == N*M:
        print(0)
    else:
        while queue:

            x, y, cnt = queue.popleft()
            for i in range(4):
                xx = dx[i] + x
                yy = dy[i] + y
                if 0 <= xx < N and 0 <= yy < M and box[xx][yy] == 0:
                    box[xx][yy] = 1
                    queue.append((xx, yy, cnt+1))
                    result = cnt+1


        for i in range(N):
            if 0 in box[i]:
                print(-1)
                break
        else:
            print(result)