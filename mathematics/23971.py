import math

H, W, N, M = map(int, input().split())

A = math.ceil(W / (M + 1))
B = math.ceil(H / (N + 1))
print(A, B)
print(A * B)
