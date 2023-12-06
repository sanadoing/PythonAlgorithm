t = int(input())
dp = [1, 1, 1]
for _ in range(t):
    n = int(input())
    if n >= len(dp):
        for i in range(len(dp), n):
            dp.append(dp[-3]+dp[-2])
    print(dp[n-1])
