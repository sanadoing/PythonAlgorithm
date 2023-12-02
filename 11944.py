N, M = map(int, input().split())
result = ''
for _ in range(N):
    result += str(N)
if len(result) >= M:
    print(result[:M])
else:
    print(result)
