A, B = map(int, input().split())
K, X = map(int, input().split())

if K+X < A or B < K-X:
    print("IMPOSSIBLE")
else:
    result = (X - max(A, K-X)) + (min(B, K+X) - X) + 1
    print(result)