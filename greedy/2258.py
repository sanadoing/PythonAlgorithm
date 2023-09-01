import sys

input = sys.stdin.readline

N, M = map(int, input().split())
beaf = []

for _ in range(N):
    weight, price = map(int, input().split())
    beaf.append((price, weight))

beaf.sort(key=lambda x: (x[0], -x[1]))

weight_sum = 0
same_price = 0
result = sys.maxsize

for i in range(N):
    weight_sum += beaf[i][1]

    if i > 0 and beaf[i][0] == beaf[i - 1][0]:
        same_price += beaf[i][0]
    else:
        same_price = 0

    if weight_sum >= M:
        result = min(result, beaf[i][0] + same_price)

if result != sys.maxsize:
    print(result)
else:
    print(-1)
