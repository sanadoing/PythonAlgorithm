n = int(input())
numbers = [0] * 10001
for i in range(n):
    numbers[i] = int(input())

dp = [0] * 10001
dp[0] = numbers[0]
dp[1] = numbers[0] + numbers[1]
dp[2] = max(numbers[2]+dp[0], numbers[2]+numbers[1], dp[1])
for i in range(3, n):
    dp[i] = max(numbers[i]+numbers[i-1]+dp[i-3], numbers[i]+dp[i-2], dp[i-1])

print(dp[n-1])

