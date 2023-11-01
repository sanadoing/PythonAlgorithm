T = int(input())

for _ in range(T):
    N = int(input())
    dp = [1] * (N + 1)  # 1으로만 이룰 수 있는 방법
    for i in range(2, 4):  # 2, 3으로 이룰 수 있는 방법
        for j in range(i, N + 1):
            dp[j] += dp[j - i]

    print(dp[-1])
