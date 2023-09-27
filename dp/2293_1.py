n, k = map(int, input().split())
coin = list(int(input()) for _ in range(n))

dp = [0] * (k + 1)
dp[0] = 1

for c in coin:
    for j in range(c, k + 1):
        dp[j] = dp[j] + dp[j - c]

print(dp[-1])
