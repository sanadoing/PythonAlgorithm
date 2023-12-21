n = int(input())
dp = [[1] * 10 for _ in range(n)]

for y in range(1, n):
    for x in range(1, 10):
        dp[y][x] = dp[y-1][x] + dp[y][x-1]
print(sum(dp[n-1])% 10007)