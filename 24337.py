N, a, b = map(int, input().split())
result = []
for i in range(1, a):
    result.append(i)
result.append(max(a, b))
for i in range(b - 1, 0, -1):
    result.append(i)

if len(result) > N:
    print(-1)
else:
    print(result[0], end=' ')
    for _ in range(N - len(result)):
        print(1, end=' ')
    for i in range(1, len(result)):
        print(result[i], end=' ')
