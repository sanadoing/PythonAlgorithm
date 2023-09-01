from collections import deque
from itertools import combinations
import sys


def distance(chicken):
    result = 0
    for h in home:
        temp = sys.maxsize
        for c in chicken:
            temp = min(temp, abs(h[0] - c[0]) + abs(h[1] - c[1]))
        result += temp

    return result


N, M = map(int, input().split())
city = []

for _ in range(N):
    city.append(list(map(int, input().split())))

home = []
chicken = []
answer = sys.maxsize

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            home.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

for c in combinations(chicken, M):
    answer = min(answer, distance(c))

print(answer)
