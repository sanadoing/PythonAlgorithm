n, k = map(int, input().split())
dp = [[1] * 201 for _ in range(201)]
for i in range(n):
    dp[i][0] = i + 1
for y in range(1, k):
    for x in range(n):
        dp[y][x] = (dp[y-1][x] + dp[y][x-1]) % 1000000000
print(dp[k-1][n-1])