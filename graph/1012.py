import sys
sys.setrecursionlimit(10000)

def DFS(x, y):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for k in range(4):
        ddx = dx[k] + x
        ddy = dy[k] + y
        if 0 <= ddx < M and 0 <= ddy < N and List[ddx][ddy] == 1:
            List[ddx][ddy] = 0
            DFS(ddx, ddy)
    else:
        return 0


if __name__ == "__main__":

    T = int(input())

    for _ in range(T):
        M, N, K = map(int, input().split())
        List = [[0 for _ in range(N)] for _ in range(M)]

        for _ in range(K):
            x, y = map(int, input().split())
            List[x][y] = 1

        cnt = 0
        for i in range(M):
            for j in range(N):
                if List[i][j] == 1:
                    DFS(i, j)
                    cnt += 1

        print(cnt)
