n = int(input())
dp = [[0] * n for _ in range(n)]
dp[0][0] = int(input())
for i in range(1, n):
    numbers = list(map(int, input().split()))
    for j in range(len(numbers)):
        if j == 0:
            dp[i][0] = dp[i - 1][0] + numbers[j]
        elif j == len(numbers) - 1:
            dp[i][j] = dp[i - 1][len(numbers) - 2] + numbers[j]
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + numbers[j]
print(max(dp[n - 1]))
