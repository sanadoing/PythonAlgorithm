N = int(input())
numbers = [0]
result = 0
for _ in range(N):
    numbers.append(int(input()))
dp = [1] * (N+1)
for i in range(1, N+1):
    for j in range(1, i):
        if numbers[j] < numbers[i]:
            dp[i] = max(dp[j]+1, dp[i])
print(N - max(dp))