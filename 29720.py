n, m, k = map(int, input().split())
result1 = n - m*k
if result1 < 0:
    result1 = 0
result2 = n - (m * (k-1) + 1)
if result2 < 0:
    result2 = 0
print(result1, result2)