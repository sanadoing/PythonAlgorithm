import sys

sys.setrecursionlimit(100000)

def DFS(x, y):
    dx = [1, 1, 0, -1, -1, -1, 0, 1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    for k in range(8):
        xx = dx[k] + x
        yy = dy[k] + y
        if 0 <= xx < h and 0 <= yy < w:
            if island[xx][yy] == 1:
                island[xx][yy] = 0
                DFS(xx, yy)


if __name__ == "__main__":

    while True:
        w, h = map(int, input().split())
        cnt = 0
        if w == 0 and h == 0:
            break

        island = []
        for i in range(h):
            temp = list(map(int, input().split()))
            island.append(temp)

        for i in range(h):
            for j in range(w):
                if island[i][j] == 1:
                    DFS(i, j)
                    cnt += 1

        print(cnt)
        island.clear()
