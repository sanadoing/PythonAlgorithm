N, T = map(int, input().split())
result = int(1e9)
bus = []
for _ in range(N):
    s, i, n = map(int, input().split())
    for j in range(n):
        if s + i * j >= T:
            result = min(result, s + i * j - T)
            break
if result == int(1e9):
    print(-1)
else:
    print(result)
