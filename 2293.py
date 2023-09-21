# N, K = map(int, input().split())
# coin = []
#
# for i in range(N):
#     coin.append(int(input()))
#
# result = set()
#
#
# def recursive(num, cnt):
#     global result
#
#     for i in range(N):
#         if num - coin[i] < 0:
#             continue
#         elif num - coin[i] == 0:
#             cnt[i] += 1
#
#             # result.add(cnt)
#             print(num - coin[i], cnt)
#             continue
#         elif num - coin[i] > 0:
#             cnt[i] += 1
#             recursive(num - coin[i], cnt)
#
# for i in range(N):
#
#     c = [0] * N
#     if K - coin[i] < 0:
#         continue
#     elif K - coin[i] == 0:
#         c[i] += 1
#
#         # result.add(cnt)
#
#         continue
#     elif K - coin[i] > 0:
#         c[i] += 1
#
#         recursive(K - coin[i], c)
#
# # recursive(K, [0] * N)
# print()

n, k = map(int, input().split())
coin = []
for _ in range(0, n):
    coin.append(int(input()))

dp = [0] * (k+1)
dp[0] = 1

for c in coin:
    for i in range(c, k+1):
        dp[i] = dp[i] + dp[i-c]

print(dp[k])