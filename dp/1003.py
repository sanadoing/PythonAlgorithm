T = int(input())
numbers = [int(input()) for _ in range(T)]
max_n = max(numbers)
dp = [[0, 0]] * (max_n + 1)
for i in range(max_n + 1):
    if i == 0:
        dp[0] = [1, 0]
    elif i == 1:
        dp[1] = [0, 1]
    else:
        dp[i] = [(dp[i - 2][0] + dp[i - 1][0]), (dp[i - 2][1] + dp[i - 1][1])]
for n in numbers:
    print(dp[n][0], dp[n][1])

# T = int(input())
# for _ in range(T):
#     N = int(input())
#     zero, one = 1, 0  # zero: 0개수, one: 1개수
#     for i in range(N):
#         zero, one = one, zero + one  # zero와 one에 대해 피보나치적용
#     print(zero, one)
