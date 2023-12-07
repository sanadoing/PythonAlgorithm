n = int(input())
dp = [0] * (n + 1)
dp[0], dp[1] = 1, 2
for i in range(2, n):
    dp[i] = (dp[i - 2] + dp[i - 1]) % 15746
print(dp[n - 1])
