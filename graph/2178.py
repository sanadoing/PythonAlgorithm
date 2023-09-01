from collections import deque

if __name__ == "__main__":

    n, m = map(int, input().split())
    miro = []
    queue = []
    queue = deque()
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]

    for _ in range(n):
        miro.append(list(map(int, input())))

    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()

        for k in range(0, 4):
            tx = dx[k] + x
            ty = dy[k] + y
            if -1 < tx < n and -1 < ty < m and miro[tx][ty] == 1:
                miro[tx][ty] = miro[x][y] + 1
                queue.append((tx, ty))

    print(miro[n-1][m-1])
