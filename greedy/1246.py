import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
p = sorted((int(input()) for _ in range(M)), reverse=True)

max_profit = 0
price = 0

for i in range(min(M, N)):
    profit = (i + 1) * p[i]  # 거꾸로 정렬 했으며, i가 살 수 있는 사람의 수이다.

    if profit >= max_profit:
        price = p[i]
        max_profit = profit

print(price, max_profit)
