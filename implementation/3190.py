import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
k = int(input())
maps = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(k):
    x, y = map(int, input().split())
    maps[x][y] = 2

info = {}
l = int(input())

for _ in range(l):
    t, d = input().split()
    info[int(t)] = d

time = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

x, y = 1, 1
maps[y][x] = 1
d = 0

snakes = deque([(1, 1)])

while True:
    xx, yy = x + dx[d], y + dy[d]

    if xx <= 0 or yy <= 0 or xx > n or yy > n or (xx, yy) in snakes:
        break
    if maps[yy][xx] != 2:  # 사과가 없으면
        a, b = snakes.popleft()
        maps[b][a] = 0

    x, y = xx, yy
    maps[y][x] = 1
    snakes.append((xx, yy))
    time += 1

    if time in info.keys():
        if info[time] == "D":
            d = (d + 1) % 4
        else:
            nd = 3 if d == 0 else d - 1
            d = nd


print(time + 1)
